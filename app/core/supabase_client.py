#SE DECLARA EL CLIENTE QUE VA 
from supabase import create_client, Client
from app.core.config import config

supabase: Client = create_client(
    config.supabase_url,
    config.supabase_key
)

def get_supabase() -> Client:
    return supabase