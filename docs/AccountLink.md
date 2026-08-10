# AccountLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**expires_at** | **int** |  | [optional] 

## Example

```python
from busybar_python_sdk.models.account_link import AccountLink

# TODO update the JSON string below
json = "{}"
# create an instance of AccountLink from a JSON string
account_link_instance = AccountLink.from_json(json)
# print the JSON string representation of the object
print AccountLink.to_json()

# convert the object into a dict
account_link_dict = account_link_instance.to_dict()
# create an instance of AccountLink from a dict
account_link_from_dict = AccountLink.from_dict(account_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


