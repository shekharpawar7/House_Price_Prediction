import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')    

@app.route('/process_form', methods=['POST'])
def predict():
    # Load the models (assuming they are defined and loaded correctly)
        bedroom=request.form['bedroom']
        bathroom=request.form['bathroom']
        sqft_living=request.form['sqft_living']
        sqft_lot=request.form['sqft_lot']
        floors=request.form['floors']
        zipcode=request.form['zipcode']
       
        model=joblib.load('model_houes.pkl')
        new_house = pd.DataFrame({'bedrooms': [bedroom], 'bathrooms': [bathroom], 'sqft_living': [sqft_living], 'sqft_lot': [sqft_lot], 'floors': [floors], 'zipcode': [zipcode]})
        predicted_price = int(model.predict(new_house))
        if predicted_price > 0:
            return render_template('index.html', prediction_text=f'Your New Houes Price expected is Rs.{predicted_price}')

        else:
            return render_template('index.html', prediction_text='Enter correct location')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1412)
