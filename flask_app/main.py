import time

from flask import Flask, Response

from chartdata import graph_data
from config import log_file_dir, reload_interval

# flaskオブジェクトの作成
app = Flask(__name__)

def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.disable_buffering()
    return rv

def gen_data():
    while True:
        try:
            graphdata = graph_data(log_file_dir)
            yield graphdata
            time.sleep(reload_interval)
        except:
            graphdata = {"label": [], "val": [0]}
            yield graphdata
            time.sleep(reload_interval)

# / へのアクセスの処理
@app.route('/')
def chart():
    genData = gen_data()
    return Response(stream_template('chart.html', gen_data=genData))

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)