# StatusFirmware


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Firmware version | 
**target** | **int** | Firmware target code | 
**branch** | **str** | Git branch name | 
**build_date** | **str** | Build date | 
**commit_hash** | **str** | Git commit hash (may include -dirty suffix) | 
**intercom_version** | **str** | Intercom handshake version string (forced version, git hash, or \&quot;intercom\&quot; if check disabled) | 
**nwp_version** | **str** | Radio firmware version | [optional] 
**matter_version** | **str** | Matter version | [optional] 

## Example

```python
from openapi_client.models.status_firmware import StatusFirmware

# TODO update the JSON string below
json = "{}"
# create an instance of StatusFirmware from a JSON string
status_firmware_instance = StatusFirmware.from_json(json)
# print the JSON string representation of the object
print StatusFirmware.to_json()

# convert the object into a dict
status_firmware_dict = status_firmware_instance.to_dict()
# create an instance of StatusFirmware from a dict
status_firmware_from_dict = StatusFirmware.from_dict(status_firmware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


