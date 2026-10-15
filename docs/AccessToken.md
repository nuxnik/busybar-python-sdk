# AccessToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_id** | **str** | Short ID of the access token. Matches the first 8 characters of the token. | [optional] 
**display_id** | **str** | Long (\&quot;display\&quot;) ID of the access token. Matches the first 8 characters and last 6 characters of the token. | [optional] 
**name** | **str** | User-assigned name of the token | [optional] 
**created_at** | **str** | Unix millisecond timestamp of when the token was created. Note: it&#39;s a number in a string. | [optional] 
**last_used_at** | **str** | Unix millisecond timestamp of when the token was used to make any request. Note: it&#39;s a number in a string. | [optional] 
**token** | **str** | Full access token. Can be used in place of the access key in \&quot;X-API-Token\&quot; header. Only shown once when generated, never again. | [optional] 

## Example

```python
from busybar_python_sdk.models.access_token import AccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of AccessToken from a JSON string
access_token_instance = AccessToken.from_json(json)
# print the JSON string representation of the object
print(AccessToken.to_json())

# convert the object into a dict
access_token_dict = access_token_instance.to_dict()
# create an instance of AccessToken from a dict
access_token_from_dict = AccessToken.from_dict(access_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


