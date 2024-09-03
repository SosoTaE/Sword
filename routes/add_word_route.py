from flask import request, Response
from config import CONNECTION_STRING, DATABASE_NAME, WORDS_COLLECTION_NAME
from tools.database_tools import initialize_database
from tools.words_parsing_tools import contains_only_georgian_letters

import json

def add_word_route():
    words_collection = initialize_database(CONNECTION_STRING, DATABASE_NAME, WORDS_COLLECTION_NAME)

    body = request.get_json()

    if not body.get("word"):
        return Response(json.dumps({"error": "No word"}), status=400)

    if not contains_only_georgian_letters(body.get("word")):
        return Response(json.dumps({"error": "Word should contain only georgian letters"}), status=400)

    if not words_collection.find_one({"word": body.get("word")}):
        words_collection.insert_one({"word": body.get("word")})
        return Response(json.dumps({"word": "Word added successfully"}), status=200)

    return Response(json.dumps({"error": "Word already exists"}), status=400)
