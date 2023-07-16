"""initialliazation called __init__.py file to creat
storage for my application"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
all_objs = storage.all()
