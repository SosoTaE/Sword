import mimetypes

def get_mimetype(filename):
    mime_type = mimetypes.guess_type(filename)[0]

    if mime_type:
        return mime_type