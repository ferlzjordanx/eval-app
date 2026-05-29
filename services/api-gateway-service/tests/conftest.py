import os


os.environ["JWT_SECRET"] = "test-secret-that-is-long-enough-for-hs256"
os.environ["JWT_ALGORITHM"] = "HS256"
os.environ.setdefault("ALLOW_ORIGINS", "http://localhost:3000")
