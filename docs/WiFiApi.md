# busybar_python_sdk.WiFiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_wifi_connect_post**](WiFiApi.md#api_wifi_connect_post) | **POST** /api/wifi/connect | 
[**api_wifi_disconnect_post**](WiFiApi.md#api_wifi_disconnect_post) | **POST** /api/wifi/disconnect | 
[**api_wifi_status_get**](WiFiApi.md#api_wifi_status_get) | **GET** /api/wifi/status | 
[**get_wifi_networks**](WiFiApi.md#get_wifi_networks) | **GET** /api/wifi/networks | 


# **api_wifi_connect_post**
> SuccessResponse api_wifi_connect_post(connect_request_config)

Attempts to connect to Wi-Fi using config

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.connect_request_config import ConnectRequestConfig
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with busybar_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = busybar_python_sdk.WiFiApi(api_client)
    connect_request_config = busybar_python_sdk.ConnectRequestConfig() # ConnectRequestConfig | 

    try:
        api_response = api_instance.api_wifi_connect_post(connect_request_config)
        print("The response of WiFiApi->api_wifi_connect_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WiFiApi->api_wifi_connect_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connect_request_config** | [**ConnectRequestConfig**](ConnectRequestConfig.md)|  | 

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
**200** | Network connection established |  -  |
**400** | Already connected |  -  |
**503** | Wi-Fi operation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_wifi_disconnect_post**
> SuccessResponse api_wifi_disconnect_post()

Disconnects from Wi-Fi

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with busybar_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = busybar_python_sdk.WiFiApi(api_client)

    try:
        api_response = api_instance.api_wifi_disconnect_post()
        print("The response of WiFiApi->api_wifi_disconnect_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WiFiApi->api_wifi_disconnect_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Network connection terminated |  -  |
**400** | Already disconnected |  -  |
**503** | Wi-Fi operation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_wifi_status_get**
> StatusResponse api_wifi_status_get()

Returns current Wi-Fi status

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.status_response import StatusResponse
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
    api_instance = busybar_python_sdk.WiFiApi(api_client)

    try:
        api_response = api_instance.api_wifi_status_get()
        print("The response of WiFiApi->api_wifi_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WiFiApi->api_wifi_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**503** | Wi-Fi operation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wifi_networks**
> NetworkResponse get_wifi_networks()

Scans environment for available Wi-Fi networks

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.network_response import NetworkResponse
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
    api_instance = busybar_python_sdk.WiFiApi(api_client)

    try:
        api_response = api_instance.get_wifi_networks()
        print("The response of WiFiApi->get_wifi_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WiFiApi->get_wifi_networks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NetworkResponse**](NetworkResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Scan not possible when connected |  -  |
**503** | Wi-Fi operation failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

