#import
import pickle 
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
print('import success')

#load_models

job_LE = pickle.load(open('../180824_prod/models/job_LE.pkl', 'rb'))
marital_LE = pickle.load(open('../180824_prod/models/marital_LE.pkl', 'rb')) 	
education_LE = pickle.load(open('../180824_prod/models/education_LE.pkl', 'rb'))	
default_LE = pickle.load(open('../180824_prod/models/default_LE.pkl', 'rb')) 	
housing_LE = pickle.load(open('../180824_prod/models/housing_LE.pkl', 'rb'))	
loan_LE	= pickle.load(open('../180824_prod/models/loan_LE.pkl', 'rb'))
contact_LE	= pickle.load(open('../180824_prod/models/contact_LE.pkl', 'rb'))
month_LE	= pickle.load(open('../180824_prod/models/month_LE.pkl', 'rb'))
poutcome_LE	= pickle.load(open('../180824_prod/models/poutcome_LE.pkl', 'rb'))
y_LE = pickle.load(open('../180824_prod/models/y_LE.pkl', 'rb'))

#get_data
#вводим с клавиатуры
# #cat_cols
# job	= input()
# marital	= input()
# education	= input()
# default	= input()
# housing= input()
# loan	= input()
# contact= input()
# month= input()
# poutcome= input()
# #num_cols
# age	= float(input())
# balance	= float(input())
# day	= float(input())
# duration = float(input())
# campaign = float(input())
# pdays	 = float(input())
# previous = float(input())

X_cat_from_keyboard = ['unemployed',
                       'married',
                       'primary',
                       'no',
                       'no',
                       'yes',
                       'cellular',
                       'may',
                       'failure'
                        ]
print(X_cat_from_keyboard)
X_nums_from_keyboard =[30,
                       1787,
                       16,
                       199,
                       4,
                       330,
                       0]
print(X_nums_from_keyboard)

#preprocessing
##categorical

##num

##объединить категориальные и числовые (в том же порядке, как и при обучении)

#scaler

#predict

#result
