'''
	# bagelchat - Made by Kendrick
	# CLI Lan Chat (hopefully with encryption)
'''

To do:

To fix:

Encountering problems:
	- Disable firewall
	- Disable unnecessary interfaces (VMware connections etc)

Structure:
	- Every node maintains a list of known peers
	- Messages are sent with TCP to all known peers
	- When a node starts up, it sends out an UDP broadcast to discover other nodes
	- When a node receives a discovery broadcast, it sends 'itself' to the source of the broadcast, in order to make itself known. The receiving node adds the broadcaster to it's own list of known peers
	- When a node drops out of the network, it sends another broadcast in order to inform the remaining nodes that they should remove the dropped client from their list
	
	