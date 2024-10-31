from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Маршрут для главной страницы


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operator = data.get('operator')
    num1 = data.get('num1')
    num2 = data.get('num2')

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        return jsonify({"error": "Invalid operator"}), 400

    return jsonify({"result": round(result, 3)})


if __name__ == '__main__':
    app.run(debug=True)
