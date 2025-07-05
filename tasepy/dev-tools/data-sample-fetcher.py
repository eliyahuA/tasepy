import tasepy
from tasepy import quick_client
from tasepy.settings import SettingsBuilder
from pathlib import Path
from datetime import datetime, timedelta

if __name__ == "__main__":
    client = quick_client(
        SettingsBuilder()
        .with_apikey(file_path='./API KEY.yaml')
        .build()
    )
    types = client.indices_basic.get_index_components(182, datetime.now() - timedelta(days=30))
    types.save_pretty_json(
        Path(tasepy.__file__).parent.parent / "tests/unit/responses/indices_basic/samples/components.json"
    )
