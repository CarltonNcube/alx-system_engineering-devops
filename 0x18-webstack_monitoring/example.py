import os
from datadog import initialize, api

# Set Datadog API and application keys
api_key = "3f30f9c2-8e01-4925-8526-1ae8c6990afc"
app_key = "f143f2ee-1b82-4e92-a77c-25fa169d8805"

# Initialize Datadog API client
options = {
    'api_key': api_key,
    'app_key': app_key,
    'api_host': 'https://api.datadoghq.com'  # Use 'https://api.datadoghq.com' for the US region
}

initialize(**options)

# Example: Get information about your Datadog account
account_info = api.Account.get()
print(account_info)

