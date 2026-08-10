# NetworkInterfaceInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Connection type | 

## Example

```python
from openapi_client.models.network_interface_info import NetworkInterfaceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInterfaceInfo from a JSON string
network_interface_info_instance = NetworkInterfaceInfo.from_json(json)
# print the JSON string representation of the object
print NetworkInterfaceInfo.to_json()

# convert the object into a dict
network_interface_info_dict = network_interface_info_instance.to_dict()
# create an instance of NetworkInterfaceInfo from a dict
network_interface_info_from_dict = NetworkInterfaceInfo.from_dict(network_interface_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


