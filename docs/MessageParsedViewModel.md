# MessageParsedViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** | Unique identifier for the message | 
**var_from** | **List[str]** | Array of sender email addresses | 
**to** | **List[str]** | Array of recipient email addresses | 
**cc** | **List[str]** | Array of CC email addresses | 
**bcc** | **List[str]** | Array of BCC email addresses | 
**subject** | [**none_type[str, str]**](.md) | Parsed subject template parameters | 
**body** | [**none_type[str, str]**](.md) | Parsed body template parameters | 
**is_html** | **bool** | Whether the email body is HTML format | 
**received** | **datetime** | Timestamp when the message was received | 

## Example

```python
from devinbox_client.models.message_parsed_view_model import MessageParsedViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of MessageParsedViewModel from a JSON string
message_parsed_view_model_instance = MessageParsedViewModel.from_json(json)
# print the JSON string representation of the object
print(MessageParsedViewModel.to_json())

# convert the object into a dict
message_parsed_view_model_dict = message_parsed_view_model_instance.to_dict()
# create an instance of MessageParsedViewModel from a dict
message_parsed_view_model_from_dict = MessageParsedViewModel.from_dict(message_parsed_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


