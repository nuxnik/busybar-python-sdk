# ConnectRequestConfigIpConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_method** | [**WifiIpMethod**](WifiIpMethod.md) |  | [optional] 
**address** | **str** |  | [optional] 
**mask** | **str** |  | [optional] 
**gateway** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.connect_request_config_ip_config import ConnectRequestConfigIpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectRequestConfigIpConfig from a JSON string
connect_request_config_ip_config_instance = ConnectRequestConfigIpConfig.from_json(json)
# print the JSON string representation of the object
print ConnectRequestConfigIpConfig.to_json()

# convert the object into a dict
connect_request_config_ip_config_dict = connect_request_config_ip_config_instance.to_dict()
# create an instance of ConnectRequestConfigIpConfig from a dict
connect_request_config_ip_config_from_dict = ConnectRequestConfigIpConfig.from_dict(connect_request_config_ip_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


