import re
def validate_pin(pin):
    #return true or false
    pin.isdigit()
    if len(pin) != 4 and len(pin) != 6:
        return False
    elif re.findall("[a-zA-Z-.:/+]", pin):
        return False
    elif re.findall("['']", pin):
        return False
    else:
        return True
g = input("Enter the pin code ")
t = re.findall("[']", g)
#h = re.findall("[-.]", g)
print(t)
#print(h)
if re.findall("['123']", g):
  print("False1")
else:
  print("should check")
b = validate_pin(g)
print(b)
print(type(g))

