# StatusSystem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_semver** | **str** | API SemVer | 
**uptime** | **str** | System uptime | 
**boot_time** | **int** | System boot timestamp | 
**auto_update_enabled** | **bool** | Is auto-update enabled | 

## Example

```python
from openapi_client.models.status_system import StatusSystem

# TODO update the JSON string below
json = "{}"
# create an instance of StatusSystem from a JSON string
status_system_instance = StatusSystem.from_json(json)
# print the JSON string representation of the object
print StatusSystem.to_json()

# convert the object into a dict
status_system_dict = status_system_instance.to_dict()
# create an instance of StatusSystem from a dict
status_system_from_dict = StatusSystem.from_dict(status_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


