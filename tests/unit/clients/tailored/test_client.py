from tasepy.responses import funds

from tasepy.clients.tailored import Client


def test_get_funds(mocker):

    mock_settings = mocker.Mock()
    mock_settings.api_key = "test_api_key"

    mock_endpoints = mocker.Mock()
    mock_endpoints.base_url = "https://api.test.com"
    mock_endpoints.funds.group_url = "funds"
    mock_endpoints.funds.funds_list.url = "list"

    mock_factory = mocker.Mock()
    mock_factory.get_endpoints.return_value = mock_endpoints

    mock_response_model = mocker.Mock()
    mock_response_model.model_validate_json = lambda: None
    mocker.patch(funds.fund_list.FundList.__module__, mock_response_model)

    mock_get = mocker.patch('requests.get', return_value=None)
    # mocker.patch('tasepy.responses.funds.fund_list.FundList.model_validate_json', return_value=None)

    client = Client(settings=mock_settings, endpoints_model_factory=mock_factory)
    client.funds.get_funds()
    mock_get.assert_called_once_with(
        'https://api.test.com/funds/list',
        params={'listingStatusId': '1'},
        headers={'accept': 'application/json', 'apikey': 'test_api_key', 'accept-language': 'he-IL'}
    )
