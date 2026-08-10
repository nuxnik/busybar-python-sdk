# TimestampInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** | ISO 8601 formatted timestamp with timezone | 

## Example

```python
from busybar_python_sdk.models.timestamp_info import TimestampInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TimestampInfo from a JSON string
timestamp_info_instance = TimestampInfo.from_json(json)
# print the JSON string representation of the object
print(TimestampInfo.to_json())

# convert the object into a dict
timestamp_info_dict = timestamp_info_instance.to_dict()
# create an instance of TimestampInfo from a dict
timestamp_info_from_dict = TimestampInfo.from_dict(timestamp_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


