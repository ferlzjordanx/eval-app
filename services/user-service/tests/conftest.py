import os


os.environ.setdefault("DB_HOST", "localhost")
os.environ.setdefault("DB_PORT", "5432")
os.environ.setdefault("DB_USERNAME", "postgres")
os.environ.setdefault("DB_PASSWORD", "postgres")
os.environ.setdefault("DB_NAME", "eval_app_test")
os.environ["JWT_SECRET"] = "test-secret-that-is-long-enough-for-hs256"
os.environ["JWT_ALGORITHM"] = "HS256"
