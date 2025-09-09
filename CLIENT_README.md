# DevInbox Python Client

A complete Python client for the DevInbox API, generated from the OpenAPI specification.

## Features

✅ **Complete API Coverage** - All 8 endpoints available:
- 📧 **Mailboxes**: Create temporary or named mailboxes
- 📨 **Messages**: Full message management with 7 different endpoints

✅ **All Message Endpoints**:
- `get_message_count()` - Get number of messages in mailbox
- `get_messages()` - Get messages with pagination
- `get_single_message()` - Get single message (if exactly 1)
- `get_single_message_with_template()` - Get single message with template parsing
- `get_last_message()` - Get most recent message
- `get_last_message_with_template()` - Get last message with template parsing
- `get_message_by_id()` - Get specific message by ID

## Installation

```bash
# Install the client in development mode
pip install -e .

# Or install dependencies only
pip install -r requirements.txt
```

## Quick Start

### 1. Basic Usage

```python
from devinbox_client.api.mailboxes_api import MailboxesApi
from devinbox_client.api.messages_api import MessagesApi
from devinbox_client.models.mailbox_create_model import MailboxCreateModel
from devinbox_client.configuration import Configuration
from devinbox_client.api_client import ApiClient

# Configure the API client
configuration = Configuration(host="https://api.devinbox.io")
configuration.api_key['ApiKey'] = "your-api-key-here"

# Create API client instance
api_client = ApiClient(configuration)
mailboxes_api = MailboxesApi(api_client)
messages_api = MessagesApi(api_client)

# Create a temporary mailbox
temp_mailbox = MailboxCreateModel()
response = mailboxes_api.create_mailbox(body=temp_mailbox.to_dict())
print(f"Mailbox created: {response.key}")

# Get message count
count = messages_api.get_message_count(key=response.key)
print(f"Message count: {count.count}")

# Get messages with pagination
messages = messages_api.get_messages(key=response.key, skip=0, take=10)
print(f"Retrieved {len(messages.messages)} messages")
```

### 2. Set Environment Variable

```bash
# Windows
set DEVINBOX_API_KEY=your-api-key-here

# Linux/Mac
export DEVINBOX_API_KEY=your-api-key-here
```

### 3. Run Examples

```bash
# Run the comprehensive test script (uses DEVINBOX_API_KEY env var)
python test_all_endpoints.py

# Run the simple usage example (prompts for API key)
python example_usage.py
```

## API Endpoints

### Mailboxes

#### Create Mailbox
```python
# Temporary mailbox (no name)
temp_mailbox = MailboxCreateModel()
response = mailboxes_api.create_mailbox(body=temp_mailbox.to_dict())

# Named mailbox
named_mailbox = MailboxCreateModel(
    name="my-test-mailbox",
    project_name="my-project"
)
response = mailboxes_api.create_mailbox(body=named_mailbox.to_dict())
```

### Messages

#### Get Message Count
```python
count = messages_api.get_message_count(key="your-mailbox-key")
print(f"Messages: {count.count}")
```

#### Get Messages with Pagination
```python
messages = messages_api.get_messages(
    key="your-mailbox-key",
    skip=0,    # Skip first 0 messages
    take=10    # Take up to 10 messages
)
```

#### Get Single Message
```python
# Only works if mailbox has exactly 1 message
message = messages_api.get_single_message(key="your-mailbox-key")
```

#### Get Last Message
```python
# Gets the most recent message
message = messages_api.get_last_message(key="your-mailbox-key")
```

#### Get Single Message with Template
```python
# Parses message using a template
message = messages_api.get_single_message_with_template(
    key="your-mailbox-key",
    template="your-template-name"
)
```

#### Get Last Message with Template
```python
# Gets last message and parses with template
message = messages_api.get_last_message_with_template(
    key="your-mailbox-key",
    template="your-template-name"
)
```

#### Get Message by ID
```python
# Get specific message by its unique ID
message = messages_api.get_message_by_id(
    key="your-mailbox-key",
    id="message-uuid-here"
)
```

## Error Handling

The client includes comprehensive error handling:

```python
try:
    message = messages_api.get_single_message(key="your-mailbox-key")
    print(f"Message: {message}")
except BadRequestException as e:
    print(f"Bad request: {e}")
except NotFoundException as e:
    print(f"Not found: {e}")
except UnauthorizedException as e:
    print(f"Unauthorized: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Data Models

The client includes complete data models:

- `MailboxCreateModel` - For creating mailboxes
- `MailboxViewModel` - Mailbox response data
- `MessageCountResult` - Message count response
- `MessageViewModel` - Basic message data
- `MessageParsedViewModel` - Message with template parameters
- `MessagesViewModel` - Paginated messages response

## Authentication

The client uses API key authentication via the `X-API-Key` header:

```python
configuration.api_key['ApiKey'] = "your-api-key-here"
```

## Testing

Run the comprehensive test to verify all endpoints:

```bash
# Set your API key first
set DEVINBOX_API_KEY=your-api-key-here  # Windows
# export DEVINBOX_API_KEY=your-api-key-here  # Linux/Mac

# Run the test
python test_all_endpoints.py
```

This will test all 8 endpoints and provide a detailed report.

## Support

For issues or questions:
- Check the [DevInbox documentation](https://devinbox.io)
- Review the generated API documentation in the `docs/` folder
- Run the test scripts to verify functionality

## License

This client is generated from the DevInbox API specification and follows the same terms as the DevInbox service.
