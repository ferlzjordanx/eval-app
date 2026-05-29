import os


os.environ.setdefault("MONGO_URI", "mongodb://localhost:27017/eval_app_test")
os.environ.setdefault("MONGO_DB", "eval_app_test")
os.environ.setdefault("ALLOW_ORIGINS", "*")
os.environ.setdefault("SERVICE_NAME", "question-management-service")
os.environ.setdefault("PORT", "8003")
os.environ.setdefault("SERVICE_HOSTNAME", "localhost")
