from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    make_response
)
import sys
from utils import *
import json


app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decider', methods=['POST'])
def decider():
    try:
        number1 = request.form['number1']
        number2 = request.form['number2']
        operation = request.form['operation']

        with app.test_client() as client:
            data = {
                'number1': number1,
                'number2': number2,
            }

            path = f'/calculator/{operation}'

            headers = {
                'Content-Type': 'application/json',
            }

            response = client.post(path, data=json.dumps(data), headers=headers)

            data['operation'] = operation_as_symbol(operation)
            data['result'] = response.get_json()['result']

            return render_template('answer.html', info=data)

    except Exception as error:
        print(error)
        return 'Algo deu errado!'

@app.route('/calculator/add', methods=['POST'])
def calculator_add():
    data = request.get_json()

    try:
        return jsonify(
            {'result': add(float(data['number1']), float(data['number2']))}
        )
    except:
        return make_response({'result': 'digitacertoporra'}, 400)

@app.route('/calculator/subtract', methods=['POST'])
def calculator_subtract():
    data = request.get_json()

    return jsonify(
        {'result': subtract(float(data['number1']), float(data['number2']))}
    )


@app.route('/calculator/multiply', methods=['POST'])
def calculator_multiply():
    data = request.get_json()

    return jsonify(
        {'result': multiply(float(data['number1']), float(data['number2']))}
    )


@app.route('/calculator/divide', methods=['POST'])
def calculator_divide():
    data = request.get_json()
    
    try:
        return jsonify(
            {'result': divide(float(data['number1']), float(data['number2']))}
        )
    except (ValueError, ZeroDivisionError) as error:
        print(error)
        return make_response({'result': 'digitacertoporra'}, 400)
    except Exception as error:
        print(error)
        return make_response({'result': 'porra gu, nao fode'}, 400)

if __name__ == "__main__":
    try:
        PORT = sys.argv[1]
    except IndexError:
        print('No port was specified')
        PORT = 5000
    
    print(f'Server is running on port {PORT}')
    app.run(port=int(PORT), debug=True)
