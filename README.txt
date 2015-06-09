'''
	# bagelchat - Made by Kendrick
	# Credits:
		- Desiree for the brilliant name idea
	# CLI/GUI Lan Chat
'''

'''
Usage:

v0.1
python node.py [username] [mutlicast_address] [mutlicast_port]
'''

To do:		
	- Custom commands e.g. /quit, /asciiart, /flipcoin, etc
	- Make python arguments nicer
	- Build 'rooms' for multicasting	
	- Build a chat bot?

To fix:
	- CLI doesn't send exit message when quit

If you can't receive/send:
	- Disable firewall
	- Disable unnecessary interfaces (VMware connections etc)		
	
v0.1
	- Sends a maximum of 255 characters across LAN
	- Uses multicast to send message
	- Simple message encryption with key
	- Notifies when user has entered/leave room	
	- Build GUI
	- Knows how many user is online (for GUI)