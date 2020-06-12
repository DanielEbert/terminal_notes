#!/usr/bin/env python3

import os
import sys
import json
import subprocess
import editor


git_dir = '/home/user/.notes'
os.environ['EDITOR'] = '/usr/bin/vim'


def init(git_url):
  if os.path.isdir(git_dir):
    print(f'notes init failed, {git_dir} exist already.')
  if os.system(f'git clone {git_url} {git_dir}') != 0:
    print('notes init failed, cloning repo failed.')


def git_push():
  subprocess.Popen(f'cd {git_dir} && git add . && git commit -m "1" && git push -q', 
                   shell=True, stdout=subprocess.DEVNULL)


def git_pull():
  subprocess.check_call(f'cd {git_dir} && git pull', shell=True)


def main():
  args = sys.argv[1:]
  if len(args) == 1:
    if args[0] == 'p' or args[0] == 'pull':
      git_pull()
    elif args[0] == 'l' or args[0] == 'list':
      subprocess.check_call(['ls', git_dir])
    elif args[0] == 'b' or args[0] == 'backup':
      git_push()
    else:
      maybe_file = os.path.join(git_dir, args[0])
      if os.path.isfile(maybe_file):
        with open(maybe_file, 'r') as f:
          print(f.read())
  elif len(args) >= 2 and args[0] == 'g' or args[0] == 'grep':
    os.system(f'grep -- {" ".join(args[1:])} {os.path.join(git_dir, "*")}')
  elif len(args) == 2:
    if args[0] == 'init':
      init(args[1])
    elif args[0] == 'e' or args[0] == 'edit':
      # edit file in vim
      filename = os.path.join(git_dir, args[1])
      editor.edit(filename)
      git_push()
    elif args[0] == 'rm':
      filename = os.path.join(git_dir, args[1])
      if not os.path.isfile(filename):
        print(f'No Note with name {argv[1]}')
      else:
        os.remove(filename)
        git_push()
  elif len(args) > 2:
    filename = os.path.join(git_dir, args[0])
    content = ' '.join(args[1:])
    if os.path.isfile(filename):
      with open(filename, 'a') as f:
        f.write('\n\n' + content)
    else:
      with open(filename, 'w') as f:
        f.write(content)
    git_push()
    

if __name__ == '__main__':
  exit(main())
