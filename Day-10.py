year1 = int(input("Enter a year: "))
month = int(input("Enter a month: "))
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("true")
      else:
        print("false")
    else:
      print("true")
  else:
    print("false")
leap_year1 = is_leap(year1)
def days_in_month():
  month_days = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if leap_year1 == "true" and month == 2:
      return 29
  return month_days[month]
print(f"Number of days in month {month} = {days_in_month()} ")
      
