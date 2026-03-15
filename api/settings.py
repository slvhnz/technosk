import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY="..."

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET_NAME = os.getenv("SUPABASE_BUCKET_NAME", "post-media")

# Comma-separated list of explicit origins allowed by CORS.
CORS_ALLOWED_ORIGINS = os.getenv(
	"CORS_ALLOWED_ORIGINS",
	"http://localhost:5173,https://technosk.vercel.app",
)

# Optional regex for dynamic origins such as Vercel preview URLs.
# Example: r"https://.*\\.vercel\\.app"
CORS_ALLOWED_ORIGIN_REGEX = os.getenv("CORS_ALLOWED_ORIGIN_REGEX", "")


SECRET_KEY = os.getenv("SECRET_KEY", "a_very_secret_key_that_should_be_changed")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


