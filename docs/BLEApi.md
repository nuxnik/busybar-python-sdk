# busybar_python_sdk.BLEApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**busybar_ble_disable_post**](BLEApi.md#busybar_ble_disable_post) | **POST** /busybar/ble/disable | Disable BLE
[**busybar_ble_enable_post**](BLEApi.md#busybar_ble_enable_post) | **POST** /busybar/ble/enable | Enable BLE
[**busybar_ble_pairing_delete**](BLEApi.md#busybar_ble_pairing_delete) | **DELETE** /busybar/ble/pairing | Remove pairing
[**busybar_ble_status_get**](BLEApi.md#busybar_ble_status_get) | **GET** /busybar/ble/status | 


# **busybar_ble_disable_post**
> SuccessResponse busybar_ble_disable_post()

Disable BLE

Stops advertising

### Example

* Bearer Authentication (barApiToken):

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

# Configure Bearer authorization: barApiToken
configuration = busybar_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with busybar_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = busybar_python_sdk.BLEApi(api_client)

    try:
        # Disable BLE
        api_response = api_instance.busybar_ble_disable_post()
        print("The response of BLEApi->busybar_ble_disable_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BLEApi->busybar_ble_disable_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[barApiToken](../README.md#barApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BLE disabled |  -  |
**503** | Unable to stop BLE |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **busybar_ble_enable_post**
> SuccessResponse busybar_ble_enable_post()

Enable BLE

Enables BLE module and starts advertising

### Example

* Bearer Authentication (barApiToken):

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

# Configure Bearer authorization: barApiToken
configuration = busybar_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with busybar_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = busybar_python_sdk.BLEApi(api_client)

    try:
        # Enable BLE
        api_response = api_instance.busybar_ble_enable_post()
        print("The response of BLEApi->busybar_ble_enable_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BLEApi->busybar_ble_enable_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[barApiToken](../README.md#barApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BLE enabled |  -  |
**503** | Unable to start BLE |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **busybar_ble_pairing_delete**
> SuccessResponse busybar_ble_pairing_delete()

Remove pairing

Remove pairing with previous device

### Example

* Bearer Authentication (barApiToken):

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

# Configure Bearer authorization: barApiToken
configuration = busybar_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with busybar_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = busybar_python_sdk.BLEApi(api_client)

    try:
        # Remove pairing
        api_response = api_instance.busybar_ble_pairing_delete()
        print("The response of BLEApi->busybar_ble_pairing_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BLEApi->busybar_ble_pairing_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[barApiToken](../README.md#barApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pairing removed, now device is discoverable |  -  |
**503** | Failed to remove because BLE is not initialized or pairing was already removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **busybar_ble_status_get**
> BleStatusResponse busybar_ble_status_get()

Returns current BLE status

### Example

* Bearer Authentication (barApiToken):

```python
import busybar_python_sdk
from busybar_python_sdk.models.ble_status_response import BleStatusResponse
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
    api_instance = busybar_python_sdk.BLEApi(api_client)

    try:
        api_response = api_instance.busybar_ble_status_get()
        print("The response of BLEApi->busybar_ble_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BLEApi->busybar_ble_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BleStatusResponse**](BleStatusResponse.md)

### Authorization

[barApiToken](../README.md#barApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**503** | Failed to get BLE status, because of an error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

