# busybar-python-sdk.AccountApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_backend**](AccountApi.md#get_account_backend) | **GET** /api/account/backend | Get MQTT configuration
[**get_account_info**](AccountApi.md#get_account_info) | **GET** /api/account/info | Get linked account info
[**get_account_status**](AccountApi.md#get_account_status) | **GET** /api/account/status | Get MQTT status info
[**link_account**](AccountApi.md#link_account) | **POST** /api/account/link | Link device to account
[**set_account_backend**](AccountApi.md#set_account_backend) | **PUT** /api/account/backend | Set MQTT configuration
[**unlink_account**](AccountApi.md#unlink_account) | **DELETE** /api/account | Unlink device from account


# **get_account_backend**
> AccountBackend get_account_backend()

Get MQTT configuration

Retrieves MQTT backend configuration

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
from busybar-python-sdk.models.account_backend import AccountBackend
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
    api_instance = busybar-python-sdk.AccountApi(api_client)

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

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
from busybar-python-sdk.models.account_info import AccountInfo
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
    api_instance = busybar-python-sdk.AccountApi(api_client)

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

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
from busybar-python-sdk.models.account_status import AccountStatus
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
    api_instance = busybar-python-sdk.AccountApi(api_client)

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

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_account**
> AccountLink link_account()

Link device to account

Requests account link PIN. Works only if device is connected to MQTT and is not linked to account

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
from busybar-python-sdk.models.account_link import AccountLink
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
    api_instance = busybar-python-sdk.AccountApi(api_client)

    try:
        # Link device to account
        api_response = api_instance.link_account()
        print("The response of AccountApi->link_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->link_account: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountLink**](AccountLink.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data retrieved successfully |  -  |
**400** | Bad request |  -  |
**503** | PIN request timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_account_backend**
> SuccessResponse set_account_backend(account_backend)

Set MQTT configuration

Sets MQTT backend configuration

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
from busybar-python-sdk.models.account_backend import AccountBackend
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
    api_instance = busybar-python-sdk.AccountApi(api_client)
    account_backend = busybar-python-sdk.AccountBackend() # AccountBackend | 

    try:
        # Set MQTT configuration
        api_response = api_instance.set_account_backend(account_backend)
        print("The response of AccountApi->set_account_backend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->set_account_backend: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_backend** | [**AccountBackend**](AccountBackend.md)|  | 

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
**200** | Set successfully |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_account**
> SuccessResponse unlink_account()

Unlink device from account

Removes account linking data

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
    api_instance = busybar-python-sdk.AccountApi(api_client)

    try:
        # Unlink device from account
        api_response = api_instance.unlink_account()
        print("The response of AccountApi->unlink_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->unlink_account: %s\n" % e)
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
**200** | Done successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

