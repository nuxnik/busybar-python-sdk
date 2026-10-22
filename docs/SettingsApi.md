# busybar_python_sdk.SettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_name_get**](SettingsApi.md#api_name_get) | **GET** /api/name | Get current device name
[**api_name_post**](SettingsApi.md#api_name_post) | **POST** /api/name | Set new device name
[**create_access_token**](SettingsApi.md#create_access_token) | **POST** /api/access/tokens | Create a new access token
[**delete_all_access_tokens**](SettingsApi.md#delete_all_access_tokens) | **DELETE** /api/access/tokens | Revoke all access tokens
[**get_access_tokens**](SettingsApi.md#get_access_tokens) | **GET** /api/access/tokens | List all access tokens
[**get_audio_volume**](SettingsApi.md#get_audio_volume) | **GET** /api/audio/volume | Get audio volume
[**get_display_brightness**](SettingsApi.md#get_display_brightness) | **GET** /api/display/brightness | Get display brightness
[**get_http_access**](SettingsApi.md#get_http_access) | **GET** /api/access | Get HTTP API access over Wi-Fi configuration
[**revoke_access_token**](SettingsApi.md#revoke_access_token) | **DELETE** /api/access/tokens/{short_id} | Revoke an access token
[**set_audio_volume**](SettingsApi.md#set_audio_volume) | **POST** /api/audio/volume | Set audio volume
[**set_display_brightness**](SettingsApi.md#set_display_brightness) | **POST** /api/display/brightness | Set display brightness
[**set_http_access**](SettingsApi.md#set_http_access) | **POST** /api/access | Set HTTP API access over Wi-Fi configuration


# **api_name_get**
> NameInfo api_name_get()

Get current device name

Get current device name

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.name_info import NameInfo
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
    api_instance = busybar_python_sdk.SettingsApi(api_client)

    try:
        # Get current device name
        api_response = api_instance.api_name_get()
        print("The response of SettingsApi->api_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->api_name_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NameInfo**](NameInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_name_post**
> SuccessResponse api_name_post(name_info)

Set new device name

Set new device name

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.name_info import NameInfo
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
    api_instance = busybar_python_sdk.SettingsApi(api_client)
    name_info = busybar_python_sdk.NameInfo() # NameInfo | 

    try:
        # Set new device name
        api_response = api_instance.api_name_post(name_info)
        print("The response of SettingsApi->api_name_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->api_name_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_info** | [**NameInfo**](NameInfo.md)|  | 

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
**200** | New name successfully set |  -  |
**400** | Invalid name parameter, or failed to store new name |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_access_token**
> AccessToken create_access_token(access_tokens_create_request)

Create a new access token

Generates a new access token for authorization alongside the access key

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.access_token import AccessToken
from busybar_python_sdk.models.access_tokens_create_request import AccessTokensCreateRequest
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
    api_instance = busybar_python_sdk.SettingsApi(api_client)
    access_tokens_create_request = busybar_python_sdk.AccessTokensCreateRequest() # AccessTokensCreateRequest | 

    try:
        # Create a new access token
        api_response = api_instance.create_access_token(access_tokens_create_request)
        print("The response of SettingsApi->create_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->create_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_tokens_create_request** | [**AccessTokensCreateRequest**](AccessTokensCreateRequest.md)|  | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved information about access tokens |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_access_tokens**
> SuccessResponse delete_all_access_tokens()

Revoke all access tokens

Removes all access tokens all at once

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
    api_instance = busybar_python_sdk.SettingsApi(api_client)

    try:
        # Revoke all access tokens
        api_response = api_instance.delete_all_access_tokens()
        print("The response of SettingsApi->delete_all_access_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->delete_all_access_tokens: %s\n" % e)
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
**200** | Deleted all access tokens |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_tokens**
> AccessTokensInfo get_access_tokens()

List all access tokens

Provides basic information all access tokens (IDs, names and timestamps)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.access_tokens_info import AccessTokensInfo
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
    api_instance = busybar_python_sdk.SettingsApi(api_client)

    try:
        # List all access tokens
        api_response = api_instance.get_access_tokens()
        print("The response of SettingsApi->get_access_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_access_tokens: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccessTokensInfo**](AccessTokensInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audio_volume**
> AudioVolumeInfo get_audio_volume()

Get audio volume

Get audio volume value

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.audio_volume_info import AudioVolumeInfo
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
    api_instance = busybar_python_sdk.SettingsApi(api_client)

    try:
        # Get audio volume
        api_response = api_instance.get_audio_volume()
        print("The response of SettingsApi->get_audio_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_audio_volume: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AudioVolumeInfo**](AudioVolumeInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_display_brightness**
> DisplayBrightnessInfo get_display_brightness()

Get display brightness

Get brightness value for displays

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.display_brightness_info import DisplayBrightnessInfo
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
    api_instance = busybar_python_sdk.SettingsApi(api_client)

    try:
        # Get display brightness
        api_response = api_instance.get_display_brightness()
        print("The response of SettingsApi->get_display_brightness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_display_brightness: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DisplayBrightnessInfo**](DisplayBrightnessInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_http_access**
> HttpAccessInfo get_http_access()

Get HTTP API access over Wi-Fi configuration

Get HTTP API access over Wi-Fi configuration

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.http_access_info import HttpAccessInfo
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
    api_instance = busybar_python_sdk.SettingsApi(api_client)

    try:
        # Get HTTP API access over Wi-Fi configuration
        api_response = api_instance.get_http_access()
        print("The response of SettingsApi->get_http_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_http_access: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HttpAccessInfo**](HttpAccessInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_access_token**
> SuccessResponse revoke_access_token(short_id)

Revoke an access token

Removes the access token with the specified short ID

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
    api_instance = busybar_python_sdk.SettingsApi(api_client)
    short_id = 'short_id_example' # str | 

    try:
        # Revoke an access token
        api_response = api_instance.revoke_access_token(short_id)
        print("The response of SettingsApi->revoke_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->revoke_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_id** | **str**|  | 

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
**200** | Deleted corresponding access token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_audio_volume**
> SuccessResponse set_audio_volume(volume, silent=silent)

Set audio volume

Set audio volume value

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
    api_instance = busybar_python_sdk.SettingsApi(api_client)
    volume = 50 # float | Audio volume (0-100)
    silent = 1 # int | Set volume silently (0 - play volume change sound(default), 1 - do not play sound) (optional)

    try:
        # Set audio volume
        api_response = api_instance.set_audio_volume(volume, silent=silent)
        print("The response of SettingsApi->set_audio_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->set_audio_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume** | **float**| Audio volume (0-100) | 
 **silent** | **int**| Set volume silently (0 - play volume change sound(default), 1 - do not play sound) | [optional] 

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
**200** | Volume set successfully |  -  |
**400** | Invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_display_brightness**
> SuccessResponse set_display_brightness(value)

Set display brightness

Set brightness for one or both displays


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
    api_instance = busybar_python_sdk.SettingsApi(api_client)
    value = '50' # str | Displays brightness (0-100/auto)

    try:
        # Set display brightness
        api_response = api_instance.set_display_brightness(value)
        print("The response of SettingsApi->set_display_brightness:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->set_display_brightness: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| Displays brightness (0-100/auto) | 

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
**200** | Brightness set successfully |  -  |
**400** | Invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_http_access**
> SuccessResponse set_http_access(mode, key=key)

Set HTTP API access over Wi-Fi configuration

Set HTTP API access over Wi-Fi configuration

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
    api_instance = busybar_python_sdk.SettingsApi(api_client)
    mode = 'key' # str | Access mode
    key = '12345678' # str | Access key (4-10 digits length). Required when mode is \"key\". (optional)

    try:
        # Set HTTP API access over Wi-Fi configuration
        api_response = api_instance.set_http_access(mode, key=key)
        print("The response of SettingsApi->set_http_access:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->set_http_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mode** | **str**| Access mode | 
 **key** | **str**| Access key (4-10 digits length). Required when mode is \&quot;key\&quot;. | [optional] 

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
**200** | Set successfully |  -  |
**400** | Invalid request data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

