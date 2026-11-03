# AppSettingsDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | Settings version of the application schema | 
**values** | **Dict[str, object]** | Setting values keyed by field id, with groups as nested objects | 

## Example

```python
from busybar_python_sdk.models.app_settings_document import AppSettingsDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AppSettingsDocument from a JSON string
app_settings_document_instance = AppSettingsDocument.from_json(json)
# print the JSON string representation of the object
print(AppSettingsDocument.to_json())

# convert the object into a dict
app_settings_document_dict = app_settings_document_instance.to_dict()
# create an instance of AppSettingsDocument from a dict
app_settings_document_from_dict = AppSettingsDocument.from_dict(app_settings_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


