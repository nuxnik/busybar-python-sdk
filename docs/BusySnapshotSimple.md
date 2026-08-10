# BusySnapshotSimple


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**card_id** | **str** |  | 
**time_left_ms** | **int** |  | 
**is_paused** | **bool** |  | 

## Example

```python
from busybar-python-sdk.models.busy_snapshot_simple import BusySnapshotSimple

# TODO update the JSON string below
json = "{}"
# create an instance of BusySnapshotSimple from a JSON string
busy_snapshot_simple_instance = BusySnapshotSimple.from_json(json)
# print the JSON string representation of the object
print BusySnapshotSimple.to_json()

# convert the object into a dict
busy_snapshot_simple_dict = busy_snapshot_simple_instance.to_dict()
# create an instance of BusySnapshotSimple from a dict
busy_snapshot_simple_from_dict = BusySnapshotSimple.from_dict(busy_snapshot_simple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


