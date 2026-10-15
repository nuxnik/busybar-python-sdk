# InstallFirmwareUpdate400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message | 
**error_code** | **str** |  | [optional] 

## Example

```python
from busybar_python_sdk.models.install_firmware_update400_response import InstallFirmwareUpdate400Response

# TODO update the JSON string below
json = "{}"
# create an instance of InstallFirmwareUpdate400Response from a JSON string
install_firmware_update400_response_instance = InstallFirmwareUpdate400Response.from_json(json)
# print the JSON string representation of the object
print(InstallFirmwareUpdate400Response.to_json())

# convert the object into a dict
install_firmware_update400_response_dict = install_firmware_update400_response_instance.to_dict()
# create an instance of InstallFirmwareUpdate400Response from a dict
install_firmware_update400_response_from_dict = InstallFirmwareUpdate400Response.from_dict(install_firmware_update400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


