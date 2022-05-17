from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('cement_strength_model.pickle', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        cement = float(request.form['cement'])
        blast_furnace=float(request.form['blast_furnace'])
        fly_ash=float(request.form['fly_ash'])
        water=float(request.form['water'])
        super_plasticizer=float(request.form['super_plasticizer'])
        coarse_aggregate=float(request.form['coarse_aggregate'])
        fine_aggregate=float(request.form['fine_aggregate'])
        age=int(request.form['age'])
        prediction=model.predict([[cement,blast_furnace,fly_ash,water,super_plasticizer,coarse_aggregate,fine_aggregate,age]])
        output=round(prediction[0],2)
        return render_template('index.html',prediction_text="The cement strength is {}".format(output))

    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

