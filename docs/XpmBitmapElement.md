# XpmBitmapElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | XPM2 source as plain text: must begin with a \&quot;! XPM2\&quot; signature line, followed by a \&quot;width height ncolors cpp\&quot; header line, then ncolors color lines, then height pixel rows. Each color line is \&quot;&lt;chars&gt; &lt;visual&gt; &lt;value&gt;\&quot; where visual is c (color), g/g4 (grayscale), m (monochrome), or s (symbolic). Values can be hex (#RGB, #RRGGBB, #RRRGGGBBB, #RRRRGGGGBBBB),  or named (none, black, white, red, green, blue, yellow, cyan, magenta, gray, grey). Limits: ncolors &lt;&#x3D; 32, cpp &lt;&#x3D; 4, and width/height must not exceed the target display dimensions (see the \&quot;display\&quot; field). | 
**opacity** | **int** | Opacity of the image in percentage (0-100) | [optional] [default to 100]

## Example

```python
from busybar_python_sdk.models.xpm_bitmap_element import XpmBitmapElement

# TODO update the JSON string below
json = "{}"
# create an instance of XpmBitmapElement from a JSON string
xpm_bitmap_element_instance = XpmBitmapElement.from_json(json)
# print the JSON string representation of the object
print(XpmBitmapElement.to_json())

# convert the object into a dict
xpm_bitmap_element_dict = xpm_bitmap_element_instance.to_dict()
# create an instance of XpmBitmapElement from a dict
xpm_bitmap_element_from_dict = XpmBitmapElement.from_dict(xpm_bitmap_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


