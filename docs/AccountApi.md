# busybar_python_sdk.AccountApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_backend**](AccountApi.md#get_account_backend) | **GET** /api/account/backend | Get MQTT configuration
[**get_account_info**](AccountApi.md#get_account_info) | **GET** /api/account/info | Get linked account info
[**get_account_status**](AccountApi.md#get_account_status) | **GET** /api/account/status | Get MQTT status info


# **get_account_backend**
> AccountBackend get_account_backend()

Get MQTT configuration

Retrieves MQTT backend configuration

### Example

* Bearer Authentication (barApiToken):

```python
import busybar_python_sdk
from busybar_python_sdk.models.account_backend import AccountBackend
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
    api_instance = busybar_python_sdk.AccountApi(api_client)

    try:
        # Get MQTT configuration
        api_response = api_instance.get_account_backend()
        print("The response of AccountApi->get_account_backend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account_backend: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountBackend**](AccountBackend.md)

### Authorization

[barApiToken](../README.md#barApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved successfully |  -  |
**503** | Failed to serialize MQTT configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_info**
> AccountInfo get_account_info()

Get linked account info

Retrieves linked account data

### Example

* Bearer Authentication (barApiToken):

```python
import busybar_python_sdk
from busybar_python_sdk.models.account_info import AccountInfo
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
    api_instance = busybar_python_sdk.AccountApi(api_client)

    try:
        # Get linked account info
        api_response = api_instance.get_account_info()
        print("The response of AccountApi->get_account_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountInfo**](AccountInfo.md)

### Authorization

[barApiToken](../README.md#barApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_status**
> AccountStatus get_account_status()

Get MQTT status info

Retrieves MQTT status

### Example

* Bearer Authentication (barApiToken):

```python
import busybar_python_sdk
from busybar_python_sdk.models.account_status import AccountStatus
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
    api_instance = busybar_python_sdk.AccountApi(api_client)

    try:
        # Get MQTT status info
        api_response = api_instance.get_account_status()
        print("The response of AccountApi->get_account_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountStatus**](AccountStatus.md)

### Authorization

[barApiToken](../README.md#barApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

