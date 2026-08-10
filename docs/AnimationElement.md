# AnimationElement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path to the animation file in the app&#39;s assets | [optional] 
**stock_path** | **str** | Stock animation file name | [optional] 
**loop** | **bool** | Whether to loop the requested part of the animation | [optional] [default to False]
**await_previous_end** | **bool** | If the element has been created before and this flag is true, the previous range will finish before the requested one starts. | [optional] [default to False]
**section** | **str** | Name of the section to play back. Specifying \&quot;default\&quot; selects the entire animation. | [optional] 
**opacity** | **int** | Opacity of the animated image in percentage (0-100) | [optional] [default to 100]

## Example

```python
from openapi_client.models.animation_element import AnimationElement

# TODO update the JSON string below
json = "{}"
# create an instance of AnimationElement from a JSON string
animation_element_instance = AnimationElement.from_json(json)
# print the JSON string representation of the object
print AnimationElement.to_json()

# convert the object into a dict
animation_element_dict = animation_element_instance.to_dict()
# create an instance of AnimationElement from a dict
animation_element_from_dict = AnimationElement.from_dict(animation_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


