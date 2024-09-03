import os
import dotenv
from server import app

dotenv.load_dotenv("./")

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
CONNECTION_STRING = os.getenv("CONNECTION_STRING")
DATABASE_NAME = os.getenv("DATABASE_NAME")
FILES_COLLECTION_NAME = os.getenv("FILES_COLLECTION_NAME")
WORDS_COLLECTION_NAME = os.getenv("WORDS_COLLECTION_NAME")

app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024