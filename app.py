from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    try:
        height = float(data['height'])
        weight = float(data['weight'])
        bmi_result = calculate_bmi(height, weight)
        return jsonify({'bmi': round(bmi_result, 2)})
    except (KeyError, ValueError, TypeError):
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    try:
        height = float(data['height'])
        weight = float(data['weight'])
        age = int(data['age'])
        gender = data['gender']
        bmr_result = calculate_bmr(height, weight, age, gender)
        return jsonify({'bmr': round(bmr_result, 2)})
    except (KeyError, ValueError, TypeError):
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
