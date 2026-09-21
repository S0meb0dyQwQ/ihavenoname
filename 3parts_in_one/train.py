from enum import Enum

class Train_type(Enum):
    passenger = 1
    fast = 2

class Time:
    def __init__(self, hours: int, minutes: int):
        self.hours = hours
        if int(minutes) > 60:
            self.hours += minutes//60
            self.minutes = minutes % 60
        else:
            self.minutes = minutes
    
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"
    
    def __repr__(self):
            return f"{self.hours:02d}:{self.minutes:02d}"
        
    def __lt__(self, other):
        if isinstance(other, Time):
            return self.minutes < other.minutes if self.hours == other.hours else self.hours < other.hours
        if isinstance(other, str):
            buf = other.split(":")
            thing = Time(int(buf[0]), int(buf[1]))
            return self.minutes < thing.minutes if self.hours == thing.hours else self.hours < thing.hours
    
    def __gt__(self, other):
        return not self < other
    @classmethod
    def copy(cls, other):
        return cls(other.hours, other.minutes)
    @classmethod
    def from_string(cls, str):
        parts = str.split(":")
        hour = int(parts[0])
        minute = int(parts[1])
        return cls(hour, minute)

class Train:
    def __init__(self, number, name, type: Train_type, time, road_time:int):
        self.number = number
        self.name = name
        self.time = Time.from_string(time)
        self.type = type
        self.road_time = road_time
        
    def __str__(self):
        return f"{self.number}; {self.name}; {self.type}; {self.time}; {self.road_time}"
    
    def __repr__(self):
            return f"{self.number}; {self.name}; {self.type}; {self.time}; {self.road_time}"
        
    def __lt__(self, other: Train):
        return self.time < other.time
    @classmethod
    def copy(cls, other):
        return cls(other.number, other.name, other.type, other.time, other.road_time)
    
    @classmethod
    def make_train(cls, word) -> Train:
        buf = word.split()
        return cls(buf[0], buf[1], Train_type[buf[2]], buf[3], int(buf[4]))
        