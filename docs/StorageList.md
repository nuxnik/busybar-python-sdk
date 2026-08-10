# StorageList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[StorageListElement]**](StorageListElement.md) | Array of elements to display | 

## Example

```python
from busybar-python-sdk.models.storage_list import StorageList

# TODO update the JSON string below
json = "{}"
# create an instance of StorageList from a JSON string
storage_list_instance = StorageList.from_json(json)
# print the JSON string representation of the object
print StorageList.to_json()

# convert the object into a dict
storage_list_dict = storage_list_instance.to_dict()
# create an instance of StorageList from a dict
storage_list_from_dict = StorageList.from_dict(storage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


