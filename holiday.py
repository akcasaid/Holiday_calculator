def isLeapYear(year):
   
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True 
    else:
        return False    

def daysInMonth(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            return 30

def nextDay(year, month, day , dayname):
         
    if dayname=='monday':
        dayname = 'tuesday'
    elif dayname =='tuesday':
        dayname = 'wednasday'
    elif dayname=='wednasday':
        dayname ='thursday'
    elif dayname=='thursday':
        dayname='friday'
    elif dayname =='friday':
        dayname = 'saturday'
    elif dayname=='saturday':
        dayname ='sunday'
    elif dayname=='sunday':
        dayname ='monday'
       
    if day < daysInMonth(year, month):
        return year, month, day + 1 , dayname
    else:
        if month < 12:
            return year, month + 1,1 ,dayname         
        else:
            return year + 1, 1, 1,dayname

  

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    # Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False.
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
    

def isholiday(day,month,year,dayname):
    holiday=[[1,1],[23,4],[1,5],[15,7],[30,8],[29,9]]
    if dayname == 'saturday' or dayname=='sunday'or [day,month] in holiday:
        return True
    else :
        return False

def totolholiday(year1, month1, day1, dayname , year2, month2, day2):
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1,dayname = nextDay(year1, month1, day1, dayname)
        if isholiday (day1,month1,year1,dayname):
            days += 1
    return days


print (totolholiday(2020,1,1,"monday",2024,2,2))