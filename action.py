from enum import Enum

class Action(Enum):
    approve = 1
    reject = 2
    assign = 3
    unassign = 4
    to_backlog = 5
    to_sprint = 6
    start_work = 7
    hold_work = 8
    resume_work = 9
    finish_work = 10
    to_review = 11
    fail_review = 12
    to_check = 13
    fail_check = 14
    start_fix = 15
    to_done = 16
    to_problem = 17
    to_archive = 18