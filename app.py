from flask import Flask, request, jsonify, render_template
import mlflow
import pandas as pd
import numpy as np
import joblib
from pathlib import Path
import os
from src.mlflow_ml.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # Initialize the Flask application

@app.route('/', methods=['GET']) # Define the home route
def homePage():
    return render_template("index.html") # Render the index.html template 

@app.route('/train', methods=['GET']) # Define the /train route for GET requests
def trainRoute():
    os.system('python main.py') # Run the main.py script to start training (using os.system, can execute any python command)
    return "Training sucessful!" # Return a success message after training
# when even main.py is run it will execute the entire model training pipeline

@app.route('/predict', methods=['GET','POST']) # Define the /predict route for POST requests
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
       
         
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__": # Run the Flask application
    # app.run(host="0.0.0.0", port=8080, debug=True) # Run the app on host
    app.run(host="0.0.0.0", port=8080) # for aws (production)
