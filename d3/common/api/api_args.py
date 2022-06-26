from datetime import datetime
from typing import Tuple, Optional, List

from d3.common.api.api_base import ApiBase


class ApiSelectionRequest(ApiBase):
    window: Optional[Tuple[datetime, datetime]]


class ApiSelectionResponse(ApiBase):
    timestamp_values: List[datetime]