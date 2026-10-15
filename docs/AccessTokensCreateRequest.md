# AccessTokensCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Arbitrary name to differentiate this token from others | 

## Example

```python
from busybar_python_sdk.models.access_tokens_create_request import AccessTokensCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessTokensCreateRequest from a JSON string
access_tokens_create_request_instance = AccessTokensCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AccessTokensCreateRequest.to_json())

# convert the object into a dict
access_tokens_create_request_dict = access_tokens_create_request_instance.to_dict()
# create an instance of AccessTokensCreateRequest from a dict
access_tokens_create_request_from_dict = AccessTokensCreateRequest.from_dict(access_tokens_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


