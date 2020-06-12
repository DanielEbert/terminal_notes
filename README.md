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

### `n e NOTENAME`

Opens NOTENAME in your editor of choice (configured in notes.py, default: vim).

### `n l` or `n list`

List all NOTENAMEs.

### `n rm NOTENAME`

Delete NOTENAME.
