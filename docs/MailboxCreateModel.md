# MailboxCreateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Optional name for the mailbox. If not provided, a temporary mailbox will be created. | [optional] 
**project_name** | **str** | Name of the project to associate the mailbox with. If not provided, uses the default project. | [optional] 
**is_temporary** | **bool** | Whether the mailbox should be temporary or persistent. | [optional] [default to True]

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


