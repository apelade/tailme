
[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm" # Load RVM into a shell session *as a function*

GIT_PS1_SHOWDIRTYSTATE=1
GIT_PS1_SHOWUNTRACKEDFILES=1
GIT_PS1_SHOWSTASHSTATE=1
export PS1='\w\[\033[01;34m\]$(__git_ps1 " (%s)")\[\033[00m\] $ '

# If this is an xterm set the title to user@host:dir
case "$TERM" in
    xterm*|rxvt*)
        PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

source ./tailme.sh


#if ! (ps -ef | grep "tail -F -n-0 typescript.txt" | grep -v grep); then
#  echo "already tailing typescript.txt for zeitgesit_event.py"
#else
#  #tail -F -n-0 typescript.txt | xargs -I {} python zeitgeist_event.py {}
#fi


# execif > >(tee logfile.txt)
# script -at typescript.txt 2> timings.txt
# ctrl+d to exit or type exit
# scriptreplay timings.txt typescript
#export AUTOFEATURE=true
