# BusySnapshot


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot** | [**BusySnapshotSnapshot**](BusySnapshotSnapshot.md) |  | 
**snapshot_timestamp_ms** | **int** |  | 

## Example

```python
from openapi_client.models.busy_snapshot import BusySnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of BusySnapshot from a JSON string
busy_snapshot_instance = BusySnapshot.from_json(json)
# print the JSON string representation of the object
print BusySnapshot.to_json()

# convert the object into a dict
busy_snapshot_dict = busy_snapshot_instance.to_dict()
# create an instance of BusySnapshot from a dict
busy_snapshot_from_dict = BusySnapshot.from_dict(busy_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


