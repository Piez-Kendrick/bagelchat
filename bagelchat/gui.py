from Tkinter import *
from send import *
from recv import *

# Inherits send and recv
class bagelchat_gui(Tk, bagelchat_send, bagelchat_recv):
    def __init__(self, parent, MULTICAST_USERNAME, MULTICAST_ADDY, MULTICAST_PORT):
        # Initialize Tkinter
        Tk.__init__(self, parent)                
        
        # Initializes send and recv class
        bagelchat_send.__init__(self, MULTICAST_USERNAME, MULTICAST_ADDY, MULTICAST_PORT)
        bagelchat_recv.__init__(self, MULTICAST_ADDY, MULTICAST_PORT)
        
        # Keeps an instance of the parent
        self.parent = parent
        
        # Keeps an instance of username, multicast_addy, multicast_port
        self.multicast_username = MULTICAST_USERNAME
        self.multicast_addy = MULTICAST_ADDY
        self.multicast_port = MULTICAST_PORT
        
        # Initializes
        self.initialize()
        
    # initializes GUI components
    def initialize(self):
        self.grid()               
        
        # Textarea display chat
        self.log = Text(self)
        self.log.grid(column=0, row=0, columnspan=1)
        
        # Textbox entry
        self.entry = Entry(self)
        self.entry.grid(column=0, row=1, sticky='EW')
        self.entry.bind('<Return>', self.on_press_enter_txtbox) # User presses enter                            
        
        # Enable resizing
        self.grid_columnconfigure(0, weight=1)
        
        # Names window
        self.title('['+ self.multicast_username +'] bagelchat @ ' + self.multicast_addy + ':' + str(self.multicast_port))               
        
    # Event handler for pressing enter
    def on_press_enter_txtbox(self, event):
        bagelchat_send.send_data(self, self.entry.get()[0:255])
        self.entry.delete(0, END)
    
    # recvs chat from other user
    def on_recv(self):        
        while True:
            _data = bagelchat_recv.get_recv_data(self)
            if _data is not None:
                self.log.insert(END, _data+'\n')
            
    
# Start's gui main loop and multi-threads additional functions
def loop_gui(gui):
    try:
        thread.start_new_thread(gui.on_recv, ())
    except Exception as e:
        print e
        
    gui.mainloop()