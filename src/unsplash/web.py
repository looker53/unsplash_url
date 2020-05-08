from flask import Flask, render_template, request

from .developer_api import get_photos, search_photos

app = Flask(__name__)

@app.route('/')
def index():
    order_by = request.args.get('order_by')
    pictures = get_photos(order_by)
    return render_template('index.html', pictures=pictures)

@app.route('/search')
def search():
    keyword = request.args.get('key')
    pictures = search_photos(keyword)['results']
    return render_template('index.html', pictures=pictures)

if __name__ == '__main__':
    app.run(debug=True)

