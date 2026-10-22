# busybar_python_sdk.SystemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dump_log**](SystemApi.md#dump_log) | **POST** /api/log_dump | Dump captured log
[**get_status**](SystemApi.md#get_status) | **GET** /api/status | Get device status
[**get_status_device**](SystemApi.md#get_status_device) | **GET** /api/status/device | Get device info
[**get_status_firmware**](SystemApi.md#get_status_firmware) | **GET** /api/status/firmware | Get firmware info
[**get_status_power**](SystemApi.md#get_status_power) | **GET** /api/status/power | Get power status
[**get_status_system**](SystemApi.md#get_status_system) | **GET** /api/status/system | Get system status
[**get_transport**](SystemApi.md#get_transport) | **GET** /api/transport | Get device network connection info
[**get_version**](SystemApi.md#get_version) | **GET** /api/version | Get API version information


# **dump_log**
> DumpLog200Response dump_log(filename=filename)

Dump captured log

Snapshot the in-memory log buffer to a file (defaults to /ext/log.txt)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.dump_log200_response import DumpLog200Response
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
    api_instance = busybar_python_sdk.SystemApi(api_client)
    filename = 'log' # str | Destination file name (without extension) (optional)

    try:
        # Dump captured log
        api_response = api_instance.dump_log(filename=filename)
        print("The response of SystemApi->dump_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->dump_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Destination file name (without extension) | [optional] 

### Return type

[**DumpLog200Response**](DumpLog200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Log dumped successfully |  -  |
**400** | Invalid filename |  -  |
**508** | Failed to dump logs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> Status get_status()

Get device status

Get device status

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.status import Status
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
    api_instance = busybar_python_sdk.SystemApi(api_client)

    try:
        # Get device status
        api_response = api_instance.get_status()
        print("The response of SystemApi->get_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information retrieved successfully |  -  |
**503** | Failed to retrieve status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_device**
> StatusDevice get_status_device()

Get device info

Get device info

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.status_device import StatusDevice
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
    api_instance = busybar_python_sdk.SystemApi(api_client)

    try:
        # Get device info
        api_response = api_instance.get_status_device()
        print("The response of SystemApi->get_status_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_status_device: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StatusDevice**](StatusDevice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information retrieved successfully |  -  |
**503** | Failed to retrieve status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_firmware**
> StatusFirmware get_status_firmware()

Get firmware info

Get firmware info

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.status_firmware import StatusFirmware
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
    api_instance = busybar_python_sdk.SystemApi(api_client)

    try:
        # Get firmware info
        api_response = api_instance.get_status_firmware()
        print("The response of SystemApi->get_status_firmware:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_status_firmware: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StatusFirmware**](StatusFirmware.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information retrieved successfully |  -  |
**503** | Failed to retrieve status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_power**
> StatusPower get_status_power()

Get power status

Get power status

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.status_power import StatusPower
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
    api_instance = busybar_python_sdk.SystemApi(api_client)

    try:
        # Get power status
        api_response = api_instance.get_status_power()
        print("The response of SystemApi->get_status_power:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_status_power: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StatusPower**](StatusPower.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information retrieved successfully |  -  |
**503** | Failed to retrieve status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_system**
> StatusSystem get_status_system()

Get system status

Get system status

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.status_system import StatusSystem
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
    api_instance = busybar_python_sdk.SystemApi(api_client)

    try:
        # Get system status
        api_response = api_instance.get_status_system()
        print("The response of SystemApi->get_status_system:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_status_system: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StatusSystem**](StatusSystem.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Information retrieved successfully |  -  |
**503** | Failed to retrieve status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport**
> NetworkInterfaceInfo get_transport()

Get device network connection info

Retrieves device transport type (usb/wifi)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.network_interface_info import NetworkInterfaceInfo
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
    api_instance = busybar_python_sdk.SystemApi(api_client)

    try:
        # Get device network connection info
        api_response = api_instance.get_transport()
        print("The response of SystemApi->get_transport:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_transport: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NetworkInterfaceInfo**](NetworkInterfaceInfo.md)

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

# **get_version**
> VersionInfo get_version()

Get API version information

Retrieves API version

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import busybar_python_sdk
from busybar_python_sdk.models.version_info import VersionInfo
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
    api_instance = busybar_python_sdk.SystemApi(api_client)

    try:
        # Get API version information
        api_response = api_instance.get_version()
        print("The response of SystemApi->get_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**VersionInfo**](VersionInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version information retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

