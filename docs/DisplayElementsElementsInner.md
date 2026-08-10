# DisplayElementsElementsInner


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
**text** | **str** | Text content to display (printable ASCII only; fonts are bitmap ASCII) | 
**font** | **str** | One of the available fonts to display the text in | 
**color** | **str** | Color to display the text in, in #RRGGBBAA format | [optional] [default to '#FFFFFFFF']
**width** | **int** | Width of the rectangle in pixels | 
**scroll_rate** | **int** | Scroll rate in pixels per minute | [optional] 
**scroll_start_delay** | **int** | Delay in milliseconds before the scroll animation begins | [optional] 
**scroll_repeat_delay** | **int** | Pause duration in milliseconds between successive scroll cycles | [optional] 
**path** | **str** | Path to the animation file in the app&#39;s assets | 
**stock_path** | **str** | Stock animation file name | 
**opacity** | **int** | Opacity of the animated image in percentage (0-100) | [optional] [default to 100]
**loop** | **bool** | Whether to loop the requested part of the animation | [optional] [default to False]
**await_previous_end** | **bool** | If the element has been created before and this flag is true, the previous range will finish before the requested one starts. | [optional] [default to False]
**section** | **str** | Name of the section to play back. Specifying \&quot;default\&quot; selects the entire animation. | [optional] 
**timestamp** | **str** | Seconds-based Unix UTC timestamp to count down or up to. Note: it&#39;s a number in a string. | 
**direction** | **str** | Whether to count up or down | 
**show_hours** | **str** | When to show the hours position | 
**height** | **int** | Height of the rectangle in pixels | 
**radius** | **int** | Corner radius of the rectangle in pixels (0 for sharp corners) | [optional] 
**fill** | **str** | Fill style of the rectangle | [optional] [default to 'none']
**fill_colors** | **List[str]** | Colors used for filling the rectangle. For solid fill, provide one color. For gradient fill, provide two colors. | [optional] [default to [#FFFFFFFF, #00000000]]
**border_width** | **int** | Width of the rectangle border in pixels (0 for no border) | [optional] [default to 1]
**border_color** | **str** | Color of the rectangle border in #RRGGBBAA format | [optional] [default to '#FFFFFFFF']

## Example

```python
from openapi_client.models.display_elements_elements_inner import DisplayElementsElementsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayElementsElementsInner from a JSON string
display_elements_elements_inner_instance = DisplayElementsElementsInner.from_json(json)
# print the JSON string representation of the object
print DisplayElementsElementsInner.to_json()

# convert the object into a dict
display_elements_elements_inner_dict = display_elements_elements_inner_instance.to_dict()
# create an instance of DisplayElementsElementsInner from a dict
display_elements_elements_inner_from_dict = DisplayElementsElementsInner.from_dict(display_elements_elements_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


