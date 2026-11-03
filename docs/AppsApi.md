# busybar_python_sdk.AppsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_settings**](AppsApi.md#get_app_settings) | **GET** /api/apps/settings | Get application settings
[**install_app**](AppsApi.md#install_app) | **POST** /api/apps/install | Install a staged JavaScript application
[**launch_app**](AppsApi.md#launch_app) | **POST** /api/apps/launch | Launch an installed JavaScript application
[**list_apps**](AppsApi.md#list_apps) | **GET** /api/apps/list | List installed JavaScript applications
[**quit_app**](AppsApi.md#quit_app) | **POST** /api/apps/quit | Quit from a running JavaScript application
[**remove_app**](AppsApi.md#remove_app) | **DELETE** /api/apps | Delete a JavaScript application
[**reset_app_settings**](AppsApi.md#reset_app_settings) | **DELETE** /api/apps/settings | Reset application settings
[**set_app_settings**](AppsApi.md#set_app_settings) | **PUT** /api/apps/settings | Set application settings
[**stage_app**](AppsApi.md#stage_app) | **POST** /api/apps/stage | Stage a JavaScript application for installation


# **get_app_settings**
> AppSettingsDocument get_app_settings(app_id)

Get application settings

Returns the complete settings document; the first request materializes it from the schema defaults.


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.app_settings_document import AppSettingsDocument
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
    api_instance = busybar_python_sdk.AppsApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Get application settings
        api_response = api_instance.get_app_settings(app_id)
        print("The response of AppsApi->get_app_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->get_app_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

### Return type

[**AppSettingsDocument**](AppSettingsDocument.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings document |  -  |
**400** | Invalid app_id parameter value |  -  |
**403** | Requested application id does not match running application id |  -  |
**404** | Unknown or invalid application, or no settings |  -  |
**503** | Invalid settings schema or failed to build the document |  -  |
**508** | Storage error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_app**
> SuccessResponse install_app(install_key)

Install a staged JavaScript application

Installs a staged JavaScript application using the installation key

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
    api_instance = busybar_python_sdk.AppsApi(api_client)
    install_key = 123456789 # int | Installation key

    try:
        # Install a staged JavaScript application
        api_response = api_instance.install_app(install_key)
        print("The response of AppsApi->install_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->install_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_key** | **int**| Installation key | 

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
**200** | Application installed successfully. |  -  |
**400** | Invalid parameters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **launch_app**
> SuccessResponse launch_app(app_id)

Launch an installed JavaScript application

Launches an installed JavaScript application by its id

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
    api_instance = busybar_python_sdk.AppsApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Launch an installed JavaScript application
        api_response = api_instance.launch_app(app_id)
        print("The response of AppsApi->launch_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->launch_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

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
**200** | Application launched successfully |  -  |
**404** | App with given ID was not found |  -  |
**400** | Missing or invalid application id |  -  |
**409** | A higher-priority application is already running |  -  |
**503** | Failed to launch the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_apps**
> AppListResult list_apps()

List installed JavaScript applications

Lists installed JavaScript applications

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.app_list_result import AppListResult
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
    api_instance = busybar_python_sdk.AppsApi(api_client)

    try:
        # List installed JavaScript applications
        api_response = api_instance.list_apps()
        print("The response of AppsApi->list_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->list_apps: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AppListResult**](AppListResult.md)

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

# **quit_app**
> SuccessResponse quit_app()

Quit from a running JavaScript application

Quits from a running JavaScript application, if there is one

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
    api_instance = busybar_python_sdk.AppsApi(api_client)

    try:
        # Quit from a running JavaScript application
        api_response = api_instance.quit_app()
        print("The response of AppsApi->quit_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->quit_app: %s\n" % e)
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
**200** | Exited from the application successfully |  -  |
**409** | Application is not running |  -  |
**503** | Failed to quit from the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_app**
> SuccessResponse remove_app(app_id)

Delete a JavaScript application

Removes an installed JavaScript application, keeping its settings

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
    api_instance = busybar_python_sdk.AppsApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Delete a JavaScript application
        api_response = api_instance.remove_app(app_id)
        print("The response of AppsApi->remove_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->remove_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

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
**404** | App with given ID was not found |  -  |
**400** | Missing application id |  -  |
**503** | Failed to quit from the application that needs to be uninstalled.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_app_settings**
> SuccessResponse reset_app_settings(app_id)

Reset application settings

Resets every field to its schema default.

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
    api_instance = busybar_python_sdk.AppsApi(api_client)
    app_id = 'app_id_example' # str | 

    try:
        # Reset application settings
        api_response = api_instance.reset_app_settings(app_id)
        print("The response of AppsApi->reset_app_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->reset_app_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 

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
**200** | Settings reset |  -  |
**400** | Invalid app_id parameter value |  -  |
**404** | Unknown or invalid application, or no settings |  -  |
**503** | Invalid settings schema |  -  |
**508** | Storage error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_app_settings**
> SuccessResponse set_app_settings(app_id, app_settings_document)

Set application settings

Replaces the settings document: every field must be present and valid, with a version matching the application settings; unknown keys are dropped.


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.app_settings_document import AppSettingsDocument
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
    api_instance = busybar_python_sdk.AppsApi(api_client)
    app_id = 'app_id_example' # str | 
    app_settings_document = busybar_python_sdk.AppSettingsDocument() # AppSettingsDocument | 

    try:
        # Set application settings
        api_response = api_instance.set_app_settings(app_id, app_settings_document)
        print("The response of AppsApi->set_app_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->set_app_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**|  | 
 **app_settings_document** | [**AppSettingsDocument**](AppSettingsDocument.md)|  | 

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
**200** | Settings stored |  -  |
**400** | Invalid app_id parameter value or invalid document |  -  |
**404** | Unknown or invalid application, or no settings |  -  |
**503** | Invalid settings schema |  -  |
**508** | Storage error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stage_app**
> AppStageResult stage_app(body)

Stage a JavaScript application for installation

Uploads an application package (TGZ or TAR file) and initiates the installation process.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.app_stage_result import AppStageResult
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
    api_instance = busybar_python_sdk.AppsApi(api_client)
    body = None # bytes | 

    try:
        # Stage a JavaScript application for installation
        api_response = api_instance.stage_app(body)
        print("The response of AppsApi->stage_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppsApi->stage_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytes**|  | 

### Return type

[**AppStageResult**](AppStageResult.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application staged successfully. |  -  |
**400** | Invalid parameters, invalid package file, or installation preparation failed. |  -  |
**409** | API version required by the application is not compatible with the firmware. |  -  |
**413** | Application package too large. |  -  |
**508** | Failed to save the application package. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

