# UpdateStatusCheck


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_version** | **str** | Version of available update (empty if none) | [optional] 
**event** | **str** | Current check event | [optional] 
**status** | **str** | Check result status | [optional] 

## Example

```python
from openapi_client.models.update_status_check import UpdateStatusCheck

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStatusCheck from a JSON string
update_status_check_instance = UpdateStatusCheck.from_json(json)
# print the JSON string representation of the object
print UpdateStatusCheck.to_json()

# convert the object into a dict
update_status_check_dict = update_status_check_instance.to_dict()
# create an instance of UpdateStatusCheck from a dict
update_status_check_from_dict = UpdateStatusCheck.from_dict(update_status_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


