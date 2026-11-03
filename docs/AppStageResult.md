# AppStageResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | Operation result | 
**install_key** | **int** | Single-use installation key | 
**staged** | [**AppInfo**](AppInfo.md) | Staged application info | 
**installed** | [**AppInfo**](AppInfo.md) | If an application with the same ID is already installed, its info | [optional] 

## Example

```python
from busybar_python_sdk.models.app_stage_result import AppStageResult

# TODO update the JSON string below
json = "{}"
# create an instance of AppStageResult from a JSON string
app_stage_result_instance = AppStageResult.from_json(json)
# print the JSON string representation of the object
print(AppStageResult.to_json())

# convert the object into a dict
app_stage_result_dict = app_stage_result_instance.to_dict()
# create an instance of AppStageResult from a dict
app_stage_result_from_dict = AppStageResult.from_dict(app_stage_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


