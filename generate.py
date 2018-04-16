import random

#Generate takes a bunch of parameters (fixed or semi-fixed)
#and generates a fake userbase based on it

#To generate a userbase you have to generate a user

def gen_user(number2,country2,gender2,income2,age2):
    user = {'number': number2,
    'country': number2,
    'gender': gender2,
    'ethnicity': ethnicity2,
    'income': income2,
    'age': age2}
    return user

#Then we create a function that takes a list of each parameter
#And generate a tuple with all the possibilities
#We will have to fill them with populations then

def gen_right_user(id2,database):
    rand=random.uniform(0, 1)
    j=0
    while database.cumulative[j]<rand:
        j=j+1
    country2=database.country[j]
    if rand>database.woman[j]:
        gender2='Man'
    else:
        gender2='Woman'
    meanincome2=database.income[j]
    gini2=database.gini[j]
    income2=meanincome2+random.uniform(-1,0)*meanincome2+random.uniform(0,gini2)*meanincome2
    meanage2=database.age[j]
    age2=meanage2+random.uniform(-1,0)*age2+random.uniform(0,1)*(81-meanage2)
    return gen_user(id2,country2,gender2,income2,age2)

def create_database(number,database):
    database=[]
    k=0
    while k<number :
        database.append(gen_right_user(k,database))
    return database
