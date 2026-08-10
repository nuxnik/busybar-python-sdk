# RectangleElement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **int** | Width of the rectangle in pixels | 
**height** | **int** | Height of the rectangle in pixels | 
**radius** | **int** | Corner radius of the rectangle in pixels (0 for sharp corners) | [optional] 
**fill** | **str** | Fill style of the rectangle | [optional] [default to 'none']
**fill_colors** | **List[str]** | Colors used for filling the rectangle. For solid fill, provide one color. For gradient fill, provide two colors. | [optional] [default to [#FFFFFFFF, #00000000]]
**border_width** | **int** | Width of the rectangle border in pixels (0 for no border) | [optional] [default to 1]
**border_color** | **str** | Color of the rectangle border in #RRGGBBAA format | [optional] [default to '#FFFFFFFF']

## Example

```python
from busybar-python-sdk.models.rectangle_element import RectangleElement

# TODO update the JSON string below
json = "{}"
# create an instance of RectangleElement from a JSON string
rectangle_element_instance = RectangleElement.from_json(json)
# print the JSON string representation of the object
print RectangleElement.to_json()

# convert the object into a dict
rectangle_element_dict = rectangle_element_instance.to_dict()
# create an instance of RectangleElement from a dict
rectangle_element_from_dict = RectangleElement.from_dict(rectangle_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


