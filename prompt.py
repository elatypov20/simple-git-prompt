"""
This file just checks if current directory is
git repo and if it is, then in gets its current
branch and prints edited PS1 variable.
`prompt.sh` sets new PS1
"""

from subprocess import check_output, DEVNULL
from os import environ, getenv

def get_git_branch():
	branches = ''
	try:
		branches = check_output(['git', 'branch'], stderr=DEVNULL).decode()
		branches = branches.split('\n')
		branch = next(filter(lambda x: x[0] == '*', branches))
		return branch[1:].strip()
	except:
		return ''



# styles to make beatiful output
COLOR = '\u001b[33m' # yellow
BOLD  = '\u001b[1m'
END   = '\033[0m'

OPEN_PAR = '[at '
CLOSE_PAR = ']'

old_ps1 = input()

branch = get_git_branch()

if OPEN_PAR in old_ps1 and CLOSE_PAR in old_ps1: 
	before = old_ps1[:old_ps1.find(OPEN_PAR) - 1]
	after = old_ps1[old_ps1.rfind(CLOSE_PAR) + len(CLOSE_PAR):]
	
	old_ps1 = before + after

if branch != '':
	
	branch = COLOR + BOLD + branch + END + END
	
	print(f'{old_ps1[:-3]} {OPEN_PAR}{branch}{CLOSE_PAR}\\$ ', end='')
else:
	print(old_ps1, end='')
