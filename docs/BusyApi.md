# busybar-python-sdk.BusyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_busy_profile**](BusyApi.md#get_busy_profile) | **GET** /api/busy/profiles/{slot} | Get BUSY timer profile
[**get_busy_snapshot**](BusyApi.md#get_busy_snapshot) | **GET** /api/busy/snapshot | Get BUSY timer snapshot
[**set_busy_profile**](BusyApi.md#set_busy_profile) | **PUT** /api/busy/profiles/{slot} | Set BUSY timer profile
[**set_busy_snapshot**](BusyApi.md#set_busy_snapshot) | **PUT** /api/busy/snapshot | Set BUSY timer snapshot


# **get_busy_profile**
> BusyProfile get_busy_profile(slot)

Get BUSY timer profile

Gets the BUSY timer profile under specified slot

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
from busybar-python-sdk.models.busy_profile import BusyProfile
from busybar-python-sdk.models.busy_profile_slot import BusyProfileSlot
from busybar-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = busybar-python-sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with busybar-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = busybar-python-sdk.BusyApi(api_client)
    slot = busybar-python-sdk.BusyProfileSlot() # BusyProfileSlot | 

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

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
from busybar-python-sdk.models.busy_snapshot import BusySnapshot
from busybar-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = busybar-python-sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with busybar-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = busybar-python-sdk.BusyApi(api_client)

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

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
from busybar-python-sdk.models.busy_profile import BusyProfile
from busybar-python-sdk.models.busy_profile_slot import BusyProfileSlot
from busybar-python-sdk.models.success_response import SuccessResponse
from busybar-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = busybar-python-sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with busybar-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = busybar-python-sdk.BusyApi(api_client)
    slot = busybar-python-sdk.BusyProfileSlot() # BusyProfileSlot | 
    busy_profile = busybar-python-sdk.BusyProfile() # BusyProfile | 

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

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
from busybar-python-sdk.models.busy_snapshot import BusySnapshot
from busybar-python-sdk.models.success_response import SuccessResponse
from busybar-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = busybar-python-sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with busybar-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = busybar-python-sdk.BusyApi(api_client)
    busy_snapshot = busybar-python-sdk.BusySnapshot() # BusySnapshot | 

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

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Snapshot successfully set |  -  |
**400** | Error setting snapshot |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

