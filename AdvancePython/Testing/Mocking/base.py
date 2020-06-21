from unittest.mock import Mock


mock = Mock()
print(mock)

# Pass the mock as an argument
def do_something(Mock):
    pass

do_something(mock)

# Patch something
json = mock
print(json)

# Lazy Attributes and Functions - on a fly
print(mock.some_attribute)
print(mock.some_function())
print(json.dumps())

# Return value of mock objects is also a Mock
print(json.loads('{"k": "v"}').get('k'))

# Lets do some assertions and inspections
# -- reset
json = Mock()

json.loads('{"key": "value"}')

# assertions - they pass
json.loads.assert_called()
json.loads.assert_called_once()
json.loads.assert_called_with('{"key": "value"}')
json.loads.assert_called_once_with('{"key": "value"}')

# assert that will fail
json.loads('{"key": "value"}')
# json.loads.assert_called_once()


# -- reset
json = Mock()
json.loads(s='{"key": "value"}')
json.loads.assert_called_with(s='{"key": "value"}')
# fial
# json.loads.assert_called_with('{"key": "value"}')

# Check some Attributes
print(json.loads.call_count)
print(json.loads.call_args)
print(json.loads.call_args_list)
print(json.method_calls)

# Configure Your Mock
mock = Mock(name="Sakhile Masoka Mock")
print(mock)
print(mock.name)

mock = Mock(return_value=True)
print(mock())
print(mock.return_value)

mock = Mock(side_effect=Exception)
mock() # raises and exception
