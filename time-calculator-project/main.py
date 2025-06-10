def add_time(start, duration, weekday=None):
    # find start time in numbers
    time, am_pm = start.split(' ')
    time_hrs, time_mins = split_duration(time)
    duration_hrs, duration_mins = split_duration(duration)
    
    # convert start time to 24-hour time
    if am_pm == 'PM':
        time_hrs += 12
    else:
        pass

    # add duration
    new_hrs = time_hrs + duration_hrs
    new_mins = time_mins + duration_mins
    if new_mins > 60:
        new_mins = new_mins - 60
        new_hrs += 1

    # find new time is AM or PM and calculate days ahead
    days_ahead = new_hrs // 24

    # convert new time to 24-hour time
    new_hrs %= 24
    
    # find new time is AM or PM
    # [0 - 11] AM, [12 - 23] PM
    new_am_pm = "AM" if new_hrs < 12 else "PM"

    # calculate new 12-hour time
    if new_hrs == 24 or new_hrs == 12 or new_hrs == 0:
        new_hrs = 12
    else:
        new_hrs = new_hrs % 12
    
    # output new time, with leading 0 for mins
    if new_mins < 10:
       new_time = f'{new_hrs}:0{new_mins} {new_am_pm}'
    else: 
        new_time = f'{new_hrs}:{new_mins} {new_am_pm}'

    if weekday:
        # calculate new day of week
        weekdays = [
            'Monday', 
            'Tuesday', 
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ]
        weekday_index = [day.lower() for day in weekdays].index(weekday.lower())
        # calculate new weekday ignoring weeks
        weekday_index += days_ahead
        weekday_index %= 7
        new_time += f', {weekdays[weekday_index]}'

    if days_ahead == 0:
        pass
    elif days_ahead == 1:
        new_time += ' (next day)'
    else:
        new_time += f' ({days_ahead} days later)'

    return new_time

def split_duration(duration): 
    """Splits a duration string 'HH:MM' into hours and minutes.""" 
    hours, minutes = map(int, duration.split(":")) 
    return hours, minutes

print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'Monday'))
print(add_time('11:43 AM', '00:20'))
print(add_time('10:10 PM', '3:30'))
print(add_time('11:43 PM', '24:20', 'tueSday'))
