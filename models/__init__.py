#!/usr/bin/python3
"""initialliazation called __init__.py file to creat storage for my application"""
from engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
