
temperature = int(input("Enter current room temperature: "))

if temperature > 20:
    print("It is too hot.")
elif temperature < 20:                  #elif =  else if(alternative)
    print("It is too cold.")
else:
    print("Normal temperature.")