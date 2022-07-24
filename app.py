import preprocess
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load('model.h5')
scaler = joblib.load('scaler.h5')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def get_prediction():


    if request.method == 'POST':
        Income = request.form['Income']
        Age = request.form['Age']
        Experience = request.form['Experience']
        CURRENT_JOB_YRS = request.form['CURRENT_JOB_YRS']
        CURRENT_HOUSE_YRS = request.form['CURRENT_HOUSE_YRS']
        Status = request.form['Status']
        Car_Ownership = request.form['Car_Ownership']
        House_Ownership = request.form['House_Ownership']
    data =  {'Income':Income, 'Age':Age, 'Experience':Experience, 'CURRENT_JOB_YRS':CURRENT_JOB_YRS,
        'CURRENT_HOUSE_YRS':CURRENT_HOUSE_YRS, 'Status':'Status', 'Car_Ownership':'Car_Ownership',
        'House_Ownership':'House_Ownership'}

    Final_data = preprocess.User(data)
    scaled_data = scaler.transform([Final_data])
    predict = model.predict(scaled_data)[0]

    print(predict)
    if predict== 0:
        predict = "Customer is not defaulter"   

    else:
        predict = "Customer is defaulter"  
                    
    return render_template('prediction.html', prediction=(predict))


if __name__ == "__main__":
    app.run(debug=True)
