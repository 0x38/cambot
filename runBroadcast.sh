#Run with a specific machine specified to receive video
#Requires the IP address of the listening machine
#the machine must be listening when this is invoked
raspivid -vf -hf -w 1280 -h 720 -fps 20  -t 999999 -o - | nc $1 5001 &
sudo python robot.py
jobs
kill %1
