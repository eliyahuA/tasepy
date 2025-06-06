from tasepy.responses import ForgivingResponse
from tasepy.responses import indices_basic
from .request_callable import APIRequestExecutor
from tasepy.requests_.parameters import BaseParameters
from tasepy.requests_.headers import LanguageAble
from .base_client import BaseClient


class IndicesBasic:

    def __init__(self,
                 client: BaseClient,
                 request_callable: APIRequestExecutor,
                 ):
        self.request_callable = request_callable
        self.client = client
        # capture by reference to have the object instantiate with the client values at the moment of call
        self._default_header_provider = \
            lambda: LanguageAble(
                accept_language=self.client.accept_language,
                apikey=self.client.settings.api_key
            )
        self._default_url_provider = \
            lambda endpoint_url: (
                self.client.endpoints,
                self.client.endpoints.indices,
                endpoint_url
            )

    def get_indices_list(self):
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.indices.indices_list),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=indices_basic.IndicesList
        )
