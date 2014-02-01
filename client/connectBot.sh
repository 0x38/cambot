#Takes the IP address of the bot as an argument, bot should be listening already
nc $1 5001 | mplayer -fps 40   -demuxer h264es -
