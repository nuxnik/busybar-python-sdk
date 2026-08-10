# GetUpdateChangelog200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changelog** | **str** | Changelog text | [optional] 

## Example

```python
from busybar_python_sdk.models.get_update_changelog200_response import GetUpdateChangelog200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUpdateChangelog200Response from a JSON string
get_update_changelog200_response_instance = GetUpdateChangelog200Response.from_json(json)
# print the JSON string representation of the object
print(GetUpdateChangelog200Response.to_json())

# convert the object into a dict
get_update_changelog200_response_dict = get_update_changelog200_response_instance.to_dict()
# create an instance of GetUpdateChangelog200Response from a dict
get_update_changelog200_response_from_dict = GetUpdateChangelog200Response.from_dict(get_update_changelog200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


