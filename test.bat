python clearlogs.py
python deltask.py -a

python addtask.py some task
python addtask.py another task
python addtask.py wrong task
python addtask.py new task

python deltask.py tasks\wrong_task

python comment.py tasks\some_task this is a comment

python setval.py tasks\some_task projects game
python setval.py tasks\some_task projects side
python setval.py tasks\some_task teams game
python setval.py tasks\some_task teams hr
python setval.py tasks\some_task task_type feature
python setval.py tasks\some_task approved_by mustcode
python setval.py tasks\some_task rejected_by eddiepocket
python setval.py tasks\some_task status backlog
python setval.py tasks\some_task importance 5
python setval.py tasks\some_task urgency 3
python setval.py tasks\some_task complexity 7
python setval.py tasks\some_task tags fun
python setval.py tasks\some_task tags gui

python delval.py tasks\some_task teams hr
python delval.py tasks\some_task projects
python delval.py tasks\some_task task_type feature
python setval.py tasks\some_task task_type bug

python setval.py tasks\some_task projects game
python setval.py tasks\some_task projects platform
python setval.py tasks\some_task status sprint
python setval.py tasks\some_task task_type workitem

python setval.py tasks\another_task projects game
python setval.py tasks\another_task projects platform
python setval.py tasks\another_task status doing
python setval.py tasks\another_task task_type bug

python setval.py tasks\new_task projects game
python setval.py tasks\new_task projects side
python setval.py tasks\new_task status check
python setval.py tasks\new_task task_type feature

python updatetask.py tasks\some_task approve
python updatetask.py tasks\some_task reject
python updatetask.py tasks\some_task to_backlog
python updatetask.py tasks\some_task to_sprint
python updatetask.py tasks\some_task start_work
python updatetask.py tasks\some_task hold_work
python updatetask.py tasks\some_task resume_work
python updatetask.py tasks\some_task finish_work
python updatetask.py tasks\some_task to_check
python updatetask.py tasks\some_task start_test
python updatetask.py tasks\some_task fail_test
python updatetask.py tasks\some_task start_fix
python updatetask.py tasks\some_task to_done
python updatetask.py tasks\some_task to_archive

python assign.py tasks\some_task eddiepocket owner
python assign.py tasks\some_task mustcode implementer
python assign.py tasks\some_task mustcode tester
python assign.py -r tasks\some_task mustcode tester

python clearviews.py
python viewtasks.py game side status
python viewtasks.py -f side platform task_type