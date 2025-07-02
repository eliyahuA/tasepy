# TasePy - TASE DataWise API Python SDK

A comprehensive Python SDK for accessing the Tel Aviv Stock Exchange (TASE) DataWise API. Provides typed clients, request builders, and response models for funds and indices data.

## Quick Start

### Installation

```bash
pip install tasepy
```

### Basic Usage

```python
import tasepy

# Create a client with default settings
client = tasepy.quick_client()

# Get list of all funds
funds = client.funds.get_list()
print(f"Found {len(funds.results)} funds")

# Get basic indices information
indices = client.indices_basic.get_list()
print(f"Found {len(indices.results)} indices")
```

### API Key Setup

The SDK automatically looks for your API key in the following order:

1. **Environment variable**: `API_KEY`
2. **YAML file**: `API key.yaml` in your working directory
3. **Direct configuration** (see Advanced Usage)

#### Option 1: Environment Variable
```bash
export API_KEY="your-tase-api-key"
```

#### Option 2: YAML File
Create `API key.yaml` in your project directory:
```yaml
api_key: "your-tase-api-key"
```

### Working with Funds

```python
import tasepy

client = tasepy.quick_client()

# Get all funds
funds = client.funds.get_list()

# Get fund classifications
fund_types = client.funds.get_fund_types()
classifications = client.funds.get_mutual_fund_classifications()

# Get fund exposures and profiles
currency_exposure = client.funds.get_currency_exposure()
share_exposure = client.funds.get_share_exposure()

# Get fund operational data
exchanges = client.funds.get_stock_exchanges()
tax_statuses = client.funds.get_tax_statuses()
```

### Working with Indices

```python
import tasepy

client = tasepy.quick_client()

# Get all indices
indices = client.indices_basic.get_list() 

# Get components of a specific index
components = client.indices_basic.get_components(index_id="your-index-id")
```

## Advanced Usage

### Custom Configuration

```python
from tasepy.settings import SettingsBuilder
from tasepy.clients.tailored import Client
from tasepy.endpoints.factories.yaml_factory import YAMLFactory
from tasepy.requests_.urls import Endpoints

# Build custom settings
settings = SettingsBuilder().with_apikey(environment="CUSTOM_API_KEY").build()

# Create client with custom configuration
client = Client(
    settings,
    YAMLFactory(Endpoints, './endpoints.yaml')
)

# Or use quick_client with custom settings
client = tasepy.quick_client(settings_instance=settings)
```

### Error Handling

```python
import tasepy

try:
    client = tasepy.quick_client()
    funds = client.funds.get_list()
except Exception as e:
    print(f"API Error: {e}")
```

## Development

### Running Tests

```bash
# Install development dependencies
pip install -r dev-requirements.txt

# Run all tests
pytest

# Run specific test categories
pytest tests/unit/          # Unit tests only
pytest tests/integration/   # Integration tests (requires API key)
```

### Requirements

- Valid TASE DataWise API key for integration testing

## API Reference

### Funds Methods

- `get_list()` - Get all available funds
- `get_fund_types()` - Get fund type classifications
- `get_mutual_fund_classifications()` - Get mutual fund classifications
- `get_currency_exposure()` - Get currency exposure profiles
- `get_share_exposure()` - Get share exposure profiles
- `get_stock_exchanges()` - Get stock exchange information
- `get_tax_statuses()` - Get tax status classifications
- `get_listing_statuses()` - Get listing status information
- `get_payment_policies()` - Get payment policy information
- `get_distribution_commissions()` - Get distribution commission data
- `get_tracking_fund_classifications()` - Get tracking fund classifications
- `get_underlying_assets()` - Get underlying asset information

### Indices Methods

- `get_list()` - Get all available indices
- `get_components(index_id)` - Get components of a specific index

## License

[License information here]

## Contributing

[Contributing guidelines here]