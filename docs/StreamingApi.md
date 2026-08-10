# busybar_python_sdk.StreamingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_screen_get**](StreamingApi.md#api_screen_get) | **GET** /api/screen | Get single frame for requested screen
[**connect_web_socket**](StreamingApi.md#connect_web_socket) | **GET** /api/status/ws | Device status streaming WebSocket endpoint


# **api_screen_get**
> str api_screen_get(display)

Get single frame for requested screen



### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar_python_sdk
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with busybar_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = busybar_python_sdk.StreamingApi(api_client)
    display = 0 # int | Type of the display Front = 0, Back = 1

    try:
        # Get single frame for requested screen
        api_response = api_instance.api_screen_get(display)
        print("The response of StreamingApi->api_screen_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingApi->api_screen_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display** | **int**| Type of the display Front &#x3D; 0, Back &#x3D; 1 | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/bmp, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Wrong display |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_web_socket**
> connect_web_socket()

Device status streaming WebSocket endpoint

WebSocket connection for real-time device status and screen streaming.
Upgrade from HTTP to WebSocket protocol is required.
After connection, client must enable streaming by sending JSON: {"enable": true}


### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar_python_sdk
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with busybar_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = busybar_python_sdk.StreamingApi(api_client)

    try:
        # Device status streaming WebSocket endpoint
        api_instance.connect_web_socket()
    except Exception as e:
        print("Exception when calling StreamingApi->connect_web_socket: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**101** | WebSocket connection established |  -  |
**400** | Exceed max clients count |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

