# MessagesViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Mailbox unique identifier | 
**count** | [**MessagesViewModelCount**](MessagesViewModelCount.md) |  | 
**messages** | [**List[MessageViewModel]**](MessageViewModel.md) | Collection of message view models | 

## Example

```python
from devinbox_client.models.messages_view_model import MessagesViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of MessagesViewModel from a JSON string
messages_view_model_instance = MessagesViewModel.from_json(json)
# print the JSON string representation of the object
print(MessagesViewModel.to_json())

# convert the object into a dict
messages_view_model_dict = messages_view_model_instance.to_dict()
# create an instance of MessagesViewModel from a dict
messages_view_model_from_dict = MessagesViewModel.from_dict(messages_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


