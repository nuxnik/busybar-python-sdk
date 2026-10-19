# busybar_python_sdk.SmartHomeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_smart_home_pairing_delete**](SmartHomeApi.md#api_smart_home_pairing_delete) | **DELETE** /api/smart_home/pairing | Erase all smart home links
[**api_smart_home_switch_get**](SmartHomeApi.md#api_smart_home_switch_get) | **GET** /api/smart_home/switch | Get state of emulated smart home switch
[**api_smart_home_switch_post**](SmartHomeApi.md#api_smart_home_switch_post) | **POST** /api/smart_home/switch | Set state of emulated smart home switch
[**get_smart_home_commissioning_status**](SmartHomeApi.md#get_smart_home_commissioning_status) | **GET** /api/smart_home/pairing | Smart home commissioning status
[**start_smart_home_pairing**](SmartHomeApi.md#start_smart_home_pairing) | **POST** /api/smart_home/pairing | Link device to a smart home


# **api_smart_home_pairing_delete**
> SuccessResponse api_smart_home_pairing_delete()

Erase all smart home links

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
    api_instance = busybar_python_sdk.SmartHomeApi(api_client)

    try:
        # Erase all smart home links
        api_response = api_instance.api_smart_home_pairing_delete()
        print("The response of SmartHomeApi->api_smart_home_pairing_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartHomeApi->api_smart_home_pairing_delete: %s\n" % e)
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
**200** | Successfully erased all smart home pairing info, device restart is needed |  -  |
**503** | Internal smart home service is broken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_smart_home_switch_get**
> SmartHomeSwitchState api_smart_home_switch_get()

Get state of emulated smart home switch

### Example

* Bearer Authentication (barApiToken):

```python
import busybar_python_sdk
from busybar_python_sdk.models.smart_home_switch_state import SmartHomeSwitchState
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
    api_instance = busybar_python_sdk.SmartHomeApi(api_client)

    try:
        # Get state of emulated smart home switch
        api_response = api_instance.api_smart_home_switch_get()
        print("The response of SmartHomeApi->api_smart_home_switch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartHomeApi->api_smart_home_switch_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SmartHomeSwitchState**](SmartHomeSwitchState.md)

### Authorization

[barApiToken](../README.md#barApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully got state of emulated smart home switch |  -  |
**503** | Internal smart home service is broken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_smart_home_switch_post**
> SuccessResponse api_smart_home_switch_post(smart_home_switch_state)

Set state of emulated smart home switch

### Example

* Bearer Authentication (barApiToken):

```python
import busybar_python_sdk
from busybar_python_sdk.models.smart_home_switch_state import SmartHomeSwitchState
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
    api_instance = busybar_python_sdk.SmartHomeApi(api_client)
    smart_home_switch_state = busybar_python_sdk.SmartHomeSwitchState() # SmartHomeSwitchState | 

    try:
        # Set state of emulated smart home switch
        api_response = api_instance.api_smart_home_switch_post(smart_home_switch_state)
        print("The response of SmartHomeApi->api_smart_home_switch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartHomeApi->api_smart_home_switch_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_home_switch_state** | [**SmartHomeSwitchState**](SmartHomeSwitchState.md)|  | 

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
**200** | Successfully set state of emulated smart home switch |  -  |
**503** | Internal smart home service is broken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smart_home_commissioning_status**
> SmartHomePairingInfo get_smart_home_commissioning_status()

Smart home commissioning status

### Example

* Bearer Authentication (barApiToken):

```python
import busybar_python_sdk
from busybar_python_sdk.models.smart_home_pairing_info import SmartHomePairingInfo
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
    api_instance = busybar_python_sdk.SmartHomeApi(api_client)

    try:
        # Smart home commissioning status
        api_response = api_instance.get_smart_home_commissioning_status()
        print("The response of SmartHomeApi->get_smart_home_commissioning_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartHomeApi->get_smart_home_commissioning_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SmartHomePairingInfo**](SmartHomePairingInfo.md)

### Authorization

[barApiToken](../README.md#barApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully got smart home commissioning status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_smart_home_pairing**
> SmartHomePairingPayload start_smart_home_pairing()

Link device to a smart home

### Example

* Bearer Authentication (barApiToken):

```python
import busybar_python_sdk
from busybar_python_sdk.models.smart_home_pairing_payload import SmartHomePairingPayload
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
    api_instance = busybar_python_sdk.SmartHomeApi(api_client)

    try:
        # Link device to a smart home
        api_response = api_instance.start_smart_home_pairing()
        print("The response of SmartHomeApi->start_smart_home_pairing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartHomeApi->start_smart_home_pairing: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SmartHomePairingPayload**](SmartHomePairingPayload.md)

### Authorization

[barApiToken](../README.md#barApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully started smart home pairing |  -  |
**503** | Internal smart home service is broken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

