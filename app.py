import os.path
import popen2

from flask import Flask, request, Response


app = Flask(__name__)


@app.route('/')
def hello():
    requested_duration = request.args.get('duration', '')
    if not len(requested_duration):
        return '<h1>Usage</h1><p><code>http://mp3loop.herokuapp.com/?duration=<em>&lt;seconds&gt;</em></code></p>'

    # The output tends to be a little shorter ...
    output_duration = int(requested_duration) * 1.008120975

    directory = os.path.dirname(os.path.realpath(__file__))
    std_out_err, std_in = popen2.popen4('ffmpeg -f concat -i %s/concat.txt -c copy -t %s -f mp3 pipe:1' % (directory, int(round(output_duration))))

    def f():
        for line in std_out_err:
            yield line

    return Response(f(), content_type='audio/mp3', headers={'Content-Disposition': 'inline; filename=loop-%s.mp3' % requested_duration})


if __name__ == "__main__":
    app.run(debug=True)
