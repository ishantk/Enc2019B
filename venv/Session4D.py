def registerUser(email, password):
    print("Registration Successful")
    print(email," Email Registered with us !!")
    return 1

ack = registerUser("john@example.com", "pass123")
if(ack == 1):
    print("Click to Enter Home")
else:
    print("Enter Correct Details")