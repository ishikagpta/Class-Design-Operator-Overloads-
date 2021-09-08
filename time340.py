# TimeSpan class stores a duration of time in seconds, minutes, hours and
# represents it as hours, minutes, and seconds. It does appropriate calculations
# on time durations as needed.
class TimeSpan:


    def __init__(self, seconds = 0, minutes = 0, hours = 0):
        self.__totalSeconds = int(seconds + (minutes * 60) + (hours * 3600))
        self.__hours = int(self.__totalSeconds // 3600)
        self.__totalSeconds = int(self.__totalSeconds - (self.__hours * 3600))
        self.__minutes = int(self.__totalSeconds // 60)
        self.__totalSeconds = int(self.__totalSeconds - (self.__minutes * 60))
        self.__seconds = int(self.__totalSeconds)

    # This function converts hours, minutes, and seconds values to the total amount of seconds and returns it
    def __getTotalSeconds__(self):
        self.__totalSeconds = int(self.getSeconds() + (self.getMinutes() * 60) \
                                  + (self.getHours() * 3600))
        return int(self.__totalSeconds)

    # This function converts the total seconds into hours and returns it
    def __getTotalHours__(self):
        self.__hours = int(self.__totalSeconds // 3600)
        return self.__hours

    def getHours(self):
        return self.__hours

    def getMinutes(self):
        return self.__minutes

    def getSeconds(self):
        return self.__seconds

    def setTime(self, seconds, minutes, hours):
        self.__seconds = seconds
        self.__minutes = minutes
        self.__hours = hours
        self.__totalSeconds = self.__getTotalSeconds__()
        self.__hours = int(self.__totalSeconds // 3600)
        self.__totalSeconds = int(self.__totalSeconds - (self.__hours * 3600))
        self.__minutes = int(self.__totalSeconds // 60)
        self.__totalSeconds = int(self.__totalSeconds - (self.__minutes * 60))
        self.__seconds = int(self.__totalSeconds)

    def __str__(self):
        return "Hours: " + str(self.__hours) + ", Minutes: " \
               + str(self.__minutes) + ", Seconds: " + str(self.__seconds)

    def __add__(self, other):
        __otherTotalSeconds = other.__getTotalSeconds__()
        __selfTotalSeconds = self.__getTotalSeconds__()
        __totalSeconds = __selfTotalSeconds + __otherTotalSeconds
        __hours = __totalSeconds // 3600
        __totalSeconds = __totalSeconds - (__hours * 3600)
        __minutes = __totalSeconds // 60
        __totalSeconds = __totalSeconds - (__minutes * 60)
        __seconds = __totalSeconds
        return TimeSpan(__seconds, __minutes, __hours)

    def __sub__(self, other):
        __otherTotalSeconds = other.__getTotalSeconds__()
        __selfTotalSeconds = self.__getTotalSeconds__()
        __totalSeconds = __selfTotalSeconds - __otherTotalSeconds
        __hours = __totalSeconds // 3600
        __totalSeconds = __totalSeconds - (__hours * 3600)
        __minutes = __totalSeconds // 60
        __totalSeconds = __totalSeconds - (__minutes * 60)
        __seconds = __totalSeconds
        return TimeSpan(__seconds, __minutes, __hours)

    def __eq__(self, other):
        __otherTotalSeconds = other.__getTotalSeconds__()
        __selfTotalSeconds = self.__getTotalSeconds__()
        return __selfTotalSeconds == __otherTotalSeconds

    def __lt__(self, other):
        __otherTotalSeconds = other.__getTotalSeconds__()
        __selfTotalSeconds = self.__getTotalSeconds__()
        return __selfTotalSeconds < __otherTotalSeconds

    def __le__(self, other):
        __otherTotalSeconds = other.__getTotalSeconds__()
        __selfTotalSeconds = self.__getTotalSeconds__()
        return __selfTotalSeconds <= __otherTotalSeconds

    def __gt__(self, other):
        __otherTotalSeconds = other.__getTotalSeconds__()
        __selfTotalSeconds = self.__getTotalSeconds__()
        return __selfTotalSeconds > __otherTotalSeconds

    def __ge__(self, other):
        __otherTotalSeconds = other.__getTotalSeconds__()
        __selfTotalSeconds = self.__getTotalSeconds__()
        return __selfTotalSeconds >= __otherTotalSeconds

    def __ne__(self, other):
        __otherTotalSeconds = other.__getTotalSeconds__()
        __selfTotalSeconds = self.__getTotalSeconds__()
        return __selfTotalSeconds != __otherTotalSeconds

    def __neg__(other):
        __otherHours = -1 * other.__hours
        __otherMinutes = -1 * other.__minutes
        __otherSeconds = -1 * other.__seconds
        return "Hours: " + str(__otherHours) + ", Minutes: " \
               + str(__otherMinutes) + ", Seconds: " + str(__otherSeconds)
