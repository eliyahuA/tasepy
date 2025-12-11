# TasePy - TASE DataWise API Python SDK

[![PyPI version](https://img.shields.io/pypi/v/tasepy.svg)](https://pypi.org/project/tasepy/)
[![Python 3.10+](https://img.shields.io/pypi/pyversions/tasepy.svg)](https://pypi.org/project/tasepy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Known Vulnerabilities](https://snyk.io/test/github/eliyahuA/tasepy/badge.svg)](https://snyk.io/test/github/eliyahuA/tasepy)

A comprehensive Python SDK for accessing the Tel Aviv Stock Exchange (TASE) DataWise API. Provides typed clients, request builders, and response models for funds and indices data.

## Scope and Limitations

This SDK currently implements the **4 free API endpoints** from TASE DataHub:

- **Funds** - Fund listings, classifications, and exposure data
- **Indices Basic** - Index listings and components  
- **Indices Online** - Real-time index rates and intraday data
- **Securities Basic** - Security listings, company data, and trading information

TASE DataHub offers additional premium API products beyond these free endpoints. For the complete catalog of available APIs and pricing, visit the official [TASE DataHub](https://www.tase.co.il/en/content/products_lobby/datahub).

Future versions of TasePy may expand to include additional endpoints based on community needs and contributions.

## Quick Start

### Installation

```bash
pip install tasepy
```

### Requirements

Valid TASE DataWise API key, can be obtained at [datahub](https://www.tase.co.il/en/content/products_lobby/datahub)

### Basic Usage

```python
import tasepy

# Create a client with default settings
client = tasepy.quick_client()

# Get list of all funds
funds = client.funds.get_funds()
print(f"Found {len(funds.results)} funds")

# Get basic indices information
indices = client.indices_basic.get_indices_list()
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
funds = client.funds.get_funds()

# Get fund classifications
fund_types = client.funds.get_types()
classifications = client.funds.get_mutual_fund_classifications()

# Get fund exposures and profiles
currency_exposure = client.funds.get_currency_exposure_profiles()
share_exposure = client.funds.get_share_exposure_profiles()

# Get fund operational data
exchanges = client.funds.get_stock_exchanges()
tax_statuses = client.funds.get_tax_statuses()
```

### Working with Indices

```python
import tasepy

client = tasepy.quick_client()

# Get all indices
indices = client.indices_basic.get_indices_list() 

# Get components of a specific index (requires date)
components = client.indices_basic.get_index_components(
    index_id=709,
    date=(27, 11, 2025)
)
```

## Advanced Usage

### Custom Configuration

```python
from tasepy.settings import SettingsBuilder
from tasepy.client import Client
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

## API Reference

### Funds Methods

- `get_funds(listing_status_id=None)` - Get all available funds
- `get_types()` - Get fund type classifications
- `get_mutual_fund_classifications()` - Get mutual fund classifications
- `get_currency_exposure_profiles()` - Get currency exposure profiles
- `get_share_exposure_profiles()` - Get share exposure profiles
- `get_stock_exchanges()` - Get stock exchange information
- `get_tax_statuses()` - Get tax status classifications
- `get_listing_statuses()` - Get listing status information
- `get_payment_policies()` - Get payment policy information
- `get_commissions()` - Get distribution commission data
- `get_tracking_funds_classifications()` - Get tracking fund classifications
- `get_underlying_assets()` - Get underlying asset information

### Indices Basic Methods

- `get_indices_list()` - Get all available indices
- `get_index_components(index_id, date)` - Get components of a specific index for a given date

### Indices Online Methods

- `get_intraday(index_id=None, start_time=None)` - Get intraday index prices with real-time monitoring data
- `get_last_rate(index_id=None)` - Get latest price updates for online indices with current rates and changes
- `get_trading_rate_types()` - Get index trading rate type classifications

### Securities Basic Methods

- `get_trade_securities_list(year, month, day)` - Get traded securities list for a specific date with extensive trading data
- `get_delisted_securities_list(year, month)` - Get delisted securities list for a specific year and month period
- `get_companies_list()` - Get companies list for securities listed on the Tel Aviv Stock Exchange
- `get_illiquid_maintenance_suspension_list()` - Get maintenance, suspension and illiquid securities lists for next trading day
- `get_trading_code_list()` - Get trading codes list providing reference codes for securities trading operations
- `get_securities_types()` - Get securities types classifications for different security instruments traded on TASE

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions to TasePy! Here's how you can help:

### Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/tasepy.git
   cd tasepy
   ```
3. **Set up development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   pip install -r dev-requirements.txt
   ```

### Running Tests

This package has been validated for Python versions 3.12 and 3.14 on Ubuntu 24.04.3 LTS native and Windows11/WSL2

```bash
# Install development dependencies
pip install -r dev-requirements.txt

# Run all tests
pytest

# Run specific test categories
pytest tests/unit/          # Unit tests only
pytest tests/integration/   # Integration tests (requires API key)
pytest tests/examples/      # Test examples (requires API key)
```

#### Multi-Version Testing

For contributors interested in cross-version validation, we maintain a [testing repository](https://github.com/eliyahuA/tasepy-testing) configured with GitHub Codespaces environments for Python 3.10-3.13 testing.

### AI Coding Assistance

If you're using AI coding agents (like Claude Code), this repository includes helpful configuration:

- **CLAUDE.md**: Contains project-specific instructions, development commands, architecture overview, and coding guidelines for AI assistants
- **.claude/ folder**: Contains specialized commands and templates for common development tasks

These files help AI assistants understand the project structure, testing procedures, and development workflows, making AI-assisted development more effective.

### Code of Conduct

This project follows a standard Code of Conduct. Please be respectful and constructive in all interactions.
