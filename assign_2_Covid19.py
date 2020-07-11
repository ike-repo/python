age = input("Are you a cigarette addict older than 75 years old? Yes / No: ") == "No"
chronic = input("Do you have a severe chronic disease? Yes / No: ") == "No"
immune = input("Is your immune system too weak? Yes / No: ") == "No"
if (age) and (chronic) and (immune):
    print("You are not in risky group")
else:
    print("You are in risky group") 
