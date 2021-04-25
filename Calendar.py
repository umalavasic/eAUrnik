#
#  Calendar.py
#  eAUrnik
#

from ics import Calendar, Event
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

def make(parsed, monday):
    calendar = Calendar()
    calendar.creator = "eAUrnik - Fork me on GitHub: https://git.io/JO5Za"
    
    durations = []
    for duration in parsed[0]:
        start, end = duration.split(" - ")
        start_hours, start_minutes = map(int, start.split(":"))
        end_hours, end_minutes = map(int, end.split(":"))
        durations.append(((start_hours, start_minutes), (end_hours, end_minutes)))
        
    data = parsed[1]
    for day_index in range(0, len(data)):
        day = monday + timedelta(days = day_index)
        lessons = data[day_index]
        for lesson_index in range(0, len(lessons)):
            for lesson in lessons[lesson_index]:
                title = lesson[0]
                subtitle = lesson[1]
                
                duration = durations[lesson_index]
                timezone = ZoneInfo("Europe/Ljubljana")
                start = datetime(day.year, day.month, day.day, duration[0][0], duration[0][1], tzinfo = timezone)
                end = datetime(day.year, day.month, day.day, duration[1][0], duration[1][1], tzinfo = timezone)

                event = Event()
                event.name = title
                event.location = subtitle
                event.begin = start
                event.end = end
                calendar.events.add(event)

    return string(calendar)

def string(calendar):
    return "".join(calendar)
