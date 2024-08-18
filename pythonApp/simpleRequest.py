import requests

#допустим тут какой-то код

X_for_predict = [10,    1,   0  ,  0 ,   0   , 0  , 0  , 10  ,  3 , 30, 1787,  19  ,79  ,  1,-1 ,   0]

api_message = requests.post('http://127.0.0.1:5000/api/v1/get_message/', 
                            json = {'X_for_predict': [X_for_predict]})

print(api_message)
if api_message.ok:
    #print(api_message.json())
    if api_message.json()[0] == 0:
        print('Ответ - no')
    else:
        print('Ответ - YES')
