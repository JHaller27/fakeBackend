from flask import Flask, request
app = Flask(__name__)


seen_set = set()


def get_key(r):
    return hash(r.args)


@app.route('/')
def do():
    key = get_key(request)
    if key not in seen_set:
        seen_set.add(key)
        return 'err', 404
    else:
        seen_set.remove(key)
        return request.args
