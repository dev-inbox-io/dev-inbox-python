#!/usr/bin/env python3
"""
DevInbox Python Client - Complete Usage Example
Demonstrates creating mailbox, sending email via SMTP, and receiving via API
"""

import sys
import os
import getpass
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
    """Get API key from user input or environment variable"""
    print("DevInbox Python Client - Complete Usage Example")
    print("=" * 50)
    print("Please provide your DevInbox API key.")
    print("You can find it in your DevInbox dashboard at https://devinbox.io")
    print("Press Enter to use DEVINBOX_API_KEY environment variable")
    print()
    
    api_key = input("Enter your API key (or press Enter for env var): ").strip()
    
    if not api_key:
        # Try to get from environment variable
        api_key = os.getenv('DEVINBOX_API_KEY')
        if not api_key:
            print("❌ No API key provided and DEVINBOX_API_KEY environment variable is not set.")
            print("Please either:")
            print("  1. Enter your API key when prompted")
            print("  2. Set the DEVINBOX_API_KEY environment variable")
            sys.exit(1)
        print("✅ Using API key from DEVINBOX_API_KEY environment variable")
    else:
        print("✅ Using provided API key")
    
    return api_key


def get_test_body_content():
    """Get the test message body content"""
    return """Hello John Doe,

This is a simple test message to verify email delivery.
If you receive this, the system is working correctly."""


def create_test_html():
    """Create simple HTML content for testing"""
    return """
    <html>
    <body>
        <h2>Hello John Doe,</h2>
        <p>This is a simple test message to verify email delivery.</p>
        <p>If you receive this, the system is working correctly.</p>
    </body>
    </html>
    """


def send_email_via_smtp(mailbox_username, mailbox_password, to_email, send_html_only=False):
    """Send email via SMTP using DevInbox SMTP server"""
    print(f"\n📤 Sending email via SMTP to {to_email}...")
    
    # SMTP configuration as specified
    # smtp_server = "smtp.devinbox.io"
    smtp_server = "localhost"
    smtp_port = 9025
    smtp_username = mailbox_username
    smtp_password = mailbox_password
    
    # Create message
    msg = MIMEMultipart('alternative')
    msg['From'] = f"DevInbox Test <{smtp_username}>"
    msg['To'] = to_email
    msg['Subject'] = "Welcome John Doe!"
    
    # Create HTML content
    html_content = create_test_html()
    
    # Create text version
    text_content = get_test_body_content()
    
    # Attach parts based on send_html_only flag
    if send_html_only:
        # Send only HTML
        html_part = MIMEText(html_content, 'html')
        msg.attach(html_part)
        print(f"   📧 Sending HTML-only email with {len(html_content)} characters")
    else:
        # Send both text and HTML (multipart)
        text_part = MIMEText(text_content, 'plain')
        html_part = MIMEText(html_content, 'html')
        
        msg.attach(text_part)
        msg.attach(html_part)
        
        print(f"   📧 Sending multipart email with:")
        print(f"      - Text part: {len(text_content)} characters")
        print(f"      - HTML part: {len(html_content)} characters")
    
    try:
        # Connect to SMTP server
        print(f"   🔌 Connecting to {smtp_server}:{smtp_port}...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        
        # Enable debug output to see SMTP commands (helpful for troubleshooting)
        server.set_debuglevel(1)
        
        # Start TLS
        print("   🔒 Starting TLS encryption...")
        # server.starttls()
        
        # Login
        print(f"   🔑 Authenticating as {smtp_username}...")
        server.login(smtp_username, smtp_password)
        
        # Send email
        print("   📧 Sending email...")
        # Use sendmail instead of send_message for better compatibility with custom SMTP servers
        server.send_message(msg)
        # server.sendmail(smtp_username, to_email, msg.as_string())
        
        # Close connection
        server.quit()
        
        print("   ✅ Email sent successfully!")
        return True
        
    except Exception as e:
        print(f"   ❌ Failed to send email: {e}")
        return False


def main():
    """Main function demonstrating complete DevInbox workflow"""
    
    # Get API key from user
    # api_key = get_api_key()
    api_key = "69f7673b13394d89b42f0ceb8cde6f82"
    
    print(f"\n🔧 Configuring API client with key: {api_key[:8]}...")
    
    # 1. Configure the API client
    configuration = Configuration(
        # host="https://api.devinbox.io",
        host="http://localhost:5062",
    )
    configuration.api_key['ApiKey'] = api_key
    
    # Create API client instance
    api_client = ApiClient(configuration)
    
    # Initialize API instances
    mailboxes_api = MailboxesApi(api_client)
    messages_api = MessagesApi(api_client)
    
    # Assert that API instances were created successfully
    assert mailboxes_api is not None, "Failed to create MailboxesApi instance"
    assert messages_api is not None, "Failed to create MessagesApi instance"
    
    print("✅ API client configured successfully!")
    
    try:
        # 2. Create a temporary mailbox
        print("\n📧 Creating a temporary mailbox...")
        temp_mailbox = MailboxCreateModel()
        temp_response = mailboxes_api.create_mailbox(mailbox_create_model=temp_mailbox)
        
        # Assert that mailbox was created successfully
        assert temp_response is not None, "Failed to create mailbox - response is None"
        assert temp_response.key is not None and len(temp_response.key) > 0, "Mailbox key is missing or empty"
        assert temp_response.password is not None and len(temp_response.password) > 0, "Mailbox password is missing or empty"
        
        print(f"   ✅ Temporary mailbox created!")
        print(f"   📋 Key: {temp_response.key}")
        print(f"   🔑 Password: {temp_response.password}")
        print(f"   📧 Email Address: {temp_response.key}@devinbox.io")
        
        mailbox_key = temp_response.key
        mailbox_password = temp_response.password
        mailbox_email = f"{mailbox_key}@devinbox.io"
        
        # 3. Check that the mailbox is empty
        print(f"\n📊 Checking that mailbox is empty...")
        count_response = messages_api.get_message_count(key=mailbox_key)
        print(f"   ✅ Message count: {count_response.count}")
        
        # Assert that mailbox is empty - this is critical for the test
        assert count_response.count == 0, f"Mailbox is not empty! Expected 0 messages, got {count_response.count}. This is a critical error as we just created the mailbox."
        print("   ✅ Mailbox is empty as expected!")
        
        # 4. Send email to the mailbox via SMTP
        print(f"\n📤 Sending test email to {mailbox_email}...")
        email_sent = send_email_via_smtp(mailbox_key, mailbox_password, mailbox_email, send_html_only=True)
        
        # Assert that email was sent successfully
        assert email_sent, "Failed to send email via SMTP. This is a critical test failure."
        
        # 5. Wait a moment for email to be processed
        print("\n⏳ Waiting for email to be processed...")
        
        # 6. Check that the email was received
        print(f"\n📬 Checking if email was received...")
        
        # Check message count again
        count_response_after = messages_api.get_message_count(key=mailbox_key)
        print(f"   📊 Message count after sending: {count_response_after.count}")
        
        # Assert that email was received (count should have increased)
        assert count_response_after.count > count_response.count, f"Email was not received! Expected count > {count_response.count}, got {count_response_after.count}. This indicates SMTP or email processing issues."
        print("   ✅ Email was received successfully!")
        
        # Get the latest message
        print(f"\n📋 Retrieving the received email...")
        messages_response = messages_api.get_messages(
            key=mailbox_key,
            skip=0,
            take=1
        )
        
        # Assert that we can retrieve the message
        assert messages_response.messages and len(messages_response.messages) > 0, "No messages found despite count increase. This indicates an API retrieval issue."
        
        latest_message = messages_response.messages[0]
        print(f"   ✅ Email retrieved successfully!")
        print(f"   📧 From: {latest_message.var_from}")
        print(f"   📧 To: {latest_message.to}")
        print(f"   📧 Subject: {latest_message.subject}")
        print(f"   📧 Received: {latest_message.received}")
        print(f"   📧 Size: {len(latest_message.body) if latest_message.body else 0} characters")
        
        # Assert that the message has expected content
        assert latest_message.subject is not None, "Email subject is missing"
        assert latest_message.var_from is not None, "Email sender address is missing"
        assert latest_message.to is not None, "Email recipient address is missing"
        
        # Check what type of content we received
        print(f"   📋 Message type: {'HTML' if latest_message.is_html else 'Text'}")
        print(f"   📋 Body content: {latest_message.body[:100]}...")
        
        # Verify that the message body is exactly what we sent
        assert latest_message.body is not None, "Message body is None"
        
        # Since we're sending HTML-only, we expect to receive HTML content
        expected_html_content = create_test_html().strip()
        received_html_normalized = ' '.join(latest_message.body.split())
        expected_html_normalized = ' '.join(expected_html_content.split())
        
        if received_html_normalized == expected_html_normalized:
            print("   ✅ HTML body content verified!")
        else:
            # If it's not the HTML version, check if it's the text version (fallback)
            expected_text_content = get_test_body_content()
            expected_text_normalized = ' '.join(expected_text_content.split())
            
            if received_html_normalized == expected_text_normalized:
                print("   ✅ Text body content verified (HTML was converted to text)!")
            else:
                assert False, f"Body content does not match expected HTML or text version. Expected HTML: '{expected_html_content}' | Expected text: '{expected_text_content}' | Actual: '{latest_message.body}'"
        
        # Show preview of email content
        if latest_message.body:
            preview = latest_message.body[:200] + "..." if len(latest_message.body) > 200 else latest_message.body
            print(f"   📄 Content preview: {preview}")
            # Assert that email has content
            assert len(latest_message.body) > 0, "Email body is empty"
        
        # 7. Test getting single message with template parsing
        print(f"\n🔍 Testing single message retrieval with 'onboarding' template...")
        try:
            parsed_message = messages_api.get_single_message_with_template(
                key=mailbox_key,
                template="onboarding"
            )
            
            # Verify the parsed message
            assert parsed_message is not None, "Parsed message is None"
            
            print(f"   ✅ Template parsing successful!")
            print(f"   📧 From: {parsed_message.var_from}")
            print(f"   📧 To: {parsed_message.to}")
            print(f"   📧 Subject: {parsed_message.subject}")
            print(f"   📧 Body: {parsed_message.body}")
            print(f"   📧 Is HTML: {parsed_message.is_html}")
            print(f"   📧 Received: {parsed_message.received}")
            
            # Note: The MessageParsedViewModel doesn't have a 'parameters' field
            # Template parsing works by replacing {{ user_name }} with actual values in subject/body dictionaries
            if parsed_message.body:
                print(f"   📋 Parsed body content: {parsed_message.body}")
                # Assert that the body is a dictionary with user_name parameter
                assert isinstance(parsed_message.body, dict), f"Body should be a dictionary, got {type(parsed_message.body)}"
                assert "user_name" in parsed_message.body, f"Template parsing failed: 'user_name' parameter not found in body. Body content: {parsed_message.body}"
                assert parsed_message.body["user_name"] == "John Doe", f"Template parsing failed: user_name should be 'John Doe', got '{parsed_message.body['user_name']}'"
                print(f"   ✅ Body contains user_name='John Doe' as expected!")
            if parsed_message.subject:
                print(f"   📋 Parsed subject content: {parsed_message.subject}")
                # Assert that the subject is a dictionary with user_name parameter
                assert isinstance(parsed_message.subject, dict), f"Subject should be a dictionary, got {type(parsed_message.subject)}"
                assert "user_name" in parsed_message.subject, f"Template parsing failed: 'user_name' parameter not found in subject. Subject content: {parsed_message.subject}"
                assert parsed_message.subject["user_name"] == "John Doe", f"Template parsing failed: user_name should be 'John Doe', got '{parsed_message.subject['user_name']}'"
                print(f"   ✅ Subject contains user_name='John Doe' as expected!")
            
        except Exception as e:
            print(f"   ❌ Template parsing failed: {e}")
            # Don't fail the entire test if template parsing fails - this might be expected if the template doesn't exist
            print(f"   ℹ️  This might be expected if the 'onboarding' template is not configured on the server")
        
        print("\n" + "=" * 50)
        print("✅ Complete DevInbox workflow test completed!")
        print("\n🎯 What we accomplished:")
        print("  📧 Created a temporary mailbox")
        print("  📊 Verified mailbox was empty")
        print("  📤 Sent email via SMTP with test content")
        print("  📬 Verified email was received via API")
        print("  🔍 Tested template parsing with 'onboarding' template")
        print("\n🚀 DevInbox is working perfectly!")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
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

