# AccountBackend


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_url** | **str** | MQTT server url to connect to | 
**client_cert_type** | **str** | Client certificate type to use | 
**ignore_server_cert** | **bool** | Whether to ignore the server certificate | 

## Example

```python
from busybar-python-sdk.models.account_backend import AccountBackend

# TODO update the JSON string below
json = "{}"
# create an instance of AccountBackend from a JSON string
account_backend_instance = AccountBackend.from_json(json)
# print the JSON string representation of the object
print AccountBackend.to_json()

# convert the object into a dict
account_backend_dict = account_backend_instance.to_dict()
# create an instance of AccountBackend from a dict
account_backend_from_dict = AccountBackend.from_dict(account_backend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


