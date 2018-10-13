from flask import Flask
from werkzeug.routing import BaseConverter

class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        super(RegexConverter, self).__init__(map)
        self.regex = args[0]

app = Flask(__name__)
app.url_map.converters["regex"] = RegexConverter

@app.route('/index/<regex("\w{4,5}"):user>/')
def index(user):
    return user

if __name__ == "__main__":
    app.run(debug=True)