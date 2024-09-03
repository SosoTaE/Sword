from server import app
from routes.home_route import home_route
from routes.search_word_route import search_word_route

@app.route("/", methods=['GET', "POST"])
def home():
    return home_route()

@app.route('/similarWords', methods=["POST"])
def search_words():
    return search_word_route()

if __name__ == '__main__':
    app.run(debug=True)
