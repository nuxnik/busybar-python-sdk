# busybar_python_sdk.BusyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_busy_profile**](BusyApi.md#get_busy_profile) | **GET** /busybar/busy/profiles/{slot} | Get BUSY timer profile
[**get_busy_snapshot**](BusyApi.md#get_busy_snapshot) | **GET** /busybar/busy/snapshot | Get BUSY timer snapshot
[**set_busy_profile**](BusyApi.md#set_busy_profile) | **PUT** /busybar/busy/profiles/{slot} | Set BUSY timer profile
[**set_busy_snapshot**](BusyApi.md#set_busy_snapshot) | **PUT** /busybar/busy/snapshot | Set BUSY timer snapshot


# **get_busy_profile**
> BusyProfile get_busy_profile(slot)

Get BUSY timer profile

Gets the BUSY timer profile under specified slot

### Example

* Bearer Authentication (barApiToken):

```python
import busybar_python_sdk
from busybar_python_sdk.models.busy_profile import BusyProfile
from busybar_python_sdk.models.busy_profile_slot import BusyProfileSlot
from busybar_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = busybar_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: barApiToken
configuration = busybar_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with busybar_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = busybar_python_sdk.BusyApi(api_client)
    slot = busybar_python_sdk.BusyProfileSlot() # BusyProfileSlot | 

    try:
        # Get BUSY timer profile
        api_response = api_instance.get_busy_profile(slot)
        print("The response of BusyApi->get_busy_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusyApi->get_busy_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slot** | [**BusyProfileSlot**](.md)|  | 

### Return type

[**BusyProfile**](BusyProfile.md)

### Authorization

[barApiToken](../README.md#barApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Got profile successfully |  -  |
**400** | Error getting profile |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_busy_snapshot**
> BusySnapshot get_busy_snapshot()

Get BUSY timer snapshot

Gets the current state of the BUSY timer in snapshot form

### Example

* Bearer Authentication (barApiToken):

```python
import busybar_python_sdk
from busybar_python_sdk.models.busy_snapshot import BusySnapshot
from busybar_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = busybar_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: barApiToken
configuration = busybar_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with busybar_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = busybar_python_sdk.BusyApi(api_client)

    try:
        # Get BUSY timer snapshot
        api_response = api_instance.get_busy_snapshot()
        print("The response of BusyApi->get_busy_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusyApi->get_busy_snapshot: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BusySnapshot**](BusySnapshot.md)

### Authorization

[barApiToken](../README.md#barApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Got snapshot successfully |  -  |
**400** | Error getting snapshot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_busy_profile**
> SuccessResponse set_busy_profile(slot, busy_profile)

Set BUSY timer profile

Sets the BUSY timer profile under specified slot

### Example

* Bearer Authentication (barApiToken):

```python
import busybar_python_sdk
from busybar_python_sdk.models.busy_profile import BusyProfile
from busybar_python_sdk.models.busy_profile_slot import BusyProfileSlot
from busybar_python_sdk.models.success_response import SuccessResponse
from busybar_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = busybar_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: barApiToken
configuration = busybar_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with busybar_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = busybar_python_sdk.BusyApi(api_client)
    slot = busybar_python_sdk.BusyProfileSlot() # BusyProfileSlot | 
    busy_profile = busybar_python_sdk.BusyProfile() # BusyProfile | 

    try:
        # Set BUSY timer profile
        api_response = api_instance.set_busy_profile(slot, busy_profile)
        print("The response of BusyApi->set_busy_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusyApi->set_busy_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slot** | [**BusyProfileSlot**](.md)|  | 
 **busy_profile** | [**BusyProfile**](BusyProfile.md)|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[barApiToken](../README.md#barApiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Profile successfully set |  -  |
**400** | Error setting profile |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_busy_snapshot**
> SuccessResponse set_busy_snapshot(busy_snapshot)

Set BUSY timer snapshot

Run the timer starting from the given snapshot

### Example

* Bearer Authentication (barApiToken):

```python
import busybar_python_sdk
from busybar_python_sdk.models.busy_snapshot import BusySnapshot
from busybar_python_sdk.models.success_response import SuccessResponse
from busybar_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = busybar_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: barApiToken
configuration = busybar_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with busybar_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = busybar_python_sdk.BusyApi(api_client)
    busy_snapshot = busybar_python_sdk.BusySnapshot() # BusySnapshot | 

    try:
        # Set BUSY timer snapshot
        api_response = api_instance.set_busy_snapshot(busy_snapshot)
        print("The response of BusyApi->set_busy_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusyApi->set_busy_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **busy_snapshot** | [**BusySnapshot**](BusySnapshot.md)|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[barApiToken](../README.md#barApiToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Snapshot successfully set |  -  |
**400** | Error setting snapshot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

