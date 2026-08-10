# AudioVolumeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume** | **float** | Audio volume value (0-100) | [optional] 

## Example

```python
from busybar_python_sdk.models.audio_volume_info import AudioVolumeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AudioVolumeInfo from a JSON string
audio_volume_info_instance = AudioVolumeInfo.from_json(json)
# print the JSON string representation of the object
print(AudioVolumeInfo.to_json())

# convert the object into a dict
audio_volume_info_dict = audio_volume_info_instance.to_dict()
# create an instance of AudioVolumeInfo from a dict
audio_volume_info_from_dict = AudioVolumeInfo.from_dict(audio_volume_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


