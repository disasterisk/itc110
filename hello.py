# This program says hello and asks for name and age
print ('Hello world!')
print ('What is your name?') # ask for name
name = input()
print ('It\'s nice to meet you, '+ name)
print ('Did you know that your name is '+str(len(name))+' letters long?')
print ('How old are you?') # ask for age
age = int(input())
if age < 2:
    print("You are excellent with a command line for your age.")
else:
    dogAge = 21+((age-2)*4)
    print ('That\'s like '+str(dogAge)+' in dog years.')
