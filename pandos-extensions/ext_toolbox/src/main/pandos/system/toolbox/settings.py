import os


PANDOS_BACKEND_HOST = os.environ.get(
    "PANDOS_BACKEND_HOST",
    default="127.0.0.1",
)

PANDOS_BACKEND_IN_LOCALHOST = any([
    PANDOS_BACKEND_HOST.startswith(prefix)
    for prefix in ("127", "local")
])

PANDOS_BACKEND_PORT = os.environ.get(
    "PANDOS_BACKEND_PORT",
    default="9472",
)

PANDOS_BACKEND_BASEURL = os.environ.get(
    "PANDOS_BACKEND_BASEURL",
    default=f"http{'' if PANDOS_BACKEND_IN_LOCALHOST else 's'}://{PANDOS_BACKEND_HOST}:{PANDOS_BACKEND_PORT}"
)
