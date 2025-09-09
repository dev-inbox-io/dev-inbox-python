#!/usr/bin/env python3
"""
DevInbox Python Client - Simple Usage Example
Demonstrates basic usage of the DevInbox API client
"""

import sys
import os
import getpass

# Add the current directory to Python path so we can import the client
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from devinbox_client.api.mailboxes_api import MailboxesApi
    from devinbox_client.api.messages_api import MessagesApi
    from devinbox_client.models.mailbox_create_model import MailboxCreateModel
    from devinbox_client.configuration import Configuration
    from devinbox_client.api_client import ApiClient
except ImportError as e:
    print("❌ Error importing DevInbox client. Please install it first:")
    print("   pip install -e .")
    print(f"   Import error: {e}")
    sys.exit(1)


def get_api_key():
    """Get API key from user input"""
    print("DevInbox Python Client - Usage Example")
    print("=" * 50)
    print("Please provide your DevInbox API key.")
    print("You can find it in your DevInbox dashboard at https://devinbox.io")
    print()
    
    while True:
        api_key = getpass.getpass("Enter your API key: ").strip()
        if api_key:
            return api_key
        print("❌ API key cannot be empty. Please try again.")


def main():
    """Main function demonstrating basic usage"""
    
    # Get API key from user
    api_key = get_api_key()
    
    print(f"\n🔧 Configuring API client with key: {api_key[:8]}...")
    
    # 1. Configure the API client
    configuration = Configuration(
        host="https://api.devinbox.io",
    )
    configuration.api_key['ApiKey'] = api_key
    
    # Create API client instance
    api_client = ApiClient(configuration)
    
    # Initialize API instances
    mailboxes_api = MailboxesApi(api_client)
    messages_api = MessagesApi(api_client)
    
    print("✅ API client configured successfully!")
    
    try:
        # 2. Create a temporary mailbox
        print("\n📧 Creating a temporary mailbox...")
        temp_mailbox = MailboxCreateModel()
        temp_response = mailboxes_api.create_mailbox(body=temp_mailbox.to_dict())
        print(f"   ✅ Temporary mailbox created!")
        print(f"   📋 Key: {temp_response.key}")
        print(f"   🔑 Password: {temp_response.password}")
        
        mailbox_key = temp_response.key
        
        # 3. Check message count
        print(f"\n📊 Checking message count for mailbox: {mailbox_key}")
        count_response = messages_api.get_message_count(key=mailbox_key)
        print(f"   ✅ Message count: {count_response.count}")
        
        # 4. Get messages with pagination
        print(f"\n📋 Getting messages with pagination...")
        messages_response = messages_api.get_messages(
            key=mailbox_key,
            skip=0,    # Skip first 0 messages
            take=10    # Take up to 10 messages
        )
        print(f"   ✅ Retrieved {len(messages_response.messages)} messages")
        
        # 5. Show how to use other endpoints (will fail gracefully for empty mailbox)
        print(f"\n📄 Other available endpoints (will fail gracefully for empty mailbox):")
        
        endpoints_to_demo = [
            ("get_single_message", lambda: messages_api.get_single_message(key=mailbox_key)),
            ("get_last_message", lambda: messages_api.get_last_message(key=mailbox_key)),
            ("get_single_message_with_template", lambda: messages_api.get_single_message_with_template(key=mailbox_key, template="test")),
            ("get_last_message_with_template", lambda: messages_api.get_last_message_with_template(key=mailbox_key, template="test")),
            ("get_message_by_id", lambda: messages_api.get_message_by_id(key=mailbox_key, id="00000000-0000-0000-0000-000000000000")),
        ]
        
        for endpoint_name, endpoint_func in endpoints_to_demo:
            try:
                result = endpoint_func()
                print(f"   ⚠️  {endpoint_name}: Unexpected success - {result}")
            except Exception as e:
                print(f"   ✅ {endpoint_name}: Expected failure - {type(e).__name__}")
        
        print("\n" + "=" * 50)
        print("✅ Example completed successfully!")
        print("\n🎯 Available endpoints in the DevInbox Python client:")
        print("  📧 Mailboxes:")
        print("     - create_mailbox() - Create temporary or named mailboxes")
        print("  📨 Messages:")
        print("     - get_message_count() - Count messages")
        print("     - get_messages() - List messages with pagination")
        print("     - get_single_message() - Get single message")
        print("     - get_single_message_with_template() - Get single with template")
        print("     - get_last_message() - Get most recent message")
        print("     - get_last_message_with_template() - Get last with template")
        print("     - get_message_by_id() - Get message by ID")
        print("\n🚀 The DevInbox Python client is ready to use!")
        
    except Exception as e:
        print(f"\n❌ Example failed with error: {e}")
        print(f"Error type: {type(e).__name__}")
        
        # Try to get more details about the error
        if hasattr(e, 'status'):
            print(f"HTTP Status: {e.status}")
        if hasattr(e, 'reason'):
            print(f"Reason: {e.reason}")
        if hasattr(e, 'body'):
            print(f"Response body: {e.body}")
        
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Example interrupted by user.")
        sys.exit(1)
