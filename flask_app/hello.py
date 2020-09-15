from flask import Flask

# flaskオブジェクトの作成
app = Flask(__name__)

# / へのアクセスの処理
@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name

## おまじない
if __name__ == "__main__":
    app.run(debug=True)

