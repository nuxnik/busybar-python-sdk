# CountdownElement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** | Seconds-based Unix UTC timestamp to count down or up to. Note: it&#39;s a number in a string. | 
**color** | **str** | Color to display the text in, in #RRGGBBAA format | [optional] [default to '#FFFFFFFF']
**direction** | **str** | Whether to count up or down | 
**show_hours** | **str** | When to show the hours position | 

## Example

```python
from busybar-python-sdk.models.countdown_element import CountdownElement

# TODO update the JSON string below
json = "{}"
# create an instance of CountdownElement from a JSON string
countdown_element_instance = CountdownElement.from_json(json)
# print the JSON string representation of the object
print CountdownElement.to_json()

# convert the object into a dict
countdown_element_dict = countdown_element_instance.to_dict()
# create an instance of CountdownElement from a dict
countdown_element_from_dict = CountdownElement.from_dict(countdown_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


