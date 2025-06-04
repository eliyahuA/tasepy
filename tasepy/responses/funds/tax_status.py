from ..responses import ResponseComponent, Root, CodeValuePair


class TaxStatus(ResponseComponent):
    tax_status: Root[CodeValuePair]
