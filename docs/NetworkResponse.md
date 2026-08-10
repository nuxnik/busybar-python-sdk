# NetworkResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**networks** | [**List[Network]**](Network.md) |  | [optional] 

## Example

```python
from busybar-python-sdk.models.network_response import NetworkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkResponse from a JSON string
network_response_instance = NetworkResponse.from_json(json)
# print the JSON string representation of the object
print NetworkResponse.to_json()

# convert the object into a dict
network_response_dict = network_response_instance.to_dict()
# create an instance of NetworkResponse from a dict
network_response_from_dict = NetworkResponse.from_dict(network_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


