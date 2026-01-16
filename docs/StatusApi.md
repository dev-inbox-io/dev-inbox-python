# devinbox_client.StatusApi

All URIs are relative to *http://localhost:5062*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status**](StatusApi.md#get_status) | **GET** /status | Get API service status


# **get_status**
> get_status()

Get API service status

Returns OK if the API service is running and available.

### Example


```python
import devinbox_client
from devinbox_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5062
# See configuration.py for a list of all supported configuration parameters.
configuration = devinbox_client.Configuration(
    host = "http://localhost:5062"
)


# Enter a context with an instance of the API client
with devinbox_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devinbox_client.StatusApi(api_client)

    try:
        # Get API service status
        api_instance.get_status()
    except Exception as e:
        print("Exception when calling StatusApi->get_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

