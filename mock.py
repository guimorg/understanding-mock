# Mock is a library standard library for Python >3.3
from unittest import mock

# One of the nice conveniences about the mock library is the Mock objecy
mock_object = mock.Mock()

# You can patch libraries, pass mock as an argument...
def myfun(a):
    print(a)

myfun(mock_object)

json = mock_object

# What is nice about mock is that it creates attributes and functions when
# you access them (on the fly).
mock_object.some_attribute
mock_object.some_fun()

# When mocking json, we can do the following
json = mock.Mock()
res = json.loads('{"key": "value"}').get('key')  # A mock function requires no arguments and will accept any arguments you pass!
type(res)
print(res)

# Mock objects contain various information and data on how it was used
json.loads.assert_called()
json.loads.assert_called_with('{"key": "value"}')
json.loads.assert_called_once()
json.loads.assert_called_once_with('{"key": "value"}')