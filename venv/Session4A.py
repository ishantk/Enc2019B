# Return Type or Acknowledgement in Functions

def mtrsToCms(mtrs):
    cms = mtrs * 100
    return cms  # Ack -> is the last statement
    print("This is Awesome") # -> will not be executed


# main thread
print("11 mtrs is",mtrsToCms(11),"cms")
print("This is Wonderful")