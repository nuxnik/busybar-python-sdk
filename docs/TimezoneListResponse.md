# TimezoneListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[TimezoneInfo]**](TimezoneInfo.md) |  | [optional] 

## Example

```python
from busybar_python_sdk.models.timezone_list_response import TimezoneListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneListResponse from a JSON string
timezone_list_response_instance = TimezoneListResponse.from_json(json)
# print the JSON string representation of the object
print(TimezoneListResponse.to_json())

# convert the object into a dict
timezone_list_response_dict = timezone_list_response_instance.to_dict()
# create an instance of TimezoneListResponse from a dict
timezone_list_response_from_dict = TimezoneListResponse.from_dict(timezone_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


