import re
def rgb(r, g, b):
  for i in [r,g,b]:
    if r > 255: r = 255
    elif r < 0: r = 0
    elif g > 255: g = 255
    elif g < 0: g = 0
    elif b > 255: b = 255
    elif b < 0: b = 0
  t = "#{:02x}{:02x}{:02x}".format(r,g, b)
  result = re.findall('[a-z0-9]', t)
  result1 = ''.join(result)
    
    
  return result1.upper()

print(rgb(260, 32, 500))

def rgb(r, g, b):
    return "%02X%02X%02X" % (max(0,min(r,255)),max(0,min(g,255)),max(0,min(b,255)))