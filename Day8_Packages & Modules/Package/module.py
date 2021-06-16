import pyttsx3

def greetings(name):
    return "Good Morning "+name
  
def password()  :  
    a= "Lavanya@apssdc"
    b=input("confirm your password")
    if a==b:
        spk=pyttsx3.init()
        spk.say("welcome")
        spk.runAndWait()
    else:
        spk=pyttsx3.init()
        spk.say("Try again")
        spk.runAndWait()