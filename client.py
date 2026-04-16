import json
import requests

data = {'features': [1,2,3,4]}

url = 'http://0.0.0.0:8000/predict/'

predictions = []
for record in data:
  payload = {'features':record}
  payload = json.dumps(payload)
  response = requests.post(url, data=payload)
  predictions.append(response.json()['predictions])

print(predictions)
