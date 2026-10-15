# DisplayElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the element | 
**timeout** | **int** | Time in seconds the element should be displayed (0 for no timeout). Mutually exclusive with display_until. | [optional] 
**display_until** | **str** | The element will be hidden when system time reaches the specified Unix timestamp (in seconds). Mutually exclusive with timeout. | [optional] 
**type** | **str** | Type of display element | 
**x** | **int** | X coordinate of selected anchor point relative to top-left of display | [optional] [default to 0]
**y** | **int** | Y coordinate of selected anchor point relative to top-left of display | [optional] [default to 0]
**display** | **str** | Which display to show the element on (for dual-display devices) | [optional] [default to 'front']
**align** | **str** | Anchor point of element. Also use &#x60;x&#x60; and &#x60;y&#x60; to position element. | [optional] 
**z_index** | **int** | Order of the element. Elements with higher Z-indexes are drawn on top of those with lower ones. | [optional] 

## Example

```python
from busybar_python_sdk.models.display_element import DisplayElement

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayElement from a JSON string
display_element_instance = DisplayElement.from_json(json)
# print the JSON string representation of the object
print(DisplayElement.to_json())

# convert the object into a dict
display_element_dict = display_element_instance.to_dict()
# create an instance of DisplayElement from a dict
display_element_from_dict = DisplayElement.from_dict(display_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


