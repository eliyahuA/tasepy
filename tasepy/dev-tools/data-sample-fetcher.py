import tasepy
from tasepy import quick_client
from tasepy.settings import SettingsBuilder
from pathlib import Path

if __name__ == "__main__":
    client = quick_client(
        SettingsBuilder()
        .with_apikey(file_path='./dev-tools/API key.yaml')
        .build()
    )
    
    # Fetch companies list data sample for securities
    companies = client.securities_basic.get_companies_list()
    
    # Create securities_basic samples directory if it doesn't exist
    samples_dir = Path(tasepy.__file__).parent.parent / "tests/unit/responses/securities_basic/samples"
    samples_dir.mkdir(parents=True, exist_ok=True)
    
    companies.save_pretty_json(
        samples_dir / "companies-list.json"
    )
