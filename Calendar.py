
import datetime
import uuid
from icalendar import Calendar, Event, Timezone
from pytz import timezone

def makeCalendar(parsed, monday):
    durations = []
    for duration in parsed[0]:
        start, end = duration.split(' - ')
        startHours, startMinutes = map(int, start.split(':'))
        endHours, endMinutes = map(int, end.split(':'))
        durations.append(((startHours, startMinutes), (endHours, endMinutes)))

    cal = Calendar()
    data = parsed[1]

    for dayIndex in range(0, len(data)):
        day = monday + datetime.timedelta(days=dayIndex)
        lessons = data[dayIndex]
        for lessonIndex in range(0, len(lessons)):
            for lesson in lessons[lessonIndex]:
                title = lesson[0]
                subtitle = lesson[1]

                duration = durations[lessonIndex]
                start = datetime.datetime(day.year, day.month, day.day, duration[0][0], duration[0][1], tzinfo=timezone('Europe/Ljubljana'))
                end = datetime.datetime(day.year, day.month, day.day, duration[1][0], duration[1][1], tzinfo=timezone('Europe/Ljubljana'))
                stamp = datetime.datetime(day.year, day.month, day.day, duration[0][0], duration[0][1])

                event = Event()
                event.add('SUMMARY', title)
                event.add("LOCATION", subtitle)
                event.add('DTSTAMP', stamp)
                event.add('DTSTART', start)
                event.add('DTEND', end)
                event['UID'] = uuid.uuid4()
                cal.add_component(event)

    ical = cal.to_ical().decode("utf-8").splitlines()
    ical[1:1] = ['METHOD:PUBLISH', 'VERSION:2.0', 'PRODID:-//eAUrnik//1.0//SL', 'X-WR-TIMEZONE:Europe/Ljubljana', 'CALSCALE:GREGORIAN', 'BEGIN:VTIMEZONE', 'TZID:Europe/Ljubljana', 'BEGIN:DAYLIGHT', 'TZOFFSETFROM:+0100', 'RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU', 'DTSTART:19830327T020000', 'TZNAME:CEST', 'TZOFFSETTO:+0200', 'END:DAYLIGHT', 'BEGIN:STANDARD', 'TZOFFSETFROM:+0200', 'RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU', 'DTSTART:19961027T030000', 'TZNAME:CET', 'TZOFFSETTO:+0100', 'END:STANDARD', 'END:VTIMEZONE']
    formatted = "\n".join(str(x) for x in ical)

    return formatted
