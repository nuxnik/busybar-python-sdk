# StatusPower


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Power state | 
**battery_charge** | **int** | Battery charge percent | 
**battery_voltage** | **int** | Battery voltage in mV | 
**battery_current** | **int** | Battery current in mA | 
**usb_voltage** | **int** | USB voltage in mV | 

## Example

```python
from busybar_python_sdk.models.status_power import StatusPower

# TODO update the JSON string below
json = "{}"
# create an instance of StatusPower from a JSON string
status_power_instance = StatusPower.from_json(json)
# print the JSON string representation of the object
print StatusPower.to_json()

# convert the object into a dict
status_power_dict = status_power_instance.to_dict()
# create an instance of StatusPower from a dict
status_power_from_dict = StatusPower.from_dict(status_power_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


