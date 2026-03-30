
from dotenv import load_dotenv
import os  # ← only needed if you want os.environ, otherwise optional

load_dotenv(".env")  # looks in the current working directory

print(os.environ.get("API_KEY_WRONG"))
