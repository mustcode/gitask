from enum import Enum

class Action(Enum):
    approve = 1
    reject = 2
    add_field = 3
    remove_field = 4
    assign = 5
    unassign = 6
    to_backlog = 7
    to_sprint = 8
    start_work = 9
    hold_work = 10
    resume_work = 11
    finish_work = 12
    to_review = 13
    fail_review = 14
    to_check = 15
    fail_check = 16
    start_fix = 17
    to_done = 18
    to_problem = 19
    to_archive = 20