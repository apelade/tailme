#! /bin/bash

if ! (ps -ef | grep "tail -F -n-0 typescript.txt" | grep -v grep > /dev/null); then
  echo "Start tailing typescript.txt for zeitgesit_event.py"
  tail -F -n-0 typescript.txt | xargs -0 -I {} python zeitgeist_event.py {} &
else
  echo "Already tailing typescript"
fi

script -af typescript.txt
