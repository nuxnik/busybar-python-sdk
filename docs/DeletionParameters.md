# DeletionParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | Fill in this field for a sanity check that you actually own these elements. Omit it to delete them anyway. | [optional] 
**element_ids** | **List[str]** | Unique identifiers of elements that should be deleted. Omit this field to delete all elements. | [optional] 

## Example

```python
from busybar_python_sdk.models.deletion_parameters import DeletionParameters

# TODO update the JSON string below
json = "{}"
# create an instance of DeletionParameters from a JSON string
deletion_parameters_instance = DeletionParameters.from_json(json)
# print the JSON string representation of the object
print(DeletionParameters.to_json())

# convert the object into a dict
deletion_parameters_dict = deletion_parameters_instance.to_dict()
# create an instance of DeletionParameters from a dict
deletion_parameters_from_dict = DeletionParameters.from_dict(deletion_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


