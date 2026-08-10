# AccountInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linked** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from busybar_python_sdk.models.account_info import AccountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfo from a JSON string
account_info_instance = AccountInfo.from_json(json)
# print the JSON string representation of the object
print AccountInfo.to_json()

# convert the object into a dict
account_info_dict = account_info_instance.to_dict()
# create an instance of AccountInfo from a dict
account_info_from_dict = AccountInfo.from_dict(account_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


