# devinbox_client.MailboxesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mailbox**](MailboxesApi.md#create_mailbox) | **POST** /mailboxes | Create a new mailbox


# **create_mailbox**
> MailboxViewModel create_mailbox(mailbox_create_model)

Create a new mailbox

Creates a new mailbox for receiving test emails. If no name is provided, a temporary mailbox is created.

### Example

* Api Key Authentication (ApiKey):

```python
import devinbox_client
from devinbox_client.models.mailbox_create_model import MailboxCreateModel
from devinbox_client.models.mailbox_view_model import MailboxViewModel
from devinbox_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = devinbox_client.Configuration(
    host = "http://localhost"
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
    mailbox_create_model = devinbox_client.MailboxCreateModel() # MailboxCreateModel | 

    try:
        # Create a new mailbox
        api_response = api_instance.create_mailbox(mailbox_create_model)
        print("The response of MailboxesApi->create_mailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailboxesApi->create_mailbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_create_model** | [**MailboxCreateModel**](MailboxCreateModel.md)|  | 

### Return type

[**MailboxViewModel**](MailboxViewModel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

