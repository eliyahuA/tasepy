import yaml

from settings import SettingsBuilder
from openapi3 import OpenAPI


if __name__ == "__main__":
    settings = (SettingsBuilder()
                .with_apikey(file_path='./API key.yaml')
                .build())

    with open('./tase openapi specs/funds.yaml') as f:
        spec = yaml.safe_load(f)
    api = OpenAPI(spec)

    api.authenticate('apiKey', settings.api_key)
    api.call_getMutualFundList(parameters={'accept-language': 'en-US', 'listingStatusId': '1'})
