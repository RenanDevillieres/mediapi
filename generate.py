#Generate takes a bunch of parameters (fixed or semi-fixed)
#and generates a fake userbase based on it

#To generate a userbase you have to generate a user

def gen_user(number2,country2,gender2,income2,age2,status2):
    user = {'number': number2,
    'country': number2,
    'gender': gender2,
    'ethnicity': ethnicity2,
    'income': income2,
    'age': age2,
    'status': status2,
    'confession': confession2}
    return user

#Then we create a function that takes a list of each parameter
#And generate a tuple with all the possibilities
#We will have to fill them with populations then
