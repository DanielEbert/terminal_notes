## Install

Add the following to your .zshrc (or .bashrc if bash is used), maybe update path to notes.py
```
function notes () { /home/user/notes/notes.py $* }
alias n='noglob notes'
```

Run `n init GIT_URL` where GIT\_URL is a git repository URL. Notes are backed up there. Can be a private repository.

## How do I use it?

### `n NOTENAME CONTENT`

Writes CONTENT to a note called NOTENAME. If notename exists already, NOTE is appended to NOTENAME.

### `n NOTENAME`

Print NOTENAME content

### `n e NOTENAME` or `n edit NOTENAME`

Opens NOTENAME in your editor of choice (configured in notes.py, default: vim).

### `n l` or `n list`

List all NOTENAMEs.

### `n g PATTERN` or `n grep PATTERN`

Search for PATTERN in all node contents. Prints the matches.

### `n rm NOTENAME`

Delete NOTENAME.
