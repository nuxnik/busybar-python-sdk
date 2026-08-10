# busybar-python-sdk.UpdaterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abort_firmware_download**](UpdaterApi.md#abort_firmware_download) | **POST** /api/update/abort_download | Abort ongoing firmware download
[**check_firmware_update**](UpdaterApi.md#check_firmware_update) | **POST** /api/update/check | Start firmware update check
[**get_autoupdate_settings**](UpdaterApi.md#get_autoupdate_settings) | **GET** /api/update/autoupdate | Get autoupdate settings
[**get_firmware_update_status**](UpdaterApi.md#get_firmware_update_status) | **GET** /api/update/status | Get firmware update status
[**get_update_changelog**](UpdaterApi.md#get_update_changelog) | **GET** /api/update/changelog | Get update changelog
[**install_firmware_update**](UpdaterApi.md#install_firmware_update) | **POST** /api/update/install | Install firmware update
[**set_autoupdate_settings**](UpdaterApi.md#set_autoupdate_settings) | **POST** /api/update/autoupdate | Set autoupdate settings
[**update_firmware**](UpdaterApi.md#update_firmware) | **POST** /api/update | Update firmware


# **abort_firmware_download**
> SuccessResponse abort_firmware_download()

Abort ongoing firmware download

Signals the updater to abort an ongoing download operation.

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
    api_instance = busybar-python-sdk.UpdaterApi(api_client)

    try:
        # Abort ongoing firmware download
        api_response = api_instance.abort_firmware_download()
        print("The response of UpdaterApi->abort_firmware_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdaterApi->abort_firmware_download: %s\n" % e)
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
**200** | Abort signal sent successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_firmware_update**
> SuccessResponse check_firmware_update()

Start firmware update check

Initiates an asynchronous check for available firmware updates.

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
    api_instance = busybar-python-sdk.UpdaterApi(api_client)

    try:
        # Start firmware update check
        api_response = api_instance.check_firmware_update()
        print("The response of UpdaterApi->check_firmware_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdaterApi->check_firmware_update: %s\n" % e)
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
**200** | Update check started successfully |  -  |
**409** | Update check already in progress |  -  |
**503** | Failed to start update check |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_autoupdate_settings**
> AutoupdateSettings get_autoupdate_settings()

Get autoupdate settings

Returns current autoupdate configuration

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
from busybar-python-sdk.models.autoupdate_settings import AutoupdateSettings
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
    api_instance = busybar-python-sdk.UpdaterApi(api_client)

    try:
        # Get autoupdate settings
        api_response = api_instance.get_autoupdate_settings()
        print("The response of UpdaterApi->get_autoupdate_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdaterApi->get_autoupdate_settings: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**AutoupdateSettings**](AutoupdateSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Settings retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firmware_update_status**
> UpdateStatus get_firmware_update_status()

Get firmware update status

Returns current update and check status including progress information.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
from busybar-python-sdk.models.update_status import UpdateStatus
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
    api_instance = busybar-python-sdk.UpdaterApi(api_client)

    try:
        # Get firmware update status
        api_response = api_instance.get_firmware_update_status()
        print("The response of UpdaterApi->get_firmware_update_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdaterApi->get_firmware_update_status: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**UpdateStatus**](UpdateStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_update_changelog**
> GetUpdateChangelog200Response get_update_changelog(version)

Get update changelog

Returns the changelog for a specific firmware version.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
from busybar-python-sdk.models.get_update_changelog200_response import GetUpdateChangelog200Response
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
    api_instance = busybar-python-sdk.UpdaterApi(api_client)
    version = '1.2.3' # str | Firmware version to get changelog for

    try:
        # Get update changelog
        api_response = api_instance.get_update_changelog(version)
        print("The response of UpdaterApi->get_update_changelog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdaterApi->get_update_changelog: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Firmware version to get changelog for | 

### Return type

[**GetUpdateChangelog200Response**](GetUpdateChangelog200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Changelog retrieved successfully |  -  |
**400** | Version parameter missing, update not available, or version mismatch |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_firmware_update**
> SuccessResponse install_firmware_update(version)

Install firmware update

Starts asynchronous firmware installation from a remote URL.
The update process (download, SHA verification, unpack, prepare, reboot) runs in the background.
Use /api/update/status to monitor progress.


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
    api_instance = busybar-python-sdk.UpdaterApi(api_client)
    version = '1.2.3' # str | Firmware version to install

    try:
        # Install firmware update
        api_response = api_instance.install_firmware_update(version)
        print("The response of UpdaterApi->install_firmware_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdaterApi->install_firmware_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Firmware version to install | 

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
**200** | Update installation started successfully in background |  -  |
**400** | Version parameter missing, update not available, or version mismatch |  -  |
**409** | Update already in progress |  -  |
**503** | Battery too low or installation failed to start |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_autoupdate_settings**
> SuccessResponse set_autoupdate_settings(autoupdate_settings)

Set autoupdate settings

Updates autoupdate configuration. All fields are optional - only provided fields are updated.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar-python-sdk
from busybar-python-sdk.models.autoupdate_settings import AutoupdateSettings
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
    api_instance = busybar-python-sdk.UpdaterApi(api_client)
    autoupdate_settings = busybar-python-sdk.AutoupdateSettings() # AutoupdateSettings | 

    try:
        # Set autoupdate settings
        api_response = api_instance.set_autoupdate_settings(autoupdate_settings)
        print("The response of UpdaterApi->set_autoupdate_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdaterApi->set_autoupdate_settings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **autoupdate_settings** | [**AutoupdateSettings**](AutoupdateSettings.md)|  | 

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
**200** | Settings updated successfully |  -  |
**400** | Invalid time format (expected HH:MM) |  -  |
**503** | Failed to apply settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firmware**
> SuccessResponse update_firmware(body)

Update firmware

Uploads a firmware update package (TAR file) and initiates the update process.

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
    api_instance = busybar-python-sdk.UpdaterApi(api_client)
    body = None # bytearray | 

    try:
        # Update firmware
        api_response = api_instance.update_firmware(body)
        print("The response of UpdaterApi->update_firmware:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpdaterApi->update_firmware: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytearray**|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update initiated successfully. The device will reboot. |  -  |
**400** | Invalid parameters, invalid TAR file, or update preparation failed. |  -  |
**409** | Upload received on a closed or invalid update context. |  -  |
**413** | Update package too large. |  -  |
**508** | Failed to save the update package. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

