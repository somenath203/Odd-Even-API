from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/oddeven/<int:a>')
def calculate(a):
    if(a % 2 == 0):
        result = {
            "Number": a,
            "Result": "Even",
        }

    else:
        result = {
            "Number": a,
            "Result": "Odd",
        }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
