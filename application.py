
# importing the necessary dependencies
import pickle

from flask import Flask, render_template, request

application = Flask(__name__) # initializing a flask app
@application.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")

@application.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            LSTAT=float(request.form['LSTAT'])
            RM = float(request.form['RM'])
            filename = 'finalized_lmmodel.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[LSTAT,RM]])
            #prediction = [75]
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=round(prediction[0],2))
        except Exception as e:
            print('The Exception message is: ',e)
            error_string = str(e)
            return 'something is wrong' + error_string
    else:
        return render_template('index.html')

if __name__ == "__main__":
    application.run(debug=True) # running the app