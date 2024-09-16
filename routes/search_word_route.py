from tools.database_tools import initialize_database
from tools.cosine_similarity_tools import compare_words, compare_words_char_cosine_similarity
from config import CONNECTION_STRING, DATABASE_NAME, WORDS_COLLECTION_NAME

from flask import request, Response

import json

def search_word_route():
    words_collection = initialize_database(CONNECTION_STRING, DATABASE_NAME, WORDS_COLLECTION_NAME)

    body = request.get_json()

    words_collection_response = words_collection.find({})

    similar_words = []

    word = body['word']
    minimum_similarity = float(body['minimum_similarity'])

    for each in words_collection_response:
        if each.get("word") == word:
            continue

        similarity = compare_words_char_cosine_similarity(word, each.get("word"))

        if similarity >= minimum_similarity:
            similar_words.append({"word": each.get("word"), "similarity": round(similarity, 2)})


    return Response(json.dumps({"words": similar_words}), mimetype="application/json")
