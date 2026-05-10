from flask import Flask, render_template, request
from model import predict_disease

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    fever = int(request.form.get('fever'))
    cough = int(request.form.get('cough'))
    headache = int(request.form.get('headache'))
    fatigue = int(request.form.get('fatigue'))
    sore_throat = int(request.form.get('sore_throat'))
    body_pain = int(request.form.get('body_pain'))

    symptoms = [
        fever,
        cough,
        headache,
        fatigue,
        sore_throat,
        body_pain
    ]

    result = predict_disease(symptoms)

    precautions = {
        'Flu': 'Drink warm fluids and take rest.',
        'Cold': 'Stay hydrated and avoid cold food.',
        'Migraine': 'Reduce stress and take proper sleep.',
        'Dengue': 'Consult doctor immediately and stay hydrated.',
        'COVID-19': 'Isolate and consult healthcare provider.',
        'Stress': 'Meditation and proper sleep recommended.',
        'Malaria': 'Take medical treatment immediately.'
    }

    recommendation = precautions.get(result, 'Consult a doctor.')

    return render_template(
        'index.html',
        prediction=result,
        recommendation=recommendation
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)