# AutoupdateSettings

Autoupdate configuration settings. All fields are optional for POST requests.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Whether automatic updates are enabled | [optional] 
**interval_start** | **str** | Start of autoupdate window in HH:MM format (e.g., \&quot;08:00\&quot;) | [optional] 
**interval_end** | **str** | End of autoupdate window in HH:MM format (e.g., \&quot;23:59\&quot;) | [optional] 

## Example

```python
from busybar-python-sdk.models.autoupdate_settings import AutoupdateSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AutoupdateSettings from a JSON string
autoupdate_settings_instance = AutoupdateSettings.from_json(json)
# print the JSON string representation of the object
print AutoupdateSettings.to_json()

# convert the object into a dict
autoupdate_settings_dict = autoupdate_settings_instance.to_dict()
# create an instance of AutoupdateSettings from a dict
autoupdate_settings_from_dict = AutoupdateSettings.from_dict(autoupdate_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


