import re
import os 

patterns = {
    'Access Key': r'AKIA[0-9A-Z]{16}',
    'Secret Key': r'(?i)aws(.{0,20})?['"\']([A-Za-z0-9/+=]{40})['"']',
    'API Key': r'(?i)(api_key|apikey|apiSecret|apiToken)[\'"\s:]+([A-Za-z0-9-_]{20,})',
    'Token': r'(?i)(token|access_token|auth_token|bearer_token)[\'"\s:]+([A-Za-z0-9-_]{20,})',
    'Username': r'(?i)(username|user_name)[\'"\s:]+[\'"][A-Za-z0-9-_]+[\'"]',
    'Password': r'(?i)(password|pass|passwd|pwd)[\'"\s:]+[\'"][A-Za-z0-9@#$%^&+=!]*[\'"]'
}

def find_secrets(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    results = []
    for secret_type, pattern in patterns.items():
        print(f"\nPattern: {pattern}")
        matches = re.findall(pattern, code)
        if matches:
            print(f"Matches: {matches}")
            for match in matches:
                results.append((secret_type, match))
    return results


if __name__ == "__main__":
    # FILE_NAME = os.environ.get("FILE_NAME")
    FILE_NAME = "secrets-scanner-action/sample_secrets.py"
    secrets_found = find_secrets(FILE_NAME)
    if secrets_found:
        print("\nPotential Secrets found: ")
        for secret_type, secret in secrets_found:
            print(f"- {secret_type}: {secret}")
    else:
        print("\nNo hardcoded secrets found.\n")