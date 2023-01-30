from collections import deque


def format_duration(seconds):
    if seconds == 0:
        return "now"

    counter = {"year": 0, "day": 0, "hour": 0, "minute": 0, "second": 0}

    year_time, day_time, hour_time, minute_time = 31536000, 86400, 3600, 60

    while seconds:

        if seconds >= year_time:
            years = seconds // year_time
            counter["year"] += years
            seconds -= years * year_time

        elif seconds >= day_time:
            days = seconds // day_time
            counter["day"] += days
            seconds -= days * day_time

        elif seconds >= hour_time:
            hours = seconds // hour_time
            counter["hour"] += hours
            seconds -= hours * hour_time

        elif seconds >= minute_time:
            minutes = seconds // minute_time
            counter["minute"] += minutes
            seconds -= minutes * minute_time

        else:
            counter["second"] += seconds
            seconds = 0

    counter = {k: v for k, v in counter.items() if v > 0}
    counter_lst = deque([f"{v} {k+'s'}" if v > 1 else f"{v} {k}" for k, v in counter.items()])

    result = []

    while counter_lst:

        if len(counter_lst) == 2:
            result.append(f"{counter_lst.popleft()} and {counter_lst.popleft()}")
        else:
            result.append(counter_lst.popleft())

    return ", ".join(result)

