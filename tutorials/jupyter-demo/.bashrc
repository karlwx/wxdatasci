# .bashrc

# DO NOT CHANGE THIS FILE


# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
	source /etc/bashrc
fi

# Source global definitions
if [ -f /usr/global/src/user_conf/.bashrc.def ]; then
	source /usr/global/src/user_conf/.bashrc.def
fi

# PUT LOCAL BASH DEFINITIONS IN ~/.bashrc.cat

# Local definitions
if [ -f ~/.bashrc.cat ]; then
	source ~/.bashrc.cat
fi
