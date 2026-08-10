# StorageListElement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Element type | 
**name** | **str** | File or directory name | 

## Example

```python
from busybar-python-sdk.models.storage_list_element import StorageListElement

# TODO update the JSON string below
json = "{}"
# create an instance of StorageListElement from a JSON string
storage_list_element_instance = StorageListElement.from_json(json)
# print the JSON string representation of the object
print StorageListElement.to_json()

# convert the object into a dict
storage_list_element_dict = storage_list_element_instance.to_dict()
# create an instance of StorageListElement from a dict
storage_list_element_from_dict = StorageListElement.from_dict(storage_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


