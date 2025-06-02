from typing import List
from ..responses import ResponseComponent


class PaymentPolicyItem(ResponseComponent):
    code: int
    value: str


class Root(ResponseComponent):
    result: List[PaymentPolicyItem]
    total: int


class PaymentPolicy(ResponseComponent):
    payment_policy: Root
