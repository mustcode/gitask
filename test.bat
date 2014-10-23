clearlogs
deltask -a

addtask some task
addtask another task
addtask wrong task
addtask new task

deltask tasks\wrong_task

comment tasks\some_task this is a comment

setval tasks\some_task projects game
setval tasks\some_task projects side
setval tasks\some_task teams game
setval tasks\some_task teams hr
setval tasks\some_task task_type feature
setval tasks\some_task approved_by mustcode
setval tasks\some_task rejected_by eddiepocket
setval tasks\some_task status backlog
setval tasks\some_task owners mustcode
setval tasks\some_task implementers eddiepocket
setval tasks\some_task implementers mustcode
setval tasks\some_task designers eddiepocket
setval tasks\some_task testers mustcode
setval tasks\some_task observers mustcode
setval tasks\some_task supervisors mustcode
setval tasks\some_task importance 5
setval tasks\some_task urgency 3
setval tasks\some_task complexity 7
setval tasks\some_task tags fun
setval tasks\some_task tags gui

delval tasks\some_task teams hr
delval tasks\some_task projects
delval tasks\some_task task_type feature
setval tasks\some_task task_type bug

setval tasks\some_task projects game
setval tasks\some_task projects platform
setval tasks\some_task status sprint
setval tasks\some_task task_type workitem

setval tasks\another_task projects game
setval tasks\another_task projects platform
setval tasks\another_task status doing
setval tasks\another_task task_type bug

setval tasks\new_task projects game
setval tasks\new_task projects side
setval tasks\new_task status check
setval tasks\new_task task_type feature

updatetask tasks\some_task approve
updatetask tasks\some_task reject
updatetask tasks\some_task assign_role
updatetask tasks\some_task to_backlog
updatetask tasks\some_task to_sprint
updatetask tasks\some_task start_work
updatetask tasks\some_task hold_work
updatetask tasks\some_task resume_work
updatetask tasks\some_task finish_work
updatetask tasks\some_task to_check
updatetask tasks\some_task start_test
updatetask tasks\some_task fail_test
updatetask tasks\some_task start_fix
updatetask tasks\some_task to_done
updatetask tasks\some_task to_archive

clearviews
viewtasks game side status
viewtasks -f side platform task_type