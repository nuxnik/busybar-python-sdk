# TimezoneInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Time zone name | 
**offset** | **str** | Time zone offset from UTC | 
**abbr** | **str** | Time zone abbreviation | 

## Example

```python
from busybar_python_sdk.models.timezone_info import TimezoneInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneInfo from a JSON string
timezone_info_instance = TimezoneInfo.from_json(json)
# print the JSON string representation of the object
print(TimezoneInfo.to_json())

# convert the object into a dict
timezone_info_dict = timezone_info_instance.to_dict()
# create an instance of TimezoneInfo from a dict
timezone_info_from_dict = TimezoneInfo.from_dict(timezone_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


