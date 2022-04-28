from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/hello')

def get_location_names():
    @app.route('/get_location_names', methods=['GET'])
    def get_location_names():
        response = jsonify({
            'locations': util.get_location_names()
        })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
@app.route('/predict_home_price', methods = ['POST'])
def perdict_home_price():
    @app.route('/predict_home_price', methods=['GET', 'POST'])
    def predict_home_price():
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        response = jsonify({
            'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

    return "hello"




if __name__ == "__main__":
    print('Starting the Python Flask Server For Bangalore House Price Prediction')
    app.run()