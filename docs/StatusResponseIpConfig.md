# StatusResponseIpConfig

Only present when connected

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_method** | [**WifiIpMethod**](WifiIpMethod.md) |  | [optional] 
**ip_type** | [**WifiIpType**](WifiIpType.md) |  | [optional] 
**address** | **str** |  | [optional] 

## Example

```python
from busybar_python_sdk.models.status_response_ip_config import StatusResponseIpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StatusResponseIpConfig from a JSON string
status_response_ip_config_instance = StatusResponseIpConfig.from_json(json)
# print the JSON string representation of the object
print StatusResponseIpConfig.to_json()

# convert the object into a dict
status_response_ip_config_dict = status_response_ip_config_instance.to_dict()
# create an instance of StatusResponseIpConfig from a dict
status_response_ip_config_from_dict = StatusResponseIpConfig.from_dict(status_response_ip_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


