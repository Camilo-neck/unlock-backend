from src.supa.client import sb

response = sb.auth.admin.list_users()

print(response)