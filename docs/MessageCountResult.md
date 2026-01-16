# MessageCountResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Mailbox unique identifier | 
**count** | [**MessageCountResultCount**](MessageCountResultCount.md) |  | 

## Example

```python
from devinbox_client.models.message_count_result import MessageCountResult

# TODO update the JSON string below
json = "{}"
# create an instance of MessageCountResult from a JSON string
message_count_result_instance = MessageCountResult.from_json(json)
# print the JSON string representation of the object
print(MessageCountResult.to_json())

# convert the object into a dict
message_count_result_dict = message_count_result_instance.to_dict()
# create an instance of MessageCountResult from a dict
message_count_result_from_dict = MessageCountResult.from_dict(message_count_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


