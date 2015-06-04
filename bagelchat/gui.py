import Tkinter

class bagelchat_gui(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        
        self.initialize()
        
    def initialize(self):
        self.grid()               
        
        # Textarea display chat
        self.log = Tkinter.Text(self, state='disabled')
        self.log.grid(column=0, row=0, columnspan=2)
        
        # Textbox entry
        self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0, row=1, sticky='EW')
        self.entry.bind('<Return>', self.on_press_enter_txtbox) # User presses enter                
        
        # Button
        send_btn = Tkinter.Button(self, text=u'Send', command=self.on_send_btn_click)
        send_btn.grid(column=1, row=1)        
        
        # Enable resizing
        self.grid_columnconfigure(0, weight=1)
    
    # Event handler for send button
    def on_send_btn_click(self):
        print 'button clicked!'
        
    # Event handler for pressing enter
    def on_press_enter_txtbox(self, event):
        print 'you pressed enter!'
        
bc_gui = bagelchat_gui(None)
bc_gui.title('bagelchat')
bc_gui.mainloop()