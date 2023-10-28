import uuid
import posixpath

from pandos.system.toolbox.endpoints.serverless_functions import BackendEndpoints


def test_serverless_functions_url_register():
    test_user_name = "Devora"
    test_function_name = "hello_world"
    url_register = BackendEndpoints.SERVERLESS_FUNCTION_REGISTRATION.url(
        user_name=test_user_name,
        function_name=test_function_name,
    )
    expected_ending = posixpath.join("register", test_user_name, test_function_name)
    assert url_register.endswith(expected_ending)


def test_serverless_functions_url_evaluation():
    test_user_name = "Devora"
    test_function_name = "hello_world"
    test_payload_uuid = str(uuid.uuid4())
    url_evaluation = BackendEndpoints.SERVERLESS_FUNCTION_EVALUATION.url(
        user_name=test_user_name,
        function_name=test_function_name,
        payload_uuid=test_payload_uuid,
    )
    expected_ending = posixpath.join("evaluate", test_user_name, test_function_name, test_payload_uuid)
    assert url_evaluation.endswith(expected_ending)


def test_serverless_functions_flask_endpoint_register():
    endpoint_register = BackendEndpoints.SERVERLESS_FUNCTION_REGISTRATION.flask_endpoint()
    expected_ending = posixpath.join("register", "<user_name>", "<function_name>")
    assert endpoint_register.endswith(expected_ending)


def test_serverless_functions_flask_endpoint_evaluation():
    endpoint_evaluation = BackendEndpoints.SERVERLESS_FUNCTION_EVALUATION.flask_endpoint()
    expected_ending = posixpath.join("evaluate", "<user_name>", "<function_name>", "<payload_uuid>")
    assert endpoint_evaluation.endswith(expected_ending)
