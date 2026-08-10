# ImageElement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path to the image file in the app&#39;s assets | 
**stock_path** | **str** | Stock image file name | 
**opacity** | **int** | Opacity of the image in percentage (0-100) | [optional] [default to 100]

## Example

```python
from openapi_client.models.image_element import ImageElement

# TODO update the JSON string below
json = "{}"
# create an instance of ImageElement from a JSON string
image_element_instance = ImageElement.from_json(json)
# print the JSON string representation of the object
print ImageElement.to_json()

# convert the object into a dict
image_element_dict = image_element_instance.to_dict()
# create an instance of ImageElement from a dict
image_element_from_dict = ImageElement.from_dict(image_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


