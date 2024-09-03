import os

from tools.database_tools import initialize_database
from tools.mimetype_tools import get_mimetype
from tools.words_parsing_tools import get_georgian_words
from config import CONNECTION_STRING, DATABASE_NAME, WORDS_COLLECTION_NAME

import fitz

from datetime import datetime, timezone

class FilesToWords:
    def __init__(self, files):
        self.files = files
        self.words_collection = initialize_database(CONNECTION_STRING, DATABASE_NAME, WORDS_COLLECTION_NAME)
        self.functions_according_to_file_mimetype = {
            "application/pdf": self.pdf_to_text
        }

        for file in files:
            print(file)
            mimetype = get_mimetype(file)
            print(f"MIME Type: {mimetype}")
            if mimetype in self.functions_according_to_file_mimetype:
                self.functions_according_to_file_mimetype[mimetype](file)

    def pdf_to_text(self, path):
        doc = fitz.open(path)

        # Iterate through pages
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)

            # Extract text from the page
            text = page.get_text()

            georgian_words = get_georgian_words(text)

            for word in georgian_words:
                current_datetime_utc = datetime.now(timezone.utc)
                data = {"word": word, "time": current_datetime_utc, "addCount": 1}
                filter_query = {"word": word}
                self.words_collection.update_one(filter_query,{"$setOnInsert": data}, upsert=True)



        # Close the PDF file
        doc.close()


