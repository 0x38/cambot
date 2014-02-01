#Run and listen for a machine to connect to receive video
#the machine must be listening when this is invoked
raspivid -vf -hf -w 1280 -h 720 -fps 20  -t 999999 -o - | nc -l 5001 &
sudo python robot.py
jobs
kill %1
