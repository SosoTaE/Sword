import os

from flask import request, render_template

from config import UPLOAD_FOLDER, CONNECTION_STRING, DATABASE_NAME, FILES_COLLECTION_NAME

from tools.database_tools import initialize_database
from tools.files_parsing_tools import FilesToWords

from datetime import datetime, timezone

def upload_files_route():
    # here I initialize database connection to check if filename is there.
    # if it is there it is not needed to add one more time

    files_collection = initialize_database(CONNECTION_STRING, DATABASE_NAME, FILES_COLLECTION_NAME)

    if 'files[]' not in request.files:
        return render_template("upload.html", message="No files part in the request")

    files = request.files.getlist('files[]')
    if not files:
        return render_template("upload.html", message="No selected file")


    saved_files = []
    for file in files:
        if file.filename == '':
            return render_template("upload.html", message="One of the files has no filename")

        if not files_collection.find_one({"filename": file.filename}):
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            saved_files.append(file_path)
            file.save(file_path)
            current_datetime_utc = datetime.now(timezone.utc)
            files_collection.insert_one({"filename": file.filename, "time": current_datetime_utc})



    files_to_words = FilesToWords(saved_files)

    return render_template("upload.html", message="Files uploaded successfully")

