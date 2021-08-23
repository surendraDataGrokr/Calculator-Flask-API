from flask import Flask, request, jsonify

# init app
app = Flask(__name__)

# For Addition
@app.route('/addition', methods=['POST'])
def addition():
    a = request.json['num1']
    b = request.json['num2']

    return jsonify(a+b)

# For Subtraction
@app.route('/subtraction', methods=['POST'])
def subtraction():
    a = request.json['num1']
    b = request.json['num2']

    return jsonify(a-b)

# For Multiplication
@app.route('/multiplication', methods=['POST'])
def multiplication():
    a = request.json['num1']
    b = request.json['num2']

    return jsonify(a*b)

# For Division
@app.route('/division', methods=['POST'])
def division():
    a = request.json['num1']
    b = request.json['num2']

    return jsonify(a/b)


# Run the server

if __name__ == '__main__':
    app.run(debug=True)