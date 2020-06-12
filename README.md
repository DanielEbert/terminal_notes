Add the following to your .zshrc (or .bashrc if bash is used), maybe update path to notes.py
```
function notes () { /home/user/notes/notes.py $* }
alias n='noglob notes'
```
