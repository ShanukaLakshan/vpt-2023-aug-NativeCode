from flask import Flask, render_template, request
import requests

app = Flask(__name__)

OPENLIBRARY_API_SEARCH = "http://openlibrary.org/search.json?q={}"
OPENLIBRARY_API_BOOK = "http://openlibrary.org/works/{}.json"


@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form.get('query')
        response = requests.get(OPENLIBRARY_API_SEARCH.format(query))
        if response.status_code == 200:
            data = response.json()
            results = data.get('docs', [])
    return render_template('index.html', results=results)


@app.route('/book/<book_id>', methods=['GET'])
def book(book_id):
    response = requests.get(OPENLIBRARY_API_BOOK.format(book_id))
    if response.status_code == 200:
        book_data = response.json()

        print(book_data)
        return render_template('book.html', book=book_data)
    return "Error fetching book details", 400


if __name__ == '__main__':
    app.run(debug=True)
