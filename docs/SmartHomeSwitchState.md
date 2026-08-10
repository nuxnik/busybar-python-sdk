# SmartHomeSwitchState


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **bool** | State of emulated switch. | [optional] 
**startup** | **str** | State of emulated switch on startup. Never sent by the server, but can be specified by the client. | [optional] 

## Example

```python
from openapi_client.models.smart_home_switch_state import SmartHomeSwitchState

# TODO update the JSON string below
json = "{}"
# create an instance of SmartHomeSwitchState from a JSON string
smart_home_switch_state_instance = SmartHomeSwitchState.from_json(json)
# print the JSON string representation of the object
print SmartHomeSwitchState.to_json()

# convert the object into a dict
smart_home_switch_state_dict = smart_home_switch_state_instance.to_dict()
# create an instance of SmartHomeSwitchState from a dict
smart_home_switch_state_from_dict = SmartHomeSwitchState.from_dict(smart_home_switch_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


