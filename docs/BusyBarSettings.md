# BusyBarSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**theme** | **str** |  | 
**show_work_phase_only** | **bool** |  | 
**trigger_smart_home** | **bool** |  | 

## Example

```python
from openapi_client.models.busy_bar_settings import BusyBarSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BusyBarSettings from a JSON string
busy_bar_settings_instance = BusyBarSettings.from_json(json)
# print the JSON string representation of the object
print BusyBarSettings.to_json()

# convert the object into a dict
busy_bar_settings_dict = busy_bar_settings_instance.to_dict()
# create an instance of BusyBarSettings from a dict
busy_bar_settings_from_dict = BusyBarSettings.from_dict(busy_bar_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


