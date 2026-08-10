# HttpAccessInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Access mode | [optional] 
**key_valid** | **bool** | Access key was set and is valid | [optional] 

## Example

```python
from busybar_python_sdk.models.http_access_info import HttpAccessInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HttpAccessInfo from a JSON string
http_access_info_instance = HttpAccessInfo.from_json(json)
# print the JSON string representation of the object
print(HttpAccessInfo.to_json())

# convert the object into a dict
http_access_info_dict = http_access_info_instance.to_dict()
# create an instance of HttpAccessInfo from a dict
http_access_info_from_dict = HttpAccessInfo.from_dict(http_access_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


