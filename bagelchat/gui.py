from Tkinter import *
from send import *
from recv import *
from resource import *

# Inherits send and recv
class bagelchat_gui(Tk, bagelchat_send, bagelchat_recv):
    def __init__(self, parent, MULTICAST_USERNAME, MULTICAST_ADDY, MULTICAST_PORT):
        # Initialize Tkinter
        Tk.__init__(self, parent)   

        # Changes Icon
        self.wm_iconbitmap(ICON_LOCATION)
        
        # Initializes send and recv class
        bagelchat_send.__init__(self, MULTICAST_USERNAME, MULTICAST_ADDY, MULTICAST_PORT)
        bagelchat_recv.__init__(self, MULTICAST_ADDY, MULTICAST_PORT)
        
        # sends handshake to everyone to update user list
        bagelchat_send.send_handshake_join(self)
        
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
        
        # Handles close window event
        self.protocol('WM_DELETE_WINDOW', self.on_exit)
        
        # Labels for x amount of users online
        self.users_online_txt = StringVar()
        self.label_users_online = Label(self, textvariable=self.users_online_txt)
        self.label_users_online.grid(column=0, row=0)        
        self.users_online_txt.set('0 users online')
        
        # Textarea display chat
        self.log = Text(self)
        self.log.grid(column=0, row=1, columnspan=1)
        
        # Textbox entry
        self.entry = Entry(self)
        self.entry.grid(column=0, row=2, sticky='EW')
        self.entry.bind('<Return>', self.on_press_enter_txtbox) # User presses enter                            
        
        # Enable resizing
        self.grid_columnconfigure(0, weight=1)
        
        # Names window
        self.title('[bagelchat] ' + self.multicast_username + ' @ ' + self.multicast_addy + ':' + str(self.multicast_port)) + '('+ '1' + 'user(s) online)'           
        
        # Number of users online count
        self.no_users_online = 0
        
        # Is application running
        self.__running = True              
        
    # Event handler for pressing enter
    def on_press_enter_txtbox(self, event):
        bagelchat_send.send_data(self, self.entry.get()[0:255])
        self.entry.delete(0, END)
        
    # Event handler for closing window
    def on_exit(self):
        # tells everyone on the multicast that user is exiting
        bagelchat_send.send_handshake_quit(self)
        
        # Stops running application
        self.__running = False
        
        # destroys bagelchat
        bagelchat_send.__del__(self)
        bagelchat_recv.__del__(self)
        
        # destroys windows
        self.destroy()
    
    # recvs chat from other user
    def on_recv(self):        
        while self.__running:
            _data, _user_enter_exit, _users_online = bagelchat_recv.get_recv_data(self)
            
            # If data is not none
            if _data is not None:
                self.log.insert(END, _data+'\n')
                self.log.yview(END)
                
            # If received data is none, resend 'handshake' to everyone    
            else:
                if _user_enter_exit:                                       
                    
                    # Updates no of users online            
                    self.users_online_txt.set(str(_users_online) + ' user(s) online')                    
                                        
                    # If its a new user joining
                    if _users_online > self.no_users_online:
                        # Resends handshake if its a new user 
                        bagelchat_send.send_handshake_join(self)
                        
                    self.no_users_online = _users_online
            
    
# Start's gui main loop and multi-threads additional functions
def loop_gui(gui):
    try:
        thread.start_new_thread(gui.on_recv, ())
    except Exception as e:
        print e
        
    gui.mainloop()