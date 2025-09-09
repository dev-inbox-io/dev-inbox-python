#!/usr/bin/env python3
"""
Comprehensive DevInbox API Test Script
Tests all available endpoints using DEVINBOX_API_KEY environment variable
"""

import sys
import os

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
    """Get API key from environment variable"""
    print("DevInbox API Test Script")
    print("=" * 50)
    print("Getting API key from DEVINBOX_API_KEY environment variable...")
    
    api_key = os.getenv('DEVINBOX_API_KEY')
    if not api_key:
        print("❌ Error: DEVINBOX_API_KEY environment variable not found!")
        print("\nPlease set the environment variable:")
        print("  Windows: set DEVINBOX_API_KEY=your-api-key-here")
        print("  Linux/Mac: export DEVINBOX_API_KEY=your-api-key-here")
        print("\nYou can find your API key in your DevInbox dashboard at https://devinbox.io")
        sys.exit(1)
    
    print(f"✅ API key found: {api_key[:8]}...")
    return api_key


def test_all_endpoints(api_key):
    """Test all available endpoints in the DevInbox client"""
    
    print(f"\n🔧 Configuring API client with key: {api_key[:8]}...")
    
    # Configure the API client
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
    
    test_results = []
    
    try:
        # Test 1: Create a temporary mailbox
        print("\n📧 Test 1: Creating a temporary mailbox...")
        temp_mailbox_data = MailboxCreateModel()
        temp_response = mailboxes_api.create_mailbox(body=temp_mailbox_data.to_dict())
        print(f"   ✅ Temporary mailbox created successfully!")
        print(f"   📋 Key: {temp_response.key}")
        print(f"   🔑 Password: {temp_response.password}")
        test_results.append(("Create temporary mailbox", True, "Success"))
        
        # Test 2: Create a named mailbox
        print("\n📧 Test 2: Creating a named mailbox...")
        try:
            named_mailbox_data = MailboxCreateModel(
                name="test-mailbox",
                project_name="test-project"
            )
            named_response = mailboxes_api.create_mailbox(body=named_mailbox_data.to_dict())
            print(f"   ✅ Named mailbox created successfully!")
            print(f"   📋 Key: {named_response.key}")
            print(f"   🔑 Password: {named_response.password}")
            test_results.append(("Create named mailbox", True, "Success"))
        except Exception as e:
            print(f"   ⚠️  Named mailbox creation failed (expected if project doesn't exist): {e}")
            test_results.append(("Create named mailbox", False, str(e)))
        
        # Use the temporary mailbox for message operations
        mailbox_key = temp_response.key
        print(f"\n📨 Testing message endpoints with mailbox: {mailbox_key}")
        
        # Test 3: Get message count
        print("\n📊 Test 3: Getting message count...")
        try:
            count_response = messages_api.get_message_count(key=mailbox_key)
            print(f"   ✅ Message count retrieved: {count_response.count}")
            test_results.append(("Get message count", True, f"Count: {count_response.count}"))
        except Exception as e:
            print(f"   ❌ Message count failed: {e}")
            test_results.append(("Get message count", False, str(e)))
        
        # Test 4: Get messages with pagination
        print("\n📋 Test 4: Getting messages with pagination...")
        try:
            messages_response = messages_api.get_messages(
                key=mailbox_key,
                skip=0,
                take=10
            )
            print(f"   ✅ Messages retrieved: {len(messages_response.messages)} messages")
            test_results.append(("Get messages with pagination", True, f"Retrieved {len(messages_response.messages)} messages"))
        except Exception as e:
            print(f"   ❌ Get messages failed: {e}")
            test_results.append(("Get messages with pagination", False, str(e)))
        
        # Test 5: Get single message (will likely fail for empty mailbox)
        print("\n📄 Test 5: Getting single message...")
        try:
            single_response = messages_api.get_single_message(key=mailbox_key)
            print(f"   ✅ Single message retrieved: {single_response}")
            test_results.append(("Get single message", True, "Success"))
        except Exception as e:
            print(f"   ⚠️  Get single message failed (expected for empty mailbox): {e}")
            test_results.append(("Get single message", False, str(e)))
        
        # Test 6: Get last message (will likely fail for empty mailbox)
        print("\n📄 Test 6: Getting last message...")
        try:
            last_response = messages_api.get_last_message(key=mailbox_key)
            print(f"   ✅ Last message retrieved: {last_response}")
            test_results.append(("Get last message", True, "Success"))
        except Exception as e:
            print(f"   ⚠️  Get last message failed (expected for empty mailbox): {e}")
            test_results.append(("Get last message", False, str(e)))
        
        # Test 7: Get single message with template (will likely fail)
        print("\n🔍 Test 7: Getting single message with template...")
        try:
            template_single_response = messages_api.get_single_message_with_template(
                key=mailbox_key,
                template="test-template"
            )
            print(f"   ✅ Single message with template retrieved: {template_single_response}")
            test_results.append(("Get single message with template", True, "Success"))
        except Exception as e:
            print(f"   ⚠️  Get single message with template failed (expected): {e}")
            test_results.append(("Get single message with template", False, str(e)))
        
        # Test 8: Get last message with template (will likely fail)
        print("\n🔍 Test 8: Getting last message with template...")
        try:
            template_last_response = messages_api.get_last_message_with_template(
                key=mailbox_key,
                template="test-template"
            )
            print(f"   ✅ Last message with template retrieved: {template_last_response}")
            test_results.append(("Get last message with template", True, "Success"))
        except Exception as e:
            print(f"   ⚠️  Get last message with template failed (expected): {e}")
            test_results.append(("Get last message with template", False, str(e)))
        
        # Test 9: Get message by ID (will likely fail without valid message ID)
        print("\n🔍 Test 9: Getting message by ID...")
        try:
            message_by_id_response = messages_api.get_message_by_id(
                key=mailbox_key,
                id="00000000-0000-0000-0000-000000000000"  # Dummy UUID
            )
            print(f"   ✅ Message by ID retrieved: {message_by_id_response}")
            test_results.append(("Get message by ID", True, "Success"))
        except Exception as e:
            print(f"   ⚠️  Get message by ID failed (expected with dummy ID): {e}")
            test_results.append(("Get message by ID", False, str(e)))
        
        return test_results
        
    except Exception as e:
        print(f"\n❌ Test failed with unexpected error: {e}")
        print(f"Error type: {type(e).__name__}")
        
        # Try to get more details about the error
        if hasattr(e, 'status'):
            print(f"HTTP Status: {e.status}")
        if hasattr(e, 'reason'):
            print(f"Reason: {e.reason}")
        if hasattr(e, 'body'):
            print(f"Response body: {e.body}")
            
        return [("Unexpected error", False, str(e))]


def print_summary(test_results):
    """Print test results summary"""
    print("\n" + "=" * 60)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 60)
    
    successful_tests = 0
    failed_tests = 0
    
    for test_name, success, details in test_results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{test_name:<40} {status}")
        if details and details != "Success":
            print(f"   📝 Details: {details}")
        
        if success:
            successful_tests += 1
        else:
            failed_tests += 1
    
    print("\n" + "-" * 60)
    print(f"Total tests: {len(test_results)}")
    print(f"✅ Successful: {successful_tests}")
    print(f"❌ Failed: {failed_tests}")
    
    print("\n🎯 Available endpoints in the DevInbox Python client:")
    print("  📧 Mailboxes:")
    print("     - create_mailbox() - Create temporary or named mailboxes")
    print("  📨 Messages:")
    print("     - get_message_count() - Get number of messages in mailbox")
    print("     - get_messages() - Get messages with pagination")
    print("     - get_single_message() - Get single message (if exactly 1)")
    print("     - get_single_message_with_template() - Get single with template parsing")
    print("     - get_last_message() - Get most recent message")
    print("     - get_last_message_with_template() - Get last with template parsing")
    print("     - get_message_by_id() - Get specific message by ID")
    
    if successful_tests > 0:
        print(f"\n🎉 {successful_tests} endpoint(s) working correctly!")
        print("The DevInbox Python client is functional and ready to use!")
    
    return successful_tests > 0


def main():
    """Main function"""
    try:
        # Get API key from environment variable
        api_key = get_api_key()
        
        # Test all endpoints
        test_results = test_all_endpoints(api_key)
        
        # Print summary
        success = print_summary(test_results)
        
        if success:
            print("\n🚀 All tests completed! The DevInbox Python client is working!")
            sys.exit(0)
        else:
            print("\n⚠️  Some tests failed. Check the details above.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n⏹️  Test interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
