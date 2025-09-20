# MessageParsedViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **str** |  | [optional] 
**var_from** | **List[str]** |  | [optional] 
**to** | **List[str]** |  | [optional] 
**cc** | **List[str]** |  | [optional] 
**bcc** | **List[str]** |  | [optional] 
**subject** | **Dict[str, str]** |  | [optional] 
**body** | **Dict[str, str]** |  | [optional] 
**is_html** | **bool** |  | [optional] 
**received** | **datetime** |  | [optional] 

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


