# UpdateStatusInstall


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_allowed** | **bool** | Whether update installation is allowed (battery check) | [optional] 
**event** | **str** | Current update event | [optional] 
**action** | **str** | Current update action | [optional] 
**status** | **str** | Current or last operation status | [optional] 
**detail** | **str** | Optional status detail string | [optional] 
**download** | [**UpdateStatusInstallDownload**](UpdateStatusInstallDownload.md) |  | [optional] 

## Example

```python
from busybar_python_sdk.models.update_status_install import UpdateStatusInstall

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStatusInstall from a JSON string
update_status_install_instance = UpdateStatusInstall.from_json(json)
# print the JSON string representation of the object
print UpdateStatusInstall.to_json()

# convert the object into a dict
update_status_install_dict = update_status_install_instance.to_dict()
# create an instance of UpdateStatusInstall from a dict
update_status_install_from_dict = UpdateStatusInstall.from_dict(update_status_install_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


