# UpdateStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**install** | [**UpdateStatusInstall**](UpdateStatusInstall.md) |  | [optional] 
**check** | [**UpdateStatusCheck**](UpdateStatusCheck.md) |  | [optional] 

## Example

```python
from busybar_python_sdk.models.update_status import UpdateStatus

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStatus from a JSON string
update_status_instance = UpdateStatus.from_json(json)
# print the JSON string representation of the object
print(UpdateStatus.to_json())

# convert the object into a dict
update_status_dict = update_status_instance.to_dict()
# create an instance of UpdateStatus from a dict
update_status_from_dict = UpdateStatus.from_dict(update_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


