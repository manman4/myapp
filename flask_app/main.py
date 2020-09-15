from flask import Flask
from flask import render_template

# flaskオブジェクトの作成
app = Flask(__name__)

# / へのアクセスの処理
@app.route('/')
def show_result():
    with open("test.txt", "r") as f:
        data_list = []
        for i in f:
          data_list.append(i.rstrip("\n"))

        start_time = data_list[0]
        end_time = data_list[1]
        num = data_list[2]

    return render_template("result.html", start_time=start_time,
                            end_time=end_time, num=num)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)