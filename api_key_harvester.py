import os
import re

def find_api_keys(path="."):
    # Common patterns for API keys
    patterns = [
        r"AKIA[0-9A-Z]{16}",  # AWS Access Key
        r"AIza[0-9A-Za-z-_]{35}",  # Google API Key
        r"sk_live_[0-9a-zA-Z]{24}",  # Stripe Live Key
    ]
    
    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                with open(os.path.join(root, file), "r", errors="ignore") as f:
                    content = f.read()
                    for pattern in patterns:
                        matches = re.findall(pattern, content)
                        if matches:
                            print(f"[!] Found API Key in {file}: {matches}")
            except Exception as e:
                print(f"Error reading {file}: {e}")

if __name__ == "__main__":
    find_api_keys("/path/to/scan")
