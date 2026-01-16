# devinbox_client.MessagesApi

All URIs are relative to *http://localhost:5062*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_last_message**](MessagesApi.md#get_last_message) | **GET** /messages/{key}/last | Get the last message from a mailbox
[**get_last_message_with_template**](MessagesApi.md#get_last_message_with_template) | **GET** /messages/{key}/{template}/last | Get the last message with template parsing
[**get_message_by_id**](MessagesApi.md#get_message_by_id) | **GET** /messages/{key}/get | Get a specific message by ID
[**get_message_count**](MessagesApi.md#get_message_count) | **GET** /messages/{key}/count | Get message count for a mailbox
[**get_messages**](MessagesApi.md#get_messages) | **GET** /messages/{key} | Get messages from a mailbox
[**get_single_message**](MessagesApi.md#get_single_message) | **GET** /messages/{key}/single | Get single message from a mailbox
[**get_single_message_with_template**](MessagesApi.md#get_single_message_with_template) | **GET** /messages/{key}/{template}/single | Get single message with template parsing


# **get_last_message**
> MessageViewModel get_last_message(key)

Get the last message from a mailbox

Retrieves the most recent message from the specified mailbox. Returns an error if the mailbox is empty.

### Example


```python
import devinbox_client
from devinbox_client.models.message_view_model import MessageViewModel
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
    api_instance = devinbox_client.MessagesApi(api_client)
    key = 'key_example' # str | 

    try:
        # Get the last message from a mailbox
        api_response = api_instance.get_last_message(key)
        print("The response of MessagesApi->get_last_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_last_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

[**MessageViewModel**](MessageViewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_message_with_template**
> MessageParsedViewModel get_last_message_with_template(key, template)

Get the last message with template parsing

Retrieves the most recent message from the specified mailbox and parses it using the provided template. Returns an error if the mailbox is empty.

### Example


```python
import devinbox_client
from devinbox_client.models.message_parsed_view_model import MessageParsedViewModel
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
    api_instance = devinbox_client.MessagesApi(api_client)
    key = 'key_example' # str | 
    template = 'template_example' # str | 

    try:
        # Get the last message with template parsing
        api_response = api_instance.get_last_message_with_template(key, template)
        print("The response of MessagesApi->get_last_message_with_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_last_message_with_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 
 **template** | **str**|  | 

### Return type

[**MessageParsedViewModel**](MessageParsedViewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_by_id**
> MessageViewModel get_message_by_id(key, id)

Get a specific message by ID

Retrieves a specific message from the specified mailbox using its unique ID.

### Example


```python
import devinbox_client
from devinbox_client.models.message_view_model import MessageViewModel
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
    api_instance = devinbox_client.MessagesApi(api_client)
    key = 'key_example' # str | 
    id = 'id_example' # str | 

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
 **key** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**MessageViewModel**](MessageViewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_count**
> MessageCountResult get_message_count(key)

Get message count for a mailbox

Returns the total number of messages in the specified mailbox.

### Example


```python
import devinbox_client
from devinbox_client.models.message_count_result import MessageCountResult
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
    api_instance = devinbox_client.MessagesApi(api_client)
    key = 'key_example' # str | 

    try:
        # Get message count for a mailbox
        api_response = api_instance.get_message_count(key)
        print("The response of MessagesApi->get_message_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_message_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

[**MessageCountResult**](MessageCountResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages**
> MessagesViewModel get_messages(key, skip=skip, take=take)

Get messages from a mailbox

Retrieves messages from the specified mailbox with optional pagination. Default: skip=0, take=10, max take=25.

### Example


```python
import devinbox_client
from devinbox_client.models.messages_view_model import MessagesViewModel
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
    api_instance = devinbox_client.MessagesApi(api_client)
    key = 'key_example' # str | 
    skip = devinbox_client.GetMessagesSkipParameter() # GetMessagesSkipParameter |  (optional)
    take = devinbox_client.GetMessagesSkipParameter() # GetMessagesSkipParameter |  (optional)

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
 **key** | **str**|  | 
 **skip** | **GetMessagesSkipParameter**|  | [optional] 
 **take** | **GetMessagesSkipParameter**|  | [optional] 

### Return type

[**MessagesViewModel**](MessagesViewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_message**
> MessageViewModel get_single_message(key)

Get single message from a mailbox

Retrieves a single message from the specified mailbox. Returns an error if the mailbox contains 0 or more than 1 message.

### Example


```python
import devinbox_client
from devinbox_client.models.message_view_model import MessageViewModel
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
    api_instance = devinbox_client.MessagesApi(api_client)
    key = 'key_example' # str | 

    try:
        # Get single message from a mailbox
        api_response = api_instance.get_single_message(key)
        print("The response of MessagesApi->get_single_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_single_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

[**MessageViewModel**](MessageViewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_message_with_template**
> MessageParsedViewModel get_single_message_with_template(key, template)

Get single message with template parsing

Retrieves a single message from the specified mailbox and parses it using the provided template. Returns an error if the mailbox contains 0 or more than 1 message.

### Example


```python
import devinbox_client
from devinbox_client.models.message_parsed_view_model import MessageParsedViewModel
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
    api_instance = devinbox_client.MessagesApi(api_client)
    key = 'key_example' # str | 
    template = 'template_example' # str | 

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
 **key** | **str**|  | 
 **template** | **str**|  | 

### Return type

[**MessageParsedViewModel**](MessageParsedViewModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

