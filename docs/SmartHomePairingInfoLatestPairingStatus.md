# SmartHomePairingInfoLatestPairingStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Latest state of smart home pairing (Matter \&quot;commissioning\&quot;) process. Note: \&quot;never_started\&quot; only refers to the current power cycle of the device; this status is not recorded across reboots. | [optional] 
**timestamp** | **int** | UTC Unix second timestamp of latest state update. Only present when a status update has occurred. | [optional] 

## Example

```python
from openapi_client.models.smart_home_pairing_info_latest_pairing_status import SmartHomePairingInfoLatestPairingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SmartHomePairingInfoLatestPairingStatus from a JSON string
smart_home_pairing_info_latest_pairing_status_instance = SmartHomePairingInfoLatestPairingStatus.from_json(json)
# print the JSON string representation of the object
print SmartHomePairingInfoLatestPairingStatus.to_json()

# convert the object into a dict
smart_home_pairing_info_latest_pairing_status_dict = smart_home_pairing_info_latest_pairing_status_instance.to_dict()
# create an instance of SmartHomePairingInfoLatestPairingStatus from a dict
smart_home_pairing_info_latest_pairing_status_from_dict = SmartHomePairingInfoLatestPairingStatus.from_dict(smart_home_pairing_info_latest_pairing_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


