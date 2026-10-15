# DisplayElements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | Application name for organizing assets | 
**priority** | **int** | Draw priority in the range [1, 100] inclusive. A draw request is accepted when its priority is greater than or equal to (&gt;&#x3D;) the priority of the currently running system app. Equal-priority requests from a different application_name override whatever is on screen. System app priority levels: stub/poweroff apps &#x3D; 0 (always preemptable), any standard built-in app &#x3D; 10, active BUSY/CUSTOM work session &#x3D; 90. The draw API only accepts values 1–100; 0 is reserved for internal use. | [optional] [default to 50]
**led_notification_color** | **str** | Color to blink the status LED, in #RRGGBBAA format. If not specified, the LED will not blink. | [optional] 
**elements** | [**List[DisplayElementsElementsInner]**](DisplayElementsElementsInner.md) | Array of elements to display | 

## Example

```python
from busybar_python_sdk.models.display_elements import DisplayElements

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayElements from a JSON string
display_elements_instance = DisplayElements.from_json(json)
# print the JSON string representation of the object
print(DisplayElements.to_json())

# convert the object into a dict
display_elements_dict = display_elements_instance.to_dict()
# create an instance of DisplayElements from a dict
display_elements_from_dict = DisplayElements.from_dict(display_elements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


