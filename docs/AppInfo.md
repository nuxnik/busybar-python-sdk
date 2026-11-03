# AppInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Application ID | 
**name** | **str** | Human-readable application name | 
**version** | **str** | Application version | 
**api_version** | **str** | Minimum required HTTP API version | 
**author** | **str** | Application author | 
**description** | **str** | Application description | 
**icon_path** | **str** | Application icon path | 
**is_debug** | **bool** | A flag indicating that this app only shows up in debug mode | 

## Example

```python
from busybar_python_sdk.models.app_info import AppInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppInfo from a JSON string
app_info_instance = AppInfo.from_json(json)
# print the JSON string representation of the object
print(AppInfo.to_json())

# convert the object into a dict
app_info_dict = app_info_instance.to_dict()
# create an instance of AppInfo from a dict
app_info_from_dict = AppInfo.from_dict(app_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


