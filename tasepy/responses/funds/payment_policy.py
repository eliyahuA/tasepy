from ..responses import ResponseComponent, Root, CodeValuePair


class PaymentPolicy(ResponseComponent):
    payment_policy: Root[CodeValuePair]
