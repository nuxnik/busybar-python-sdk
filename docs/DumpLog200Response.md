# DumpLog200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | 
**path** | **str** | Full path to the written log file | 

## Example

```python
from busybar-python-sdk.models.dump_log200_response import DumpLog200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DumpLog200Response from a JSON string
dump_log200_response_instance = DumpLog200Response.from_json(json)
# print the JSON string representation of the object
print DumpLog200Response.to_json()

# convert the object into a dict
dump_log200_response_dict = dump_log200_response_instance.to_dict()
# create an instance of DumpLog200Response from a dict
dump_log200_response_from_dict = DumpLog200Response.from_dict(dump_log200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


