def bookCab(source, destinition, type):
    if type == 1:
        # print("Micro Cab Booked from",source,"to",destinition)
        return "Micro Cab Booked from", source, "to", destinition
    elif type == 2:
        # print("Mini Cab Booked from", source, "to", destinition)
        return "Mini Cab Booked from", source, "to", destinition
    elif type == 3:
        # print("Sedan Cab Booked from", source, "to", destinition)
        return "Sedan Cab Booked from", source, "to", destinition
    else:
        # print("Enter a Valid Choice")
        return "Enter a Valid Choice"

result = bookCab("Auribises","MBD Mall", 7)
print(result)