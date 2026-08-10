# UpdateStatusInstallDownload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**speed_bytes_per_sec** | **int** | Current download speed in bytes per second | [optional] 
**received_bytes** | **int** | Bytes received so far | [optional] 
**total_bytes** | **int** | Total download size in bytes | [optional] 

## Example

```python
from busybar-python-sdk.models.update_status_install_download import UpdateStatusInstallDownload

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStatusInstallDownload from a JSON string
update_status_install_download_instance = UpdateStatusInstallDownload.from_json(json)
# print the JSON string representation of the object
print UpdateStatusInstallDownload.to_json()

# convert the object into a dict
update_status_install_download_dict = update_status_install_download_instance.to_dict()
# create an instance of UpdateStatusInstallDownload from a dict
update_status_install_download_from_dict = UpdateStatusInstallDownload.from_dict(update_status_install_download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


