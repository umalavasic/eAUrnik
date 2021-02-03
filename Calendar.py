#
#  Calendar.py
#  eAUrnik
#

from ics import Calendar, Event
import datetime

def make(parsed, monday):
    calendar = Calendar()
    
    durations = []
    for duration in parsed[0]:
        start, end = duration.split(" - ")
        start_hours, start_minutes = map(int, start.split(":"))
        end_hours, end_minutes = map(int, end.split(":"))
        durations.append(((start_hours, start_minutes), (end_hours, end_minutes)))
        
    data = parsed[1]
    for day_index in range(0, len(data)):
        day = monday + datetime.timedelta(days = day_index)
        lessons = data[day_index]
        for lesson_index in range(0, len(lessons)):
            for lesson in lessons[lesson_index]:
                title = lesson[0]
                subtitle = lesson[1]
                
                duration = durations[lesson_index]
                start = datetime.datetime(day.year, day.month, day.day, duration[0][0], duration[0][1])
                end = datetime.datetime(day.year, day.month, day.day, duration[1][0], duration[1][1])

                event = Event()
                event.name = title
                event.location = subtitle
                event.begin = start
                event.end = end
                calendar.events.add(event)

    return calendar

def string(calendar):
    return "\n".join(calendar)
