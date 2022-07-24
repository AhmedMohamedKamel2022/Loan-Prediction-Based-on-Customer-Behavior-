import joblib
import warnings
warnings.simplefilter(action='ignore')

def status(x):
    if x == 'single':
        return [1]
    else:
        return[0]

def car(x):
    if x == 'yes':
        return [1]
    else:
        return[0]

def house(x):
    if x == 'owned':
        return [1,0]
    elif x == 'rented':
        return[0,1]
    else:
        return[0,0]


def User(data):
    
    Income = data['Income']
    Age = data['Age']
    Experience = data['Experience']
    CURRENT_JOB_YRS = data['CURRENT_JOB_YRS']
    CURRENT_HOUSE_YRS = data['CURRENT_HOUSE_YRS']
    Status = status(data['Status'])
    Car_Ownership = car(data['Car_Ownership'])
    House_Ownership = house(data['House_Ownership'])
    
    Final_Data= [Income, Age, Experience, CURRENT_JOB_YRS, CURRENT_HOUSE_YRS] + Status + Car_Ownership + House_Ownership
    return Final_Data


# data =  {'Income':100000, 'Age':30, 'Experience':10, 'CURRENT_JOB_YRS':7, 'CURRENT_HOUSE_YRS':4, 'Status':'married',
#          'Car_Ownership':'yes', 'House_Ownership':'rented'}

# Final_Data  = User(data)
# print((Final_Data))
# print()
# print(len(Final_Data))

# model = joblib.load('model.h5')
# scaler = joblib.load('scaler.h5')

# Final_Data = scaler.transform([Final_Data])
# print(Final_Data)
# print(model.predict(Final_Data)[0])