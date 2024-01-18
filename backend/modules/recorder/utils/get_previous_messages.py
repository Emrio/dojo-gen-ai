import os
from supabase.client import create_client

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]

def get_previous_messages():
  supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)

  response = supabase_client.table("history").select("*").execute()

  return response.data
