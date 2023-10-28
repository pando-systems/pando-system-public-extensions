# Pando System Extension: toolbox

## About

The `toolbox extension` contains a set of tools intended to be shared between the frontend client(s) and
the backend servers. 

## Installation for local development

```commandline
$ PANDOS_DISABLE_MYPYC=1 pip install -e pandos-extensions/ext_toolbox 
```

## Usage

Example 1: Get the function registration URL

```python
from pandos.system.toolbox.endpoints.serverless_functions import BackendEndpoint

user_name = "Devora"
function_name = "hello_world"

# Get the function registration URL via an enum:
function_registration_url = BackendEndpoints.SERVERLESS_FUNCTION_REGISTRATION.url(
    user_name=user_name,
    function_name=function_name,
)
```
