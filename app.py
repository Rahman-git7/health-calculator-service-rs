from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '''
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Calculateur de Santé - API</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="container py-5">
        <h1 class="mb-4">Calculateur de Santé - API</h1>
        <p>Bienvenue sur l'API de Calculateur de Santé. Cette API fournit des calculs pour l'Indice de Masse Corporelle (IMC) et le Métabolisme de Base (MB).</p>

        <hr>

        <h2 class="mt-5">Calculateur d'IMC</h2>
        <form id="bmiForm" class="mb-5">
            <div class="mb-3">
                <label class="form-label">Taille (en mètres):</label>
                <input type="number" step="any" class="form-control" id="height">
            </div>
            <div class="mb-3">
                <label class="form-label">Poids (en kg):</label>
                <input type="number" step="any" class="form-control" id="weight">
            </div>
            <button type="submit" class="btn btn-primary">Calculer l'IMC</button>
            <p class="mt-3" id="bmiResult"></p>
        </form>

        <h2>Calculateur de Métabolisme de Base</h2>
        <form id="bmrForm">
            <div class="mb-3">
                <label class="form-label">Taille (en cm):</label>
                <input type="number" class="form-control" id="height_bmr">
            </div>
            <div class="mb-3">
                <label class="form-label">Poids (en kg):</label>
                <input type="number" class="form-control" id="weight_bmr">
            </div>
            <div class="mb-3">
                <label class="form-label">Âge (en années):</label>
                <input type="number" class="form-control" id="age">
            </div>
            <div class="mb-3">
                <label class="form-label">Genre:</label>
                <select class="form-control" id="gender">
                    <option value="male">Homme</option>
                    <option value="female">Femme</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Calculer le MB</button>
            <p class="mt-3" id="bmrResult"></p>
        </form>

        <script>
            document.getElementById('bmiForm').addEventListener('submit', async (e) => {
                e.preventDefault();
                const height = parseFloat(document.getElementById('height').value);
                const weight = parseFloat(document.getElementById('weight').value);

                const response = await fetch('/bmi', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ height, weight })
                });

                const data = await response.json();
                if (data.bmi) {
                    document.getElementById('bmiResult').textContent = `Votre IMC est : ${data.bmi}`;
                } else {
                    document.getElementById('bmiResult').textContent = 'Erreur dans les données.';
                }
            });

            document.getElementById('bmrForm').addEventListener('submit', async (e) => {
                e.preventDefault();
                const height = parseFloat(document.getElementById('height_bmr').value);
                const weight = parseFloat(document.getElementById('weight_bmr').value);
                const age = parseInt(document.getElementById('age').value);
                const gender = document.getElementById('gender').value;

                const response = await fetch('/bmr', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ height, weight, age, gender })
                });

                const data = await response.json();
                if (data.bmr) {
                    document.getElementById('bmrResult').textContent = `Votre MB est : ${data.bmr}`;
                } else {
                    document.getElementById('bmrResult').textContent = 'Erreur dans les données.';
                }
            });
        </script>
    </body>
    </html>
    '''

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
    app.run(host='0.0.0.0', port=5000)
