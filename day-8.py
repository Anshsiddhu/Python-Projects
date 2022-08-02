height = float(input("What's the height of wall?\n"))
width = float(input("What's the width of wall?\n"))
def cal(height , width):
  area = height * width
  coverage = 5
  xaint2 = area / coverage
  print(f"{xaint2}")
cal(height, width)