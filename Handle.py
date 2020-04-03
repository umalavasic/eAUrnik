
import requests
import datetime
from dateutil import rrule
from Parse import parse
from Calendar import makeCalendar

def handle(sola, razred, dijak):
    today = datetime.datetime.today()
    monday = today + datetime.timedelta(days = -today.weekday())
    if today.weekday() == 5 or today.weekday() == 6:
        monday += datetime.timedelta(weeks = 1)

    schoolyear = today.year
    if today.month < 8:
        schoolyear -= 1
    schoolyearStart = datetime.date(schoolyear, 9, 1)
    while schoolyearStart.weekday() == 5 or schoolyearStart.weekday() == 6:
        schoolyearStart += datetime.timedelta(days=1)

    teden = rrule.rrule(rrule.WEEKLY, dtstart=schoolyearStart, until=monday).count()
    URL = "https://www.easistent.com/urniki/izpis/" + sola + "/" + str(razred) + "/0/0/0/" + str(teden) + "/" + str(dijak)
    page = requests.get(URL)
    parsed = parse(page)

    if not parsed:
        return
    else:
        return makeCalendar(parsed, monday)
