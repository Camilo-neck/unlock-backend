from src._supabase.supabase_client import supabase_client as sb

response = sb.auth.admin.list_users()

print(response)