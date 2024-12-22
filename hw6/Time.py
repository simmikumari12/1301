class Time():
    def __init__(self, hour, minute, ampm):
        self._hour = hour
        self._minute = minute
        self._ampm = ampm  # 'AM' or 'PM'

    def next(self):
        """Returns the time 1 minute after the current time."""
        if self._hour == 11 and self._minute == 59:
            if self._ampm == 'AM':
                return Time(12, 0, 'PM')
            else:
                return Time(12, 0, 'AM')
        elif self._hour == 12 and self._minute == 59:
            return Time(1, 0, self._ampm)
        elif self._minute == 59:
            return Time(self._hour + 1, 0, self._ampm)
        else:
            return Time(self._hour, self._minute + 1, self._ampm)

    def previous(self):
        """Returns the time 1 minute before the current time."""
        if self._hour == 12 and self._minute == 0:
            if self._ampm == 'AM':
                return Time(11, 59, 'PM')
            else:
                return Time(11, 59, 'AM')
        elif self._minute == 0:
            return Time(self._hour - 1, 59, self._ampm)
        else:
            return Time(self._hour, self._minute - 1, self._ampm)

    def add(self, nminutes):
        """Returns the time n minutes after the current time."""
        t = Time(self._hour, self._minute, self._ampm)
        for _ in range(nminutes):
            t = t.next()
        return t

    def sub(self, nminutes):
        """Returns the time n minutes before the current time."""
        t = Time(self._hour, self._minute, self._ampm)
        for _ in range(nminutes):
            t = t.previous()
        return t

    def minutes_since_midnight(self):
        """Returns the number of minutes since midnight."""
        total_minutes = self._hour * 60 + self._minute
        if self._ampm == 'PM' and self._hour != 12:
            total_minutes += 720  # 12 hours in minutes for PM
        elif self._ampm == 'AM' and self._hour == 12:
            total_minutes -= 720  # subtract 12 hours for midnight
        return total_minutes

    def after(self, t):
        """Returns True if the current time is after t."""
        return self.minutes_since_midnight() > t.minutes_since_midnight()

    def equals(self, t):
        """Returns True if the current time is equal to t."""
        return self._hour == t._hour and self._minute == t._minute and self._ampm == t._ampm

    def before(self, t):
        """Returns True if the current time is before t."""
        return self.minutes_since_midnight() < t.minutes_since_midnight()

    def minutes_between(self, t):
        """Returns the number of minutes between the current time and t."""
        return abs(self.minutes_since_midnight() - t.minutes_since_midnight())

    def __str__(self):
        """Returns a string representation of the time in HH:MMAM/PM format."""
        def two_digits(n):
            return f"{n:02d}"

        return f"{two_digits(self._hour)}:{two_digits(self._minute)}{self._ampm}"
