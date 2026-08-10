# busybar_python_sdk.AssetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_display**](AssetsApi.md#clear_display) | **DELETE** /api/display/draw | Clear display
[**delete_app_assets**](AssetsApi.md#delete_app_assets) | **DELETE** /api/assets/upload | Delete app assets
[**draw_on_display**](AssetsApi.md#draw_on_display) | **POST** /api/display/draw | Draw on display
[**play_audio**](AssetsApi.md#play_audio) | **POST** /api/audio/play | Play audio file
[**stop_audio**](AssetsApi.md#stop_audio) | **DELETE** /api/audio/play | Stop audio playback
[**upload_asset_with_app_id**](AssetsApi.md#upload_asset_with_app_id) | **POST** /api/assets/upload | Upload asset file with app ID


# **clear_display**
> SuccessResponse clear_display(application_name=application_name)

Clear display

Deletes display elements drawn by the Canvas application. If application_name is specified, only elements for that app are removed.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
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
    api_instance = busybar_python_sdk.AssetsApi(api_client)
    application_name = 'my_app' # str | Application identifier (optional)

    try:
        # Clear display
        api_response = api_instance.clear_display(application_name=application_name)
        print("The response of AssetsApi->clear_display:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->clear_display: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| Application identifier | [optional] 

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
**200** | Display cleared successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_assets**
> SuccessResponse delete_app_assets(application_name)

Delete app assets

Deletes all assets for a specific app ID

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
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
    api_instance = busybar_python_sdk.AssetsApi(api_client)
    application_name = 'my_app' # str | Application ID whose assets should be deleted

    try:
        # Delete app assets
        api_response = api_instance.delete_app_assets(application_name)
        print("The response of AssetsApi->delete_app_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->delete_app_assets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| Application ID whose assets should be deleted | 

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
**200** | Assets deleted successfully |  -  |
**400** | Invalid request parameters |  -  |
**503** | Delete failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **draw_on_display**
> SuccessResponse draw_on_display(display_elements)

Draw on display

Sends drawing data to the display.
Supports JSON-defined display elements.


### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar_python_sdk
from busybar_python_sdk.models.display_elements import DisplayElements
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
    api_instance = busybar_python_sdk.AssetsApi(api_client)
    display_elements = busybar_python_sdk.DisplayElements() # DisplayElements | 

    try:
        # Draw on display
        api_response = api_instance.draw_on_display(display_elements)
        print("The response of AssetsApi->draw_on_display:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->draw_on_display: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_elements** | [**DisplayElements**](DisplayElements.md)|  | 

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
**200** | Drawing command executed successfully |  -  |
**400** | Invalid drawing data |  -  |
**409** | Requested priority level is below that of currently active app |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **play_audio**
> SuccessResponse play_audio(play_audio)

Play audio file

Plays an audio file from the assets directory.
Supported formats include .snd files.


### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import busybar_python_sdk
from busybar_python_sdk.models.play_audio import PlayAudio
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
    api_instance = busybar_python_sdk.AssetsApi(api_client)
    play_audio = busybar_python_sdk.PlayAudio() # PlayAudio | 

    try:
        # Play audio file
        api_response = api_instance.play_audio(play_audio)
        print("The response of AssetsApi->play_audio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->play_audio: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **play_audio** | [**PlayAudio**](PlayAudio.md)|  | 

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
**200** | Audio playback started successfully |  -  |
**400** | Invalid file path |  -  |
**404** | Audio file not found or is unplayable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_audio**
> SuccessResponse stop_audio()

Stop audio playback

Stops any currently playing audio

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
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
    api_instance = busybar_python_sdk.AssetsApi(api_client)

    try:
        # Stop audio playback
        api_response = api_instance.stop_audio()
        print("The response of AssetsApi->stop_audio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->stop_audio: %s\n" % e)
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
**200** | Audio playback stopped successfully |  -  |
**410** | No audio is playing |  -  |
**503** | Audio system error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_asset_with_app_id**
> SuccessResponse upload_asset_with_app_id(application_name, file, body)

Upload asset file with app ID

Uploads a file to a specific app's assets directory

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
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
    api_instance = busybar_python_sdk.AssetsApi(api_client)
    application_name = 'my_app' # str | Application ID for organizing assets
    file = 'data.png' # str | Filename for the uploaded asset
    body = None # bytearray | 

    try:
        # Upload asset file with app ID
        api_response = api_instance.upload_asset_with_app_id(application_name, file, body)
        print("The response of AssetsApi->upload_asset_with_app_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->upload_asset_with_app_id: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**| Application ID for organizing assets | 
 **file** | **str**| Filename for the uploaded asset | 
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
**200** | File uploaded successfully |  -  |
**400** | Invalid parameters or upload failed |  -  |
**413** | File too large |  -  |
**508** | Failed to write uploaded file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

