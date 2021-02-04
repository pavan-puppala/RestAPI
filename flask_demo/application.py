from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def input():
    return render_template('input.html')

@app.route("/math", methods=['POST'])
def math_operations():
    if request.json is not None:
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if operation == "add":
            result = num1+num2
        elif operation == "sub":
            result = num1-num2
        elif operation == "mul":
            result = num1*num2
        elif operation == "div":
            result = num1/num2
        print(result)  # to print in console

        return jsonify(result)
    else:
        return(jsonify("request is not correct.."))

if __name__ == '__main__':
    print("application is running..")
    app.run()
