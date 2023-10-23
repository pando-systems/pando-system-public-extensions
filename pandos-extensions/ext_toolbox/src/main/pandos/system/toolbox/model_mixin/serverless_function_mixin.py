from pandos.utils.pyobj_serializers import PyObjSerializationFrameworkEnum


class ServerlessFunctionMixin:
    function_name: str
    function_data: str
    function_serialization_framework: PyObjSerializationFrameworkEnum

    @property
    def function(self):
        return self.function_serialization_framework.loads(self.function_data)

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)
