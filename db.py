from encodings import utf_8
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy(use_native_unicode='utf8')
