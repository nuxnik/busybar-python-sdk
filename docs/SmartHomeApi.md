# openapi_client.SmartHomeApi

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

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.success_response import SuccessResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SmartHomeApi(api_client)

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

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.smart_home_switch_state import SmartHomeSwitchState
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SmartHomeApi(api_client)

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

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.smart_home_switch_state import SmartHomeSwitchState
from openapi_client.models.success_response import SuccessResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SmartHomeApi(api_client)
    smart_home_switch_state = openapi_client.SmartHomeSwitchState() # SmartHomeSwitchState | 

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

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.smart_home_pairing_info import SmartHomePairingInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SmartHomeApi(api_client)

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

[ApiKeyAuth](../README.md#ApiKeyAuth)

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

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.smart_home_pairing_payload import SmartHomePairingPayload
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SmartHomeApi(api_client)

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

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully started smart home pairing |  -  |
**503** | Internal smart home service is broken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

