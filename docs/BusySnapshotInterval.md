# BusySnapshotInterval


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**card_id** | **str** |  | 
**current_interval** | **int** |  | 
**current_interval_time_total_ms** | **int** |  | 
**current_interval_time_left_ms** | **int** |  | 
**is_paused** | **bool** |  | 
**interval_settings** | [**BusyTimerIntervalSettings**](BusyTimerIntervalSettings.md) |  | 

## Example

```python
from busybar-python-sdk.models.busy_snapshot_interval import BusySnapshotInterval

# TODO update the JSON string below
json = "{}"
# create an instance of BusySnapshotInterval from a JSON string
busy_snapshot_interval_instance = BusySnapshotInterval.from_json(json)
# print the JSON string representation of the object
print BusySnapshotInterval.to_json()

# convert the object into a dict
busy_snapshot_interval_dict = busy_snapshot_interval_instance.to_dict()
# create an instance of BusySnapshotInterval from a dict
busy_snapshot_interval_from_dict = BusySnapshotInterval.from_dict(busy_snapshot_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


