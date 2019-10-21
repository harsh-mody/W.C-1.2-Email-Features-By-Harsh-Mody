enteredEmail = input("Please Enter A Email Id : ")
if enteredEmail.__contains__(".com"):
    if enteredEmail.__contains__("@gmail.com"):
        enteredEmailId = enteredEmail.replace('@gmail.com', '')
        if enteredEmailId.__contains__("+"):
            sep = '+'
            outputEmailId = enteredEmailId.split(sep, 1)[0]
            finalOutputEmail = outputEmailId + "@gmail.com"
            print("Your Output Email Is : ", finalOutputEmail)
        elif enteredEmailId.__contains__("."):
            finalOutputEmailId = enteredEmailId.translate({ord('.'): None})
            finalOutputEmail = finalOutputEmailId + "@gmail.com"
            print("Your Output Email Is : ", finalOutputEmail)
        else:
            print("Your Output Email Is : ", enteredEmail)
    else:
        print("Your Output Email Is : ", enteredEmail)
else:
    print("Please Enter a Valid Email Address.")




