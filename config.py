import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://20220608sql.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', '5wPrKTE2ridfpNhJIvm3C5kWIyVL8bkrlnVjGaqXFSxadvCIKkcU0hx5x99XXaFgsLPKFdrd9NBVPZFYFfzYHg=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}