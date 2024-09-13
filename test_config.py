import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the config.ini file
config.read('config.ini')

# Accessing values from the config file
app_base_url = config['Application']['base_url']
api_base_url = config['API']['base_url']
api_users_url = config['API']['users_url']
api_products_url = config['API']['products_url']
api_orders_url = config['API']['orders_url']
auth_login_url = config['Authentication']['login_url']
database_url = config['Database']['url']
payment_gateway_url = config['ThirdPartyServices']['payment_gateway_url']
cdn_images_url = config['CDN']['images_url']
docs_url = config['Documentation']['docs_url']
support_url = config['Support']['support_url']


# Accessing values from the config file using config.get
app_base_url = config.get('Application', 'base_url')
api_base_url = config.get('API', 'base_url')
api_users_url = config.get('API', 'users_url')
api_products_url = config.get('API', 'products_url')
api_orders_url = config.get('API', 'orders_url')
auth_login_url = config.get('Authentication', 'login_url')
database_url = config.get('Database', 'url')
payment_gateway_url = config.get('ThirdPartyServices', 'payment_gateway_url')
cdn_images_url = config.get('CDN', 'images_url')
docs_url = config.get('Documentation', 'docs_url')
support_url = config.get('Support', 'support_url')

# Print the values
print(f"App Base URL: {app_base_url}")
print(f"API Base URL: {api_base_url}")
print(f"API Users URL: {api_users_url}")
print(f"API Products URL: {api_products_url}")
print(f"API Orders URL: {api_orders_url}")
print(f"Auth Login URL: {auth_login_url}")
print(f"Database URL: {database_url}")
print(f"Payment Gateway URL: {payment_gateway_url}")
print(f"CDN Images URL: {cdn_images_url}")
print(f"Docs URL: {docs_url}")
print(f"Support URL: {support_url}")

