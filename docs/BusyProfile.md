# BusyProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort_order** | **int** |  | 
**title** | **str** |  | 
**id** | **UUID** |  | 
**timer_settings** | [**BusyProfileTimerSettings**](BusyProfileTimerSettings.md) |  | 
**busy_bar_settings** | [**BusyBarSettings**](BusyBarSettings.md) |  | 
**profile_timestamp_ms** | **int** |  | 

## Example

```python
from busybar_python_sdk.models.busy_profile import BusyProfile

# TODO update the JSON string below
json = "{}"
# create an instance of BusyProfile from a JSON string
busy_profile_instance = BusyProfile.from_json(json)
# print the JSON string representation of the object
print(BusyProfile.to_json())

# convert the object into a dict
busy_profile_dict = busy_profile_instance.to_dict()
# create an instance of BusyProfile from a dict
busy_profile_from_dict = BusyProfile.from_dict(busy_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


