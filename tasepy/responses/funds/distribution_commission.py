from typing import List
from ..responses import ResponseComponent, CodeValuePair, Root


class DistributionCommission(ResponseComponent):
    distribution_commission: Root[CodeValuePair]
