# busybar-python-sdk.TimeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_time**](TimeApi.md#get_time) | **GET** /api/time | Get current timestamp with timezone
[**get_time_timezone**](TimeApi.md#get_time_timezone) | **GET** /api/time/timezone | Get timezone
[**get_time_tzlist**](TimeApi.md#get_time_tzlist) | **GET** /api/time/tzlist | Get list of supported time zones
[**set_time_timestamp**](TimeApi.md#set_time_timestamp) | **POST** /api/time/timestamp | Set current timestamp
[**set_time_timezone**](TimeApi.md#set_time_timezone) | **POST** /api/time/timezone | Set timezone


# **get_time**
> TimestampInfo get_time()

Get current timestamp with timezone

Retrieves the current timestamp from RTC with timezone in ISO 8601 format

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
from busybar-python-sdk.models.timestamp_info import TimestampInfo
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
    api_instance = busybar-python-sdk.TimeApi(api_client)

    try:
        # Get current timestamp with timezone
        api_response = api_instance.get_time()
        print("The response of TimeApi->get_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeApi->get_time: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**TimestampInfo**](TimestampInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Timestamp retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_timezone**
> TimezoneInfo get_time_timezone()

Get timezone

Get current timezone name

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
from busybar-python-sdk.models.timezone_info import TimezoneInfo
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
    api_instance = busybar-python-sdk.TimeApi(api_client)

    try:
        # Get timezone
        api_response = api_instance.get_time_timezone()
        print("The response of TimeApi->get_time_timezone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeApi->get_time_timezone: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**TimezoneInfo**](TimezoneInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Timezone got successfully |  -  |
**400** | Invalid timezone offset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_tzlist**
> TimezoneListResponse get_time_tzlist()

Get list of supported time zones

Retrieves the list of time zones accepted by /api/time/timezone

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
from busybar-python-sdk.models.timezone_list_response import TimezoneListResponse
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
    api_instance = busybar-python-sdk.TimeApi(api_client)

    try:
        # Get list of supported time zones
        api_response = api_instance.get_time_tzlist()
        print("The response of TimeApi->get_time_tzlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeApi->get_time_tzlist: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**TimezoneListResponse**](TimezoneListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Got the list successfully |  -  |
**400** | Error getting time zone list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_time_timestamp**
> SuccessResponse set_time_timestamp(timestamp)

Set current timestamp

Sets the RTC timestamp in ISO 8601 format. Time zone qualifier (e.g. Z of UTC or +hh:mm for local time) is required.


### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
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
    api_instance = busybar-python-sdk.TimeApi(api_client)
    timestamp = '2025-10-02T14:30:45+0100' # datetime | ISO 8601 timestamp (e.g., 2025-10-02T14:30:45+02:00 for local time or 2025-10-02T14:30:45Z for UTC)

    try:
        # Set current timestamp
        api_response = api_instance.set_time_timestamp(timestamp)
        print("The response of TimeApi->set_time_timestamp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeApi->set_time_timestamp: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **datetime**| ISO 8601 timestamp (e.g., 2025-10-02T14:30:45+02:00 for local time or 2025-10-02T14:30:45Z for UTC) | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Timestamp set successfully |  -  |
**400** | Invalid timestamp format or value |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_time_timezone**
> SuccessResponse set_time_timezone(timezone)

Set timezone

Sets the timezone name. Use /api/time/tzlist to get available names list.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
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
    api_instance = busybar-python-sdk.TimeApi(api_client)
    timezone = 'Berlin' # str | Timezone name (use /api/time/tzlist to get available names)

    try:
        # Set timezone
        api_response = api_instance.set_time_timezone(timezone)
        print("The response of TimeApi->set_time_timezone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeApi->set_time_timezone: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timezone** | **str**| Timezone name (use /api/time/tzlist to get available names) | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Timezone set successfully |  -  |
**400** | Invalid timezone offset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

