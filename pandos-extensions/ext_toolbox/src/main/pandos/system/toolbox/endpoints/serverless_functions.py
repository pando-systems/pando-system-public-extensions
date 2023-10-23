import posixpath
import enum
from typing import (
    List,
    cast,
)

from ..settings import PANDOS_BACKEND_BASEURL


ENDPOINT_BASE: List[str] = ["serverless", "function"]


class BackendEndpoints(enum.Enum):
    SERVERLESS_FUNCTIONS_REGISTER = ENDPOINT_BASE + [
        "register",
        "{user_name}",
        "{function_name}",
    ]
    SERVERLESS_FUNCTION_EVALUATION = ENDPOINT_BASE + [
        "evaluate",
        "{user_name}",
        "{function_name}",
        "{payload_uuid}",
    ]

    def url(self, exclude_baseurl: bool = False, **kwargs) -> str:
        components = cast(List[str], self.value)
        if not exclude_baseurl:
            components = [PANDOS_BACKEND_BASEURL] + components
        return posixpath.join(*components).format(**kwargs)

    def flask_endpoint(self, include_base: bool = False) -> str:
        components: List[str] = cast(List[str], self.value)
        if not include_base:
            components = components[len(ENDPOINT_BASE):]
        return posixpath.join(*components).replace("{", "<").replace("}", ">")
