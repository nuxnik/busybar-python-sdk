# TextElement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text content to display (printable ASCII only; fonts are bitmap ASCII) | 
**font** | **str** | One of the available fonts to display the text in | 
**color** | **str** | Color to display the text in, in #RRGGBBAA format | [optional] [default to '#FFFFFFFF']
**width** | **int** | Width of the label | [optional] 
**scroll_rate** | **int** | Scroll rate in pixels per minute | [optional] 
**scroll_start_delay** | **int** | Delay in milliseconds before the scroll animation begins | [optional] 
**scroll_repeat_delay** | **int** | Pause duration in milliseconds between successive scroll cycles | [optional] 

## Example

```python
from busybar_python_sdk.models.text_element import TextElement

# TODO update the JSON string below
json = "{}"
# create an instance of TextElement from a JSON string
text_element_instance = TextElement.from_json(json)
# print the JSON string representation of the object
print TextElement.to_json()

# convert the object into a dict
text_element_dict = text_element_instance.to_dict()
# create an instance of TextElement from a dict
text_element_from_dict = TextElement.from_dict(text_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


