import os
import pickle

import pandas as pd
from flask import Flask, jsonify, render_template, request,jsonify

app = Flask(__name__)
current_path = os.getcwd()
pickle_path = os.path.join(current_path, "assets", "covid19.pkl")
classifier = pickle.load(open(pickle_path, "rb"))
data_path = os.path.join(current_path, "assets", "Covid19India1.csv")
df = pd.read_csv(data_path)


@app.route("/",methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])


def predict():
	data = request.form
	print (data)
	No=data["No"]
	Num_Cases = data["Num_Cases"]
	Age_Bracket = data["Age_Bracket"]
	Gender = data["Gender"]
	Detected_City = data["Detected_City"]
	Detected_District = data["Detected_District"]
	Detected_State = data["Detected_State"]
        
	Day = data["Day"]
	Month = data["Month"]
	Year = data["Year"]

	cols = [
		'No'
		'Num_Cases' 
		'Age_Bracket'
		'Gender'
		'Detected_City' 
		'Detected_District' 
		'Detected_State'
		'Day' 
		'Month' 
		'Year '

    ]
	test_data = pd.DataFrame(
		[
			[
				No,
				Num_Cases,
				Age_Bracket,
				Gender,
				Detected_City, 
				Detected_District, 
				Detected_State,
				Day,
				Month, 
				Year ,
			]
		],
		columns=cols,
	)
	pred = classifier.predict(test_data)
	
	if pred==0:
		
		return render_template('index.html',prediction_text="Deceased")	
				
	elif pred==1:
		
		return render_template('index.html',prediction_text="Hospitalize")	
		
	elif pred==6:
		
		return render_template('index.html',prediction_text="Recovered")
	
		
	return render_template('index.html',prediction_text="others")
		
	


@app.route("/api/predict", methods=["POST"])
def predict_api():
	data = request.form
	print(data)
	No= data["No"]
	Num_Cases = data["Num_Cases"]
	Age_Bracket = data["Age_Bracket"]
	Gender = data["Gender"]
	Detected_City = data["Detected_City"]
	Detected_District = data["Detected_District	"]
	Detected_State = data["Detected_State"]
	Day = data["Day"]
	Month = data["Month"]
	Year = data["Year"]

	cols = [
		'No'
		'Num_Cases' 
		'Age_Bracket'
		'Gender'
		'Detected_City' 
		'Detected_District' 
		'Detected_State'
		'Day' 
		'Month' 
		'Year '

	]
	test_data = pd.DataFrame(
		[
			[
				No,
				Num_Cases ,
				Age_Bracket,
				Gender,
				Detected_City, 
				Detected_District, 
				Detected_State,
				Day,
				Month, 
				Year ,
			]
		],
			columns=cols,
	)
	pred = classifier.predict(test_data)
    
	if pred == 0:
			
		return jsonify("Deceased")
			
	elif pred==1:
	
		return jsonify("Hospitalize")
	
	elif pred==6:
		
		return jsonify(prediction_text="Recovered")
    
	
	return jsonify("others")

if __name__ == "__main__":
    app.run(debug=True)
