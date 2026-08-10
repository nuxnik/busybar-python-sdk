# BusyTimerSimpleSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**total_time_ms** | **int** |  | 

## Example

```python
from openapi_client.models.busy_timer_simple_settings import BusyTimerSimpleSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BusyTimerSimpleSettings from a JSON string
busy_timer_simple_settings_instance = BusyTimerSimpleSettings.from_json(json)
# print the JSON string representation of the object
print BusyTimerSimpleSettings.to_json()

# convert the object into a dict
busy_timer_simple_settings_dict = busy_timer_simple_settings_instance.to_dict()
# create an instance of BusyTimerSimpleSettings from a dict
busy_timer_simple_settings_from_dict = BusyTimerSimpleSettings.from_dict(busy_timer_simple_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


