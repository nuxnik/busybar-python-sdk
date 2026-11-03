# AppListResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**List[AppInfo]**](AppInfo.md) |  | 

## Example

```python
from busybar_python_sdk.models.app_list_result import AppListResult

# TODO update the JSON string below
json = "{}"
# create an instance of AppListResult from a JSON string
app_list_result_instance = AppListResult.from_json(json)
# print the JSON string representation of the object
print(AppListResult.to_json())

# convert the object into a dict
app_list_result_dict = app_list_result_instance.to_dict()
# create an instance of AppListResult from a dict
app_list_result_from_dict = AppListResult.from_dict(app_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


