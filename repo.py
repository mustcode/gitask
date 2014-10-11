import subprocess

def pull():
    subprocess.call('git pull origin master')

def commit():
    changes = subprocess.getoutput('git status --short')
    if not changes:
        return
    subprocess.call('git add --all .')
    commitMsg = subprocess.getoutput('git status --short')
    subprocess.call('git commit -m "{0}"'.format(commitMsg))

def push():
    subprocess.call('git push -u origin master')

def sync():
    pull()
    commit()
    push()
