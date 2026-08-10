# SmartHomePairingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fabric_count** | **int** | Number of smart homes (Matter \&quot;fabrics\&quot;) that this device is paired with (\&quot;commissioned into\&quot;) | [optional] 
**latest_pairing_status** | [**SmartHomePairingInfoLatestPairingStatus**](SmartHomePairingInfoLatestPairingStatus.md) |  | [optional] 

## Example

```python
from busybar_python_sdk.models.smart_home_pairing_info import SmartHomePairingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SmartHomePairingInfo from a JSON string
smart_home_pairing_info_instance = SmartHomePairingInfo.from_json(json)
# print the JSON string representation of the object
print(SmartHomePairingInfo.to_json())

# convert the object into a dict
smart_home_pairing_info_dict = smart_home_pairing_info_instance.to_dict()
# create an instance of SmartHomePairingInfo from a dict
smart_home_pairing_info_from_dict = SmartHomePairingInfo.from_dict(smart_home_pairing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


