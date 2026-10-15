# busybar_python_sdk.StreamingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**busybar_screen_get**](StreamingApi.md#busybar_screen_get) | **GET** /busybar/screen | Get single frame for requested screen


# **busybar_screen_get**
> str busybar_screen_get(display)

Get single frame for requested screen

### Example

* Bearer Authentication (barApiToken):

```python
import busybar_python_sdk
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
    api_instance = busybar_python_sdk.StreamingApi(api_client)
    display = 0 # int | Type of the display Front = 0, Back = 1

    try:
        # Get single frame for requested screen
        api_response = api_instance.busybar_screen_get(display)
        print("The response of StreamingApi->busybar_screen_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StreamingApi->busybar_screen_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display** | **int**| Type of the display Front &#x3D; 0, Back &#x3D; 1 | 

### Return type

**str**

### Authorization

[barApiToken](../README.md#barApiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/bmp, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Wrong display |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

