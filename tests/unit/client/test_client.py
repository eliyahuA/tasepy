import pytest
from unittest.mock import Mock
from tasepy.client.client import Client
from tasepy.requests_.parameters import BaseParameters
from tasepy.requests_.headers import Header
from tasepy.requests_.resources import NoResource


@pytest.fixture
def mock_url_components():
    """Common URL components for testing"""
    endpoints = Mock()
    endpoints.base_url = "https://api.test.com"
    
    endpoint_group = Mock()
    endpoint_group.group_url = "funds"
    
    endpoint = Mock()
    endpoint.url = "list"
    
    return endpoints, endpoint_group, endpoint


@pytest.fixture
def mock_params():
    """Common request parameters for testing"""
    params = Mock(spec=BaseParameters)
    params.model_dump.return_value = {"listingStatusId": "1"}
    return params


@pytest.fixture
def mock_headers():
    """Common request headers for testing"""
    headers = Mock(spec=Header)
    headers.model_dump.return_value = {"apikey": "test-key", "accept": "application/json"}
    return headers


@pytest.fixture
def mock_response_model():
    """Common response model for testing"""
    mock_model = Mock()
    mock_parsed_response = Mock()
    mock_model.model_validate_json.return_value = mock_parsed_response
    return mock_model, mock_parsed_response


def test_do_request_success(mocker, mock_url_components, mock_params, mock_headers, mock_response_model):
    """Test successful HTTP request execution"""
    # Mock the requests.get response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '{"name": "test fund"}'
    mock_get = mocker.patch('requests.get', return_value=mock_response)
    
    # Unpack fixtures
    endpoints, endpoint_group, endpoint = mock_url_components
    mock_model, mock_parsed_response = mock_response_model
    
    # Execute the method
    result = Client._do_request(
        url=(endpoints, endpoint_group, endpoint),
        params=mock_params,
        headers=mock_headers,
        response_model=mock_model,
        resource=NoResource()
    )
    
    # Verify HTTP request was made correctly
    mock_get.assert_called_once_with(
        url="https://api.test.com/funds/list",
        params={"listingStatusId": "1"},
        headers={"apikey": "test-key", "accept": "application/json"}
    )
    
    # Verify response parsing
    mock_model.model_validate_json.assert_called_once_with('{"name": "test fund"}')
    
    # Verify return value
    assert result == mock_parsed_response


def test_do_request_http_error(mocker, mock_url_components, mock_params, mock_headers):
    """Test HTTP error handling"""
    # Mock failed HTTP response
    mock_response = Mock()
    mock_response.status_code = 500
    _ = mocker.patch('requests.get', return_value=mock_response)
    
    # Unpack fixtures
    endpoints, endpoint_group, endpoint = mock_url_components
    mock_model = Mock()
    
    # Test that RuntimeError is raised
    with pytest.raises(RuntimeError) as exc_info:
        Client._do_request(
            url=(endpoints, endpoint_group, endpoint),
            params=mock_params,
            headers=mock_headers,
            response_model=mock_model,
            resource=NoResource()
        )
    
    assert "failed with status code 500" in str(exc_info.value)


def test_do_request_rejected_response(mocker, mock_url_components, mock_params, mock_headers):
    """Test API rejection handling"""
    # Mock response with rejection message
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '<html><body>Request Rejected</body></html>'
    _ = mocker.patch('requests.get', return_value=mock_response)
    
    # Unpack fixtures
    endpoints, endpoint_group, endpoint = mock_url_components
    mock_model = Mock()
    
    # Test that RuntimeError is raised for rejection
    with pytest.raises(RuntimeError) as exc_info:
        Client._do_request(
            url=(endpoints, endpoint_group, endpoint),
            params=mock_params,
            headers=mock_headers,
            response_model=mock_model,
            resource=NoResource()
        )
    
    assert "was rejected" in str(exc_info.value)


def test_do_request_with_resource(mocker, mock_params, mock_headers):
    """Test URL construction with resource path"""
    # Mock successful response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '{"name": "test"}'
    mock_get = mocker.patch('requests.get', return_value=mock_response)
    
    # Mock response model
    mock_model = Mock()
    mock_model.model_validate_json.return_value = Mock()
    
    # Setup test data with different URL components
    endpoints = Mock()
    endpoints.base_url = "https://api.test.com"
    endpoint_group = Mock()
    endpoint_group.group_url = "indices"
    endpoint = Mock()
    endpoint.url = "components"
    
    # Resource with path
    resource = Mock()
    resource.resource_path = "/182/2024-01-01"
    
    # Execute the method
    Client._do_request(
        url=(endpoints, endpoint_group, endpoint),
        params=mock_params,
        headers=mock_headers,
        response_model=mock_model,
        resource=resource
    )
    
    # Verify URL construction with resource path
    mock_get.assert_called_once_with(
        url="https://api.test.com/indices/components/182/2024-01-01",
        params={"listingStatusId": "1"},
        headers={"apikey": "test-key", "accept": "application/json"}
    )