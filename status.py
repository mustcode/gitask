from enum import Enum

class Status(Enum):
    requested = 1
    rejected = 2
    backlog = 3
    sprint = 4
    doing = 5
    review = 6
    check = 7
    fail = 8
    fix = 9
    done = 10
    arhived = 11
    problem = 12