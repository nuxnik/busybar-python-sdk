# InstallFirmwareUpdate409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message | 
**error_code** | **str** |  | [optional] 

## Example

```python
from busybar_python_sdk.models.install_firmware_update409_response import InstallFirmwareUpdate409Response

# TODO update the JSON string below
json = "{}"
# create an instance of InstallFirmwareUpdate409Response from a JSON string
install_firmware_update409_response_instance = InstallFirmwareUpdate409Response.from_json(json)
# print the JSON string representation of the object
print(InstallFirmwareUpdate409Response.to_json())

# convert the object into a dict
install_firmware_update409_response_dict = install_firmware_update409_response_instance.to_dict()
# create an instance of InstallFirmwareUpdate409Response from a dict
install_firmware_update409_response_from_dict = InstallFirmwareUpdate409Response.from_dict(install_firmware_update409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


