# PlayAudio


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_name** | **str** | Application ID for organizing assets | 
**path** | **str** | Path to audio file within app&#39;s assets directory | 
**stock_path** | **str** | Stock audio file name | 

## Example

```python
from busybar-python-sdk.models.play_audio import PlayAudio

# TODO update the JSON string below
json = "{}"
# create an instance of PlayAudio from a JSON string
play_audio_instance = PlayAudio.from_json(json)
# print the JSON string representation of the object
print PlayAudio.to_json()

# convert the object into a dict
play_audio_dict = play_audio_instance.to_dict()
# create an instance of PlayAudio from a dict
play_audio_from_dict = PlayAudio.from_dict(play_audio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


