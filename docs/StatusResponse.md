# StatusResponse

Wi-Fi status. Only `state` is always present. Fields `ssid`, `bssid`, `channel`, `rssi`, `security`, and `ip_config` are only included when state is \"connected\". 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**ssid** | **str** | Only present when connected | [optional] 
**bssid** | **str** | Only present when connected | [optional] 
**channel** | **int** | Only present when connected | [optional] 
**rssi** | **int** | Only present when connected | [optional] 
**security** | [**WifiSecurityMethod**](WifiSecurityMethod.md) | Only present when connected | [optional] 
**ip_config** | [**StatusResponseIpConfig**](StatusResponseIpConfig.md) |  | [optional] 

## Example

```python
from busybar-python-sdk.models.status_response import StatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatusResponse from a JSON string
status_response_instance = StatusResponse.from_json(json)
# print the JSON string representation of the object
print StatusResponse.to_json()

# convert the object into a dict
status_response_dict = status_response_instance.to_dict()
# create an instance of StatusResponse from a dict
status_response_from_dict = StatusResponse.from_dict(status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


