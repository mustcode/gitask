deltask -a

addtask some task
addtask another task
addtask wrong task
addtask new task

deltask tasks\wrong_task

comment tasks\some_task this is a comment

setval tasks\some_task task_type feature
setval tasks\some_task projects game
setval tasks\some_task projects side
setval tasks\some_task teams game
setval tasks\some_task teams hr
setval tasks\some_task status backlog

delval tasks\some_task teams hr
delval tasks\some_task projects
delval tasks\some_task task_type feature
setval tasks\some_task task_type bug
setval tasks\some_task task_type workitem