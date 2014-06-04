import json
import os
from subprocess import Popen, PIPE

from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def hello():
    url = request.args.get('url', None)
    if url is None or not len(url):
        return jsonify({'usage': 'http://mp3duration.herokuapp.com/?url=http://some/url/to/a/file.mp3'})

    output = Popen(['ffprobe', '-print_format', 'json', '-show_entries', 'format=duration', '-i', url.replace('&', '\&')], stdout=PIPE).stdout.read()
    data = json.loads(output)
    if data.has_key('format'):
        return jsonify({'seconds': data['format']['duration']})
    else:
        return jsonify({'error': 'Unable to retrieve file from URL'})


if __name__ == "__main__":
    app.run(debug=True)
