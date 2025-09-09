# devinbox_client.MailboxesApi

All URIs are relative to *https://api.devinbox.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mailbox**](MailboxesApi.md#create_mailbox) | **POST** /mailboxes | Create a new mailbox


# **create_mailbox**
> MailboxViewModel create_mailbox(body)

Create a new mailbox

Creates a new temporary or named mailbox for receiving test emails

### Example

* Api Key Authentication (ApiKey):

```python
import devinbox_client
from devinbox_client.models.mailbox_create_model import MailboxCreateModel
from devinbox_client.models.mailbox_view_model import MailboxViewModel
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
    api_instance = devinbox_client.MailboxesApi(api_client)
    body = devinbox_client.MailboxCreateModel() # MailboxCreateModel | Mailbox creation parameters

    try:
        # Create a new mailbox
        api_response = api_instance.create_mailbox(body)
        print("The response of MailboxesApi->create_mailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->create_mailbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MailboxCreateModel**](MailboxCreateModel.md)| Mailbox creation parameters | 

### Return type

[**MailboxViewModel**](MailboxViewModel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

