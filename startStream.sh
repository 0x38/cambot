 raspivid -vf -t 999999 -o - | nc $1 5001
