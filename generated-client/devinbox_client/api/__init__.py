# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from devinbox_client.api.mailboxes_api import MailboxesApi
    from devinbox_client.api.messages_api import MessagesApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from devinbox_client.api.mailboxes_api import MailboxesApi
from devinbox_client.api.messages_api import MessagesApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
