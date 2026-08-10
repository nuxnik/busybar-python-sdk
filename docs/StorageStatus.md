# StorageStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used_bytes** | **int** |  | [optional] 
**free_bytes** | **int** |  | [optional] 
**total_bytes** | **int** | Total size of the partition | [optional] 

## Example

```python
from busybar-python-sdk.models.storage_status import StorageStatus

# TODO update the JSON string below
json = "{}"
# create an instance of StorageStatus from a JSON string
storage_status_instance = StorageStatus.from_json(json)
# print the JSON string representation of the object
print StorageStatus.to_json()

# convert the object into a dict
storage_status_dict = storage_status_instance.to_dict()
# create an instance of StorageStatus from a dict
storage_status_from_dict = StorageStatus.from_dict(storage_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


