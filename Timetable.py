#
#  Timetable.py
#  eAUrnik
#

import Parser
import Calendar
import requests
import datetime

def get(school, class_, student):
    today = datetime.date.today()
    monday = today + datetime.timedelta(days = -today.weekday())
    if today.weekday() == 5 or today.weekday() == 6: # Saturday or Sunday
        monday += datetime.timedelta(weeks = 1)

    schoolyear = today.year
    if today.month < 8:
        schoolyear -= 1
    schoolyearStart = datetime.date(schoolyear, 9, 1)
    while schoolyearStart.weekday() == 5 or schoolyearStart.weekday() == 6:
        schoolyearStart += datetime.timedelta(days = 1)

    week = 1
    for i in range((monday - schoolyearStart).days):
        if (schoolyearStart + datetime.timedelta(days = i + 1)).weekday() == 0:
            week += 1
            
    session = requests.Session()
    session.get("https://www.easistent.com")
    
    # Remove all cookies except "vxcaccess", as they cause further requests to be rejected.
    for cookie in session.cookies:
        name = cookie.name
        if name != "vxcaccess":
            session.cookies.pop(name)
            
    URL = "https://www.easistent.com/urniki/izpis/" + school + "/" + str(class_) + "/0/0/0/" + str(week) + "/" + str(student)
    response = session.get(URL)
    
    lessons = Parser.lessons(response.content)
    timetable = Calendar.make(lessons, monday)
    
    return timetable
