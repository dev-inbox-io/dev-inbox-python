# MessageViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** | Unique message identifier | 
**var_from** | **List[str]** | Message sender addresses | [optional] 
**to** | **List[str]** | Message recipient addresses | [optional] 
**cc** | **List[str]** | Message CC addresses | [optional] 
**bcc** | **List[str]** | Message BCC addresses | [optional] 
**subject** | **str** | Message subject | [optional] 
**body** | **str** | Message body content | [optional] 
**is_html** | **bool** | Whether the message body is HTML | [optional] 
**received** | **datetime** | When the message was received | 

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


