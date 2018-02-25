#!/bin/sh
until python3 sb.py; do
    echo "'python3 sb.py' crashed with exit code $?. Restarting..." >&2
    sleep 1
done
