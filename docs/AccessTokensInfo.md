# AccessTokensInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tokens** | [**List[AccessToken]**](AccessToken.md) |  | [optional] 

## Example

```python
from busybar_python_sdk.models.access_tokens_info import AccessTokensInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokensInfo from a JSON string
access_tokens_info_instance = AccessTokensInfo.from_json(json)
# print the JSON string representation of the object
print(AccessTokensInfo.to_json())

# convert the object into a dict
access_tokens_info_dict = access_tokens_info_instance.to_dict()
# create an instance of AccessTokensInfo from a dict
access_tokens_info_from_dict = AccessTokensInfo.from_dict(access_tokens_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


