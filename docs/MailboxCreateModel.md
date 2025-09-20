# MailboxCreateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 

## Example

```python
from devinbox_client.models.mailbox_create_model import MailboxCreateModel

# TODO update the JSON string below
json = "{}"
# create an instance of MailboxCreateModel from a JSON string
mailbox_create_model_instance = MailboxCreateModel.from_json(json)
# print the JSON string representation of the object
print(MailboxCreateModel.to_json())

# convert the object into a dict
mailbox_create_model_dict = mailbox_create_model_instance.to_dict()
# create an instance of MailboxCreateModel from a dict
mailbox_create_model_from_dict = MailboxCreateModel.from_dict(mailbox_create_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


