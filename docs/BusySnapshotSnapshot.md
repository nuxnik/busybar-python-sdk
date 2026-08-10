# BusySnapshotSnapshot


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**card_id** | **str** |  | 
**is_paused** | **bool** |  | 
**time_left_ms** | **int** |  | 
**current_interval** | **int** |  | 
**current_interval_time_total_ms** | **int** |  | 
**current_interval_time_left_ms** | **int** |  | 
**interval_settings** | [**BusyTimerIntervalSettings**](BusyTimerIntervalSettings.md) |  | 
**busy_bar_settings** | [**BusyBarSettings**](BusyBarSettings.md) |  | 

## Example

```python
from busybar_python_sdk.models.busy_snapshot_snapshot import BusySnapshotSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of BusySnapshotSnapshot from a JSON string
busy_snapshot_snapshot_instance = BusySnapshotSnapshot.from_json(json)
# print the JSON string representation of the object
print BusySnapshotSnapshot.to_json()

# convert the object into a dict
busy_snapshot_snapshot_dict = busy_snapshot_snapshot_instance.to_dict()
# create an instance of BusySnapshotSnapshot from a dict
busy_snapshot_snapshot_from_dict = BusySnapshotSnapshot.from_dict(busy_snapshot_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


