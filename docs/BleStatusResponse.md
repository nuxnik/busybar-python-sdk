# BleStatusResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**address** | **str** | Remote device address. Only present when status is \&quot;connected\&quot;. | [optional] 

## Example

```python
from busybar-python-sdk.models.ble_status_response import BleStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BleStatusResponse from a JSON string
ble_status_response_instance = BleStatusResponse.from_json(json)
# print the JSON string representation of the object
print BleStatusResponse.to_json()

# convert the object into a dict
ble_status_response_dict = ble_status_response_instance.to_dict()
# create an instance of BleStatusResponse from a dict
ble_status_response_from_dict = BleStatusResponse.from_dict(ble_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


