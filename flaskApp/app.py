#import
import pickle 
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from flask import (Flask,
                   request,
                   jsonify,
                   render_template)

#for api
import  requests

print('import success')

#load_models
#le
job_LE = pickle.load(open('../flaskApp/models/job_LE.pkl', 'rb'))
marital_LE = pickle.load(open('../flaskApp/models/marital_LE.pkl', 'rb')) 	
education_LE = pickle.load(open('../flaskApp/models/education_LE.pkl', 'rb'))	
default_LE = pickle.load(open('../flaskApp/models/default_LE.pkl', 'rb')) 	
housing_LE = pickle.load(open('../flaskApp/models/housing_LE.pkl', 'rb'))	
loan_LE	= pickle.load(open('../flaskApp/models/loan_LE.pkl', 'rb'))
contact_LE	= pickle.load(open('../flaskApp/models/contact_LE.pkl', 'rb'))
month_LE	= pickle.load(open('../flaskApp/models/month_LE.pkl', 'rb'))
poutcome_LE	= pickle.load(open('../flaskApp/models/poutcome_LE.pkl', 'rb'))
#predict le
y_LE = pickle.load(open('../flaskApp/models/y_LE.pkl', 'rb'))
#scaler
num_scaler = pickle.load(open('../flaskApp/models/num_scaler.pkl', 'rb'))
#ML models
kNN = pickle.load(open('../flaskApp/models/kNN.pkl', 'rb'))

#app
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def main():
    if request.method == 'GET':
        return render_template('main.html')
    
    if request.method == 'POST':
        #get_data
        #получаем данные с формы
        #cat_cols
        job	= request.form['job']
        marital	= request.form['marital']
        education	= request.form['education']
        default	= request.form['default']
        housing= request.form['housing']
        loan	= request.form['loan']
        contact= request.form['contact']
        month= request.form['month']
        poutcome= request.form['poutcome']
        #num_cols
        age	= float(request.form['age'])
        balance	= float(request.form['balance'])
        day	= float(request.form['day'])
        duration = float(request.form['duration'])
        campaign = float(request.form['campaign'])
        pdays	 = float(request.form['pdays'])
        previous = float(request.form['previous'])

        #preprocessing
        ##categorical
        X_cat_from_form = [job,
                           marital,
                           education,
                           default,
                           housing,
                           loan,
                           contact,
                           month,
                           poutcome]
        #print(X_cat_from_form)
        
        
        le_list = [job_LE,	
                marital_LE,	
                education_LE,	
                default_LE,
                housing_LE,
                loan_LE,
                contact_LE,
                month_LE,
                poutcome_LE]

        X_le_list = [] #под закодированные признаки
        for i in range(len(X_cat_from_form)):
            x_cat = le_list[i].transform([X_cat_from_form[i]])[0]
            # print(x_cat)
            X_le_list.append(x_cat)
        #print('X_cat_le:', X_le_list)

        ##num
        X_nums_from_form =[age, 
                               balance, 
                               day, 
                               duration,
                               campaign,
                               pdays,
                               previous]
        #print('X_nums', X_nums_from_form)

        ##объединить категориальные и числовые (в том же порядке, как и при обучении)
        X = []
        X.extend(X_le_list)
        X.extend(X_nums_from_form)
        #print('X:', X)

        #scaler
        X_scaled = num_scaler.transform([X])
        #print('X_scaled:', X_scaled)

        #predict
        prediction = kNN.predict(X_scaled)
        print(prediction)

        #result
        result = y_LE.inverse_transform(prediction)
        #print('Выдавать клиентский договор? Ответ - ', result)
        
        return render_template('predict.html', 
                               result = result)


#API 
@app.route('/api/v1/get_message/', methods = ['POST', 'GET'])
def api_message():
    get_message_x = request.json #получаем json  с другого сервиса
    #scaler
    X_scaled = num_scaler.transform(get_message_x['X_for_predict'])
    print('X_scaled:', X_scaled)
    #predict
    prediction = kNN.predict(X_scaled)

    return jsonify(str(prediction))


#инструкция исполнения
if __name__ == '__main__':
    app.run()
