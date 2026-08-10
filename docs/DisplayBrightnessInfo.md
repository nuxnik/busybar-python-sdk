# DisplayBrightnessInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Displays brightness (0-100/auto) | [optional] 

## Example

```python
from busybar_python_sdk.models.display_brightness_info import DisplayBrightnessInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayBrightnessInfo from a JSON string
display_brightness_info_instance = DisplayBrightnessInfo.from_json(json)
# print the JSON string representation of the object
print DisplayBrightnessInfo.to_json()

# convert the object into a dict
display_brightness_info_dict = display_brightness_info_instance.to_dict()
# create an instance of DisplayBrightnessInfo from a dict
display_brightness_info_from_dict = DisplayBrightnessInfo.from_dict(display_brightness_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


