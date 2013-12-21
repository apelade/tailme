tailme
======

Tail bash terminal to send zeitgeist events for Gnome Activity Journal


Developers use the bash terminal for some good stuff and it would be nice to record it like other orienting events in Gnome Activity Journal.
* Note it currently is set to ignore single quotes, otherwise crashed on some multiline input.
* That makes it mess up the output for showing colors etc.
* So, fix the tail command.

Install:
* sudo apt-get install gnome-activity-journal
* Copy tailme.sh and zeitgeist_event.py to your home directory. Chmod +x maybe.
* In zeitgeist.event, edit `MY_PROMPT` to be your bash prompt delimiter string.
* While there, notice only 'cd' command currently triggers event logging.

Run:
* Open Activity Journal by searching unity.
* Open a bash terminal.
* Enter `source ./tailme.sh`
* Enter `dir` or `ls -la`, no event in Activity Journal.
* Enter `cd ..`, creates event in Activity Journal. 

Todo: Add more commands and investigate payload and other options.

Extracting [prompt][command][args] to know what to do with the info.
Right now it only creates event for the first 'cd' command.
All the common dev and shell commands of interest could be covered.
It would be nice if Activity journal showed number of times a thing was accessed on the icon and use folder for grouping various bash commands Could do something with .bash_history too.
Some saved state between invocations would allow note of dwell time, sequences of different commands. Bash history file too maybe.
Set nice to lowest priority. Man nice.
I want to add note-to-self or todos like hotkey. Payload binary on event.
