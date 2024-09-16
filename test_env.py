import os
from pathlib import Path
from dotenv import load_dotenv
import dotenv

# Load .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Accessing environment variables
app_base_url = os.getenv('APP_BASE_URL')
api_base_url = os.environ('API_BASE_URL')
api_users_url = os.getenv('API_USERS_URL')
api_products_url = os.getenv('API_PRODUCTS_URL')
api_orders_url = dotenv.get_key('API_ORDERS_URL')

# Print the values
print(f"App Base URL: {app_base_url}")
print(f"API Base URL: {api_base_url}")
print(f"API Users URL: {api_users_url}")
print(f"API Products URL: {api_products_url}")
print(f"API Orders URL: {api_orders_url}")
