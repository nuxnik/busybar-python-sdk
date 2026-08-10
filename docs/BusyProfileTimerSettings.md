# BusyProfileTimerSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**total_time_ms** | **int** |  | 
**interval_work_ms** | **int** |  | 
**interval_rest_ms** | **int** |  | 
**interval_work_cycles_count** | **int** |  | 
**is_autostart_enabled** | **bool** |  | 

## Example

```python
from busybar_python_sdk.models.busy_profile_timer_settings import BusyProfileTimerSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BusyProfileTimerSettings from a JSON string
busy_profile_timer_settings_instance = BusyProfileTimerSettings.from_json(json)
# print the JSON string representation of the object
print BusyProfileTimerSettings.to_json()

# convert the object into a dict
busy_profile_timer_settings_dict = busy_profile_timer_settings_instance.to_dict()
# create an instance of BusyProfileTimerSettings from a dict
busy_profile_timer_settings_from_dict = BusyProfileTimerSettings.from_dict(busy_profile_timer_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


