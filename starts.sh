#!/bin/sh
until python3 sb.py; do
    echo "'[PROGRAM CRASHED]' Exit Code : $?. Restartin program!" >&2
    sleep 1
done
