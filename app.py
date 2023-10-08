from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained machine learning model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user inputs from the form
        guests = float(request.form['guests'])
        event = request.form['event']

        # Perform prediction using the trained model
        balloons_needed = model.predict([[guests]])[0]

        # Render the result in the result.html template
        return render_template('result.html', guests=guests, event=event, balloons_needed=balloons_needed)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
