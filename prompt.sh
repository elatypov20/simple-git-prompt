#!/bin/bash

cd(){
	builtin cd $1
	PS1=$(echo "$PS1" | python3 ~/.simple-git-prompt/prompt.py) 
}

git(){
	/usr/bin/git "$@"
	cd .
}