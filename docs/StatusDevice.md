# StatusDevice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial_number** | **str** | Device serial number | 
**usb_mac** | **str** | MAC of USB ethernet device | 
**wifi_mac** | **str** | WIFI MAC | [optional] 
**ble_mac** | **str** | BLE MAC | [optional] 
**otp_valid** | **bool** | Is OTP data valid | 
**otp_model** | **str** | Device model code | [optional] 
**otp_timestamp** | **int** | Production timestamp | [optional] 
**firmware_security** | **str** | Summary of firmware signature protection derived from the wireless coprocessor (Si917) NWP and M4 signature state. \&quot;secure\&quot; - both NWP and M4 firmware signature verification active; \&quot;insecure\&quot; - neither active; \&quot;other\&quot; - mixed state (exactly one active); \&quot;unknown\&quot; - coprocessor info not ready yet.  | 

## Example

```python
from busybar_python_sdk.models.status_device import StatusDevice

# TODO update the JSON string below
json = "{}"
# create an instance of StatusDevice from a JSON string
status_device_instance = StatusDevice.from_json(json)
# print the JSON string representation of the object
print StatusDevice.to_json()

# convert the object into a dict
status_device_dict = status_device_instance.to_dict()
# create an instance of StatusDevice from a dict
status_device_from_dict = StatusDevice.from_dict(status_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


