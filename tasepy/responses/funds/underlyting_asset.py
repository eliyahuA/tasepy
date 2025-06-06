from ..responses import ResponseComponent, Root, CodeValuePair


class UnderlyingAsset(ResponseComponent):
    underlying_asset: Root[CodeValuePair]
