from flask import Flask, render_template, request, jsonify
from werkzeug.routing import BaseConverter
from queue import Queue

Users = {
    1: {"name": "lance", "count": 1},
    2: {"name": "lily", "count": 1},
    3: {"name": "Guo", "count": 1}
}

class RegexConverter(BaseConverter):
    def __init__(self, map, *args):
        super(RegexConverter, self).__init__(map)
        self.regex = args[0]

app = Flask(__name__)
app.url_map.converters["regex"] = RegexConverter

@app.route('/index/<regex("\w{4,5}"):user>/')
def regex(user):
    return user

@app.route("/index/")
def index():
    return render_template("index.html", users=Users)


q = Queue()
@app.route("/vote/", methods=["POST"])
def vote():
    uid = request.form.get("uid")
    Users[int(uid)]["count"] += 1
    q.put(Users)
    return jsonify(Users)

if __name__ == "__main__":
    app.run(debug=True)