import tasepy
from tasepy import quick_client
from tasepy.settings import SettingsBuilder
from pathlib import Path

if __name__ == "__main__":
    client = quick_client(
        SettingsBuilder()
        .with_apikey(file_path='./tasepy/dev-tools/API key.yaml')
        .build()
    )
    
    # Fetch securities types data sample for securities
    securities_types = client.securities_basic.get_securities_types()
    
    # Create securities_basic samples directory if it doesn't exist
    samples_dir = Path(tasepy.__file__).parent.parent / "tests/unit/responses/securities_basic/samples"
    samples_dir.mkdir(parents=True, exist_ok=True)
    
    securities_types.save_pretty_json(
        samples_dir / "securities-types.json"
    )
