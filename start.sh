#!/bin/sh
until sb.py; do
    echo "'sb.py' crashed with exit code $?. Restarting..." >&2
    sleep 1
done
#!/bin/sh
until sb.py; do
    echo "'sb.py' crashed with exit code $?. Restarting..." >&2
    sleep 1
done
