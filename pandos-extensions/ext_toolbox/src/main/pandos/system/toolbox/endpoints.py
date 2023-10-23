import posixpath
import enum
from typing import (
    List,
    cast,
)

from .settings import PANDOS_BACKEND_BASEURL


ENDPOINT_BASE_SERVERLESS_FUNCTION: List[str] = ["serverless", "function"]


class BackendEndpoints(enum.Enum):
    SERVERLESS_FUNCTIONS_REGISTER = ENDPOINT_BASE_SERVERLESS_FUNCTION + [
        "register",
        "{user_name}",
        "{function_name}",
    ]
    SERVERLESS_FUNCTION_EVALUATION = ENDPOINT_BASE_SERVERLESS_FUNCTION + [
        "evaluate",
        "{user_name}",
        "{function_name}",
        "{payload_uuid}",
    ]

    def url(self, **kwargs) -> str:
        components = [PANDOS_BACKEND_BASEURL] + ENDPOINT_BASE_SERVERLESS_FUNCTION + cast(List[str], self.value)
        return posixpath.join(*components).format(**kwargs)

    def flask_endpoint(self) -> str:
        components: List[str] = cast(List[str], self.value)
        return posixpath.join(*components).replace("{", "<").replace("}", ">")
