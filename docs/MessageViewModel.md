# MessageViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** | Unique identifier for the message | 
**var_from** | **List[str]** | Array of sender email addresses | 
**to** | **List[str]** | Array of recipient email addresses | 
**cc** | **List[str]** | Array of CC email addresses | 
**bcc** | **List[str]** | Array of BCC email addresses | 
**subject** | **str** | Email subject line | 
**body** | **str** | Email body content | 
**is_html** | **bool** | Whether the email body is HTML format | 
**received** | **datetime** | Timestamp when the message was received | 

## Example

```python
from devinbox_client.models.message_view_model import MessageViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of MessageViewModel from a JSON string
message_view_model_instance = MessageViewModel.from_json(json)
# print the JSON string representation of the object
print(MessageViewModel.to_json())

# convert the object into a dict
message_view_model_dict = message_view_model_instance.to_dict()
# create an instance of MessageViewModel from a dict
message_view_model_from_dict = MessageViewModel.from_dict(message_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


