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

The SDK provides multiple flexible ways to configure your API key:

#### Quick Start (Default)
```python
import tasepy
# Uses TASE_API_KEY environment variable by default
client = tasepy.quick_client()
```

#### All Configuration Options

**1. Direct API Key**
```python
from tasepy.settings import SettingsBuilder
settings = SettingsBuilder().with_apikey(key="your-direct-api-key").build()
client = tasepy.quick_client(settings_instance=settings)
```

**2. Custom Environment Variable**
```python
# You can use any environment variable name you prefer
settings = SettingsBuilder().with_apikey(environment="MY_CUSTOM_API_KEY").build()
client = tasepy.quick_client(settings_instance=settings)
```

**3. YAML File**
```python
settings = SettingsBuilder().with_apikey(file_path="path/to/your/key.yaml").build()
client = tasepy.quick_client(settings_instance=settings)
```

**4. Custom Provider Function**
```python
def get_api_key():
    # Your custom logic to retrieve API key
    return "your-api-key"

settings = SettingsBuilder().with_apikey(key_provider=get_api_key).build()
client = tasepy.quick_client(settings_instance=settings)
```

#### Environment Variable Setup

**Default Environment Variable (TASE_API_KEY)**
```bash
export TASE_API_KEY="your-tase-api-key"
```

**Custom Environment Variable**
```bash
export MY_CUSTOM_API_KEY="your-tase-api-key"
```

#### YAML File Format
Create a YAML file with this structure:
```yaml
key: "your-tase-api-key"
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