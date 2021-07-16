all:
	# install prompt
	mkdir -p ~/.simple-git-prompt
	chmod +x prompt.sh
	cp prompt.sh ~/.simple-git-prompt
	cp prompt.py ~/.simple-git-prompt
	echo >> ~/.bashrc
	echo "source ~/.simple-git-prompt/prompt.sh" >> ~/.bashrc
	echo "cd ." >> ~/.bashrc