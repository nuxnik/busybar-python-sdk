# BusyTimerIntervalSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**interval_work_ms** | **int** |  | 
**interval_rest_ms** | **int** |  | 
**interval_work_cycles_count** | **int** |  | 
**is_autostart_enabled** | **bool** |  | 

## Example

```python
from openapi_client.models.busy_timer_interval_settings import BusyTimerIntervalSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BusyTimerIntervalSettings from a JSON string
busy_timer_interval_settings_instance = BusyTimerIntervalSettings.from_json(json)
# print the JSON string representation of the object
print BusyTimerIntervalSettings.to_json()

# convert the object into a dict
busy_timer_interval_settings_dict = busy_timer_interval_settings_instance.to_dict()
# create an instance of BusyTimerIntervalSettings from a dict
busy_timer_interval_settings_from_dict = BusyTimerIntervalSettings.from_dict(busy_timer_interval_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


