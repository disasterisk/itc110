# This program says hello and asks for name and age
print ('Hello world!')
print ('What is your name?') # ask for name
name = input()
print ('It\'s nice to meet you, '+ name)
print ('Did you know that your name is '+str(len(name))+' letters long?')
print ('How old are you?') # ask for age
age = input()
print ('That\'s like '+str(int(age)*7)+' in dog years.')
