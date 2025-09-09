# devinbox_client.MessagesApi

All URIs are relative to *https://api.devinbox.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_last_message**](MessagesApi.md#get_last_message) | **GET** /messages/{key}/last | Get last message from mailbox
[**get_last_message_with_template**](MessagesApi.md#get_last_message_with_template) | **GET** /messages/{key}/{template}/last | Get last message with template parsing
[**get_message_by_id**](MessagesApi.md#get_message_by_id) | **GET** /messages/{key}/get | Get a specific message by ID
[**get_message_count**](MessagesApi.md#get_message_count) | **GET** /messages/{key}/count | Get message count
[**get_messages**](MessagesApi.md#get_messages) | **GET** /messages/{key} | Get messages from a mailbox
[**get_single_message**](MessagesApi.md#get_single_message) | **GET** /messages/{key}/single | Get single message from mailbox
[**get_single_message_with_template**](MessagesApi.md#get_single_message_with_template) | **GET** /messages/{key}/{template}/single | Get single message with template parsing


# **get_last_message**
> MessageViewModel get_last_message(key)

Get last message from mailbox

Retrieves the most recent message from the specified mailbox. Fails if mailbox is empty.

### Example

* Api Key Authentication (ApiKey):

```python
import devinbox_client
from devinbox_client.models.message_view_model import MessageViewModel
from devinbox_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.devinbox.io
# See configuration.py for a list of all supported configuration parameters.
configuration = devinbox_client.Configuration(
    host = "https://api.devinbox.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with devinbox_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devinbox_client.MessagesApi(api_client)
    key = 'key_example' # str | Mailbox key

    try:
        # Get last message from mailbox
        api_response = api_instance.get_last_message(key)
        print("The response of MessagesApi->get_last_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_last_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Mailbox key | 

### Return type

[**MessageViewModel**](MessageViewModel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_message_with_template**
> MessageParsedViewModel get_last_message_with_template(key, template)

Get last message with template parsing

Retrieves the most recent message from the specified mailbox and parses it using the specified template. Fails if mailbox is empty.

### Example

* Api Key Authentication (ApiKey):

```python
import devinbox_client
from devinbox_client.models.message_parsed_view_model import MessageParsedViewModel
from devinbox_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.devinbox.io
# See configuration.py for a list of all supported configuration parameters.
configuration = devinbox_client.Configuration(
    host = "https://api.devinbox.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with devinbox_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devinbox_client.MessagesApi(api_client)
    key = 'key_example' # str | Mailbox key
    template = 'template_example' # str | Template name for parsing the message

    try:
        # Get last message with template parsing
        api_response = api_instance.get_last_message_with_template(key, template)
        print("The response of MessagesApi->get_last_message_with_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_last_message_with_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Mailbox key | 
 **template** | **str**| Template name for parsing the message | 

### Return type

[**MessageParsedViewModel**](MessageParsedViewModel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_by_id**
> MessageViewModel get_message_by_id(key, id)

Get a specific message by ID

Retrieves a specific message from the specified mailbox using its unique ID.

### Example

* Api Key Authentication (ApiKey):

```python
import devinbox_client
from devinbox_client.models.message_view_model import MessageViewModel
from devinbox_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.devinbox.io
# See configuration.py for a list of all supported configuration parameters.
configuration = devinbox_client.Configuration(
    host = "https://api.devinbox.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with devinbox_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devinbox_client.MessagesApi(api_client)
    key = 'key_example' # str | Mailbox key
    id = 'id_example' # str | Message unique ID

    try:
        # Get a specific message by ID
        api_response = api_instance.get_message_by_id(key, id)
        print("The response of MessagesApi->get_message_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_message_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Mailbox key | 
 **id** | **str**| Message unique ID | 

### Return type

[**MessageViewModel**](MessageViewModel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_count**
> MessageCountResult get_message_count(key)

Get message count

Gets the number of messages in the specified mailbox

### Example

* Api Key Authentication (ApiKey):

```python
import devinbox_client
from devinbox_client.models.message_count_result import MessageCountResult
from devinbox_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.devinbox.io
# See configuration.py for a list of all supported configuration parameters.
configuration = devinbox_client.Configuration(
    host = "https://api.devinbox.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with devinbox_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devinbox_client.MessagesApi(api_client)
    key = 'key_example' # str | Mailbox key

    try:
        # Get message count
        api_response = api_instance.get_message_count(key)
        print("The response of MessagesApi->get_message_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_message_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Mailbox key | 

### Return type

[**MessageCountResult**](MessageCountResult.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages**
> MessagesViewModel get_messages(key, skip=skip, take=take)

Get messages from a mailbox

Retrieves messages from the specified mailbox with optional pagination. Default: skip=0, take=10, max take=25.

### Example

* Api Key Authentication (ApiKey):

```python
import devinbox_client
from devinbox_client.models.messages_view_model import MessagesViewModel
from devinbox_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.devinbox.io
# See configuration.py for a list of all supported configuration parameters.
configuration = devinbox_client.Configuration(
    host = "https://api.devinbox.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with devinbox_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devinbox_client.MessagesApi(api_client)
    key = 'key_example' # str | Mailbox key
    skip = 56 # int | Number of messages to skip (default: 0) (optional)
    take = 56 # int | Number of messages to take (default: 10, max: 25) (optional)

    try:
        # Get messages from a mailbox
        api_response = api_instance.get_messages(key, skip=skip, take=take)
        print("The response of MessagesApi->get_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Mailbox key | 
 **skip** | **int**| Number of messages to skip (default: 0) | [optional] 
 **take** | **int**| Number of messages to take (default: 10, max: 25) | [optional] 

### Return type

[**MessagesViewModel**](MessagesViewModel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_message**
> MessageViewModel get_single_message(key)

Get single message from mailbox

Retrieves a single message from the specified mailbox. Fails if mailbox contains 0 or more than 1 message.

### Example

* Api Key Authentication (ApiKey):

```python
import devinbox_client
from devinbox_client.models.message_view_model import MessageViewModel
from devinbox_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.devinbox.io
# See configuration.py for a list of all supported configuration parameters.
configuration = devinbox_client.Configuration(
    host = "https://api.devinbox.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with devinbox_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devinbox_client.MessagesApi(api_client)
    key = 'key_example' # str | Mailbox key

    try:
        # Get single message from mailbox
        api_response = api_instance.get_single_message(key)
        print("The response of MessagesApi->get_single_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_single_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Mailbox key | 

### Return type

[**MessageViewModel**](MessageViewModel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_message_with_template**
> MessageParsedViewModel get_single_message_with_template(key, template)

Get single message with template parsing

Retrieves a single message from the specified mailbox and parses it using the specified template. Fails if mailbox contains 0 or more than 1 message.

### Example

* Api Key Authentication (ApiKey):

```python
import devinbox_client
from devinbox_client.models.message_parsed_view_model import MessageParsedViewModel
from devinbox_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.devinbox.io
# See configuration.py for a list of all supported configuration parameters.
configuration = devinbox_client.Configuration(
    host = "https://api.devinbox.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with devinbox_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = devinbox_client.MessagesApi(api_client)
    key = 'key_example' # str | Mailbox key
    template = 'template_example' # str | Template name for parsing the message

    try:
        # Get single message with template parsing
        api_response = api_instance.get_single_message_with_template(key, template)
        print("The response of MessagesApi->get_single_message_with_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_single_message_with_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Mailbox key | 
 **template** | **str**| Template name for parsing the message | 

### Return type

[**MessageParsedViewModel**](MessageParsedViewModel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

