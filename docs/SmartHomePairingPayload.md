# SmartHomePairingPayload

Set of information for pairing with a Matter smart home

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_until** | **str** | Pairing with (\&quot;commissioning into\&quot;) a Matter smart home using the provided payload is possible before this UTC Unix millisecond timestamp. Note: it&#39;s a number in a string. | [optional] 
**qr_code** | **str** | Payload of the QR code for pairing with (\&quot;commissioning into\&quot;) a smart home | [optional] 
**manual_code** | **str** | Manual code for pairing with (\&quot;commissioning into\&quot;) a smart home | [optional] 

## Example

```python
from openapi_client.models.smart_home_pairing_payload import SmartHomePairingPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SmartHomePairingPayload from a JSON string
smart_home_pairing_payload_instance = SmartHomePairingPayload.from_json(json)
# print the JSON string representation of the object
print SmartHomePairingPayload.to_json()

# convert the object into a dict
smart_home_pairing_payload_dict = smart_home_pairing_payload_instance.to_dict()
# create an instance of SmartHomePairingPayload from a dict
smart_home_pairing_payload_from_dict = SmartHomePairingPayload.from_dict(smart_home_pairing_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


