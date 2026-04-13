from fastapi import FastAPI
import joblib
import numpy as np

model = joblib.load('model.joblib')

class_names = np.array(['setosa', 'versicolor','virginica'])

app =FastAPI()

@app.get('/')

@app.post('/predict')
