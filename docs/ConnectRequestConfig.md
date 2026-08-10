# ConnectRequestConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssid** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**security** | [**WifiSecurityMethod**](WifiSecurityMethod.md) |  | [optional] 
**ip_config** | [**ConnectRequestConfigIpConfig**](ConnectRequestConfigIpConfig.md) |  | [optional] 

## Example

```python
from busybar_python_sdk.models.connect_request_config import ConnectRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectRequestConfig from a JSON string
connect_request_config_instance = ConnectRequestConfig.from_json(json)
# print the JSON string representation of the object
print(ConnectRequestConfig.to_json())

# convert the object into a dict
connect_request_config_dict = connect_request_config_instance.to_dict()
# create an instance of ConnectRequestConfig from a dict
connect_request_config_from_dict = ConnectRequestConfig.from_dict(connect_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


