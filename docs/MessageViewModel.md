# MessageViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** |  | [optional] 
**var_from** | **List[str]** |  | [optional] 
**to** | **List[str]** |  | [optional] 
**cc** | **List[str]** |  | [optional] 
**bcc** | **List[str]** |  | [optional] 
**subject** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**is_html** | **bool** |  | [optional] 
**received** | **datetime** |  | [optional] 

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


