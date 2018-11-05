from main import *
from Functions import *
# ==================================================
# ==================================================
# START PRIMARY TK CLASS      PRIMARY TK CLASS        PRIMARY TK CLASS
# ==================================================
class Steganography(tk.Tk):
    # Current Py file Directory
    # /Users/nct/Dropbox/ComputerScience/tkinter/NCTStudyApp/NCTStudyApp.py
    # =================
    # Current txt file Directory
    # /Users/nct/Dropbox/ComputerScience/tkinter/NCTStudyApp/NCTStudyApp.txt
    # =================
    '''
    Note: This is our primary page container format/configuration page for all pages.
        Set geometry, title, image(not working though)

        We have a menu that is not being used at the momemnt.

        We have a popup message coming from the menu selection, just for show at the moment.


     __init__ implies that this will be run automatically if the class is called.
         other def methods will not run automatically.
            args = arguments = open ended, you can pass whatever you want through
            kwargs = key-word arguments, basically dictionaries.
     '''
    def __init__(self, *args, **kwargs):
        # Now initialize tkinter also.
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.title(self, "NCT's Steganography App")
        tk.Tk.geometry(self, "1200x1000")
        # Can't get the icon to show, now just a png icon
        # Resized to 12/16 pixels
        tk.Tk.iconbitmap(self, "icon.png")
        # =================
        # =================
        # =================
        # =================
        # =================
        container = ttk.Frame(self)
        # Making a quick window, use pack, for more detailed, use grid
        # side= What side do you want this on.
        # fill= Fill the entire space
        # expand= If there is any more white space in the window. Use it.
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Menubar block created in file 9
        # Create an overall menubar, and assign to this tkinter
        menuBar1 = tk.Menu(container)
        # Adding a tearoff divider into the menu that drops down
        fileMenu1 = tk.Menu(menuBar1, tearoff=0)
        # Now actually place a literal piece on the menubar
        menuBar1.add_cascade(label="File", menu=fileMenu1)


        fileMenu1.add_separator()
        # Create a 2nd subpiece under the File Tab
        # Remember this is for the file tab, not the page buttons
        fileMenu1.add_command(label="Steganography", command=lambda: self.show_frame())



        # ==================================================
        tk.Tk.config(self, menu=menuBar1)
        # ----------------------------------------------------

        # ==================================================
        # Specify a dictionary here
        self.frames = {}
        # We will have numerous windows, and either click/button will bring another.
        # One application with numerous windows.
        # ==================================================
        # ==================================================
        # ==================================================
        # ==================================================
        # ==================================================
        # ===================FOR PAGE LOOP===============================
        # For loop that ranges in our page limits
        # Make sure to add any new page to our tuple for loop
        for F in (StartPage, ):
            # Use F so that we can progress through our pages.
            frame = F(container, self)
            self.frames[F] = frame
            # grid is more specific compared to pack.
            # sticky is using North/South/East/West -->
            #    will stretch to the size of the window.
            #       if you just use ew then it will stretch all to the sides.
            frame.grid(row=0, column=0, sticky="nsew")
        # ==================================================
        # ==================================================
        self.show_frame(StartPage)
        # ==================================================
        # ==================================================
        # Set function to show a frame for a specific page.

    def show_frame(self, controller1):
        # self.frames is looking at the frame dictionary that we created above.
        #       Controller is which frame we want to access
        frame = self.frames[controller1]
        # Then we will run a library function on the frame.
        frame.tkraise()
    # ==================================================
    # END PRIMARY TK CLASS      PRIMARY TK CLASS        PRIMARY TK CLASS
    # ==================================================
    # ==================================================
    # ==================================================
    # ==================================================
    # ==================================================
    # ==================================================
# ==================================================
# END PRIMARY TK CLASS      PRIMARY TK CLASS        PRIMARY TK CLASS
# ==================================================
# ==================================================
# ==================================================
# START PAGES PAGES PAGES PAGES PAGES PAGES PAGES
# START PAGES PAGES PAGES PAGES PAGES PAGES PAGES
# START PAGES PAGES PAGES PAGES PAGES PAGES PAGES
# ==================================================
# ==================================================
class StartPage(ttk.Frame):


    '''
    START PAGE
        Note: this page is on the pack format, not the grid
        Current: 5 Buttons - take user to page, or close program
            1) Start Page
                    Used for buttons and initial selections

            5) Quit Program


    '''
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start Page", font=XL_FONT)
        label.pack(padx=10, pady=10)


        startPage_UserSelect_InitialPhoto = ttk.Button(self, text="Select Photo",
                                                       command=lambda: get_photoName(), width=15)
        startPage_UserSelect_InitialPhoto.pack(pady=(10, 10))

        startPage_UserSelect_InitialPhoto = ttk.Button(self, text="Input Secret Message", width=15)
        startPage_UserSelect_InitialPhoto.pack(pady=(10, 10))

        startPage_UserSelect_InitialPhoto = ttk.Button(self, text="Encypt", width=15)
        startPage_UserSelect_InitialPhoto.pack(pady=(10, 10))

        startPage_UserSelect_InitialPhoto = ttk.Button(self, text="Embedd", width=15)
        startPage_UserSelect_InitialPhoto.pack(pady=(10, 10))

# ==================================================
# ==================================================
# ==================================================