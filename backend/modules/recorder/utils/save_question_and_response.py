import os
from supabase.client import create_client

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]

def save_question_and_response(question, answer):
    supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)

    supabase_client.table("history").insert({
      "question": question,
      "answer": answer
    }).execute()
