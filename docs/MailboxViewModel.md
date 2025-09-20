# MailboxViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from devinbox_client.models.mailbox_view_model import MailboxViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of MailboxViewModel from a JSON string
mailbox_view_model_instance = MailboxViewModel.from_json(json)
# print the JSON string representation of the object
print(MailboxViewModel.to_json())

# convert the object into a dict
mailbox_view_model_dict = mailbox_view_model_instance.to_dict()
# create an instance of MailboxViewModel from a dict
mailbox_view_model_from_dict = MailboxViewModel.from_dict(mailbox_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


