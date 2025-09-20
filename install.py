#!/usr/bin/env python3
"""
DevInbox Python Client Installation Script
Installs the client and its dependencies
"""

import subprocess
import sys
import os


def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"   ✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ {description} failed:")
        print(f"   Error: {e.stderr}")
        return False


def main():
    """Main installation function"""
    print("DevInbox Python Client Installation")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("setup.py"):
        print("❌ Error: setup.py not found. Please run this script from the dev-inbox directory.")
        sys.exit(1)
    
    # Install the client
    if not run_command("pip install -e .", "Installing DevInbox client"):
        print("\n❌ Installation failed!")
        sys.exit(1)
    
    # Install additional dependencies if needed
    if os.path.exists("requirements.txt"):
        if not run_command("pip install -r requirements.txt", "Installing additional dependencies"):
            print("\n⚠️  Some dependencies failed to install, but the client should still work.")
    
    print("\n" + "=" * 50)
    print("🎉 Installation completed successfully!")
    print("\nNext steps:")
    print("1. Run the test script: python test_all_endpoints.py")
    print("2. Try the example: python example_usage.py")
    print("3. Read the documentation: CLIENT_README.md")
    print("\n🚀 The DevInbox Python client is ready to use!")


if __name__ == "__main__":
    main()

