from tkinter import *
from PIL import Image, ImageTk

class WhiskyBible:
    def __init__(self):
        f = open("girwhisky.csv", "r")
        contents = f.readlines()
        f.close()

        self.whiskylist = []
        for i in range(len(contents)):
            self.whiskylist.append([j.strip() for j in contents[i].split(",")])
        
        
        root = Tk()
        canvas = Canvas(root,width=1600, height = 200, bg = "white")
        logo = Image.open("GirC.png")
        resized_image= logo.resize((200,200), Image.ANTIALIAS)
        newLogo= ImageTk.PhotoImage(resized_image)
        canvas.create_image(800, 100, image = newLogo)
        canvas.pack()
        
        frame1 = Frame(root)
        frame1.pack()
        filterlabel = Label(frame1, text = "Filter")
        filterlabel.pack()
        
        frame2 = Frame(root) #Filterradiobuttons
        frame2.pack()
        self.v1 = IntVar()
        Radiobutton(frame2, text = "Whisky", variable = self.v1, value = 0, command = self.processFilter).grid(row = 1, column = 1)
        Radiobutton(frame2, text = "Tema", variable = self.v1 , value = 1, command = self.processFilter).grid(row = 1, column = 2)
        Radiobutton(frame2, text = "Land", variable = self.v1 , value = 2, command = self.processFilter).grid(row = 1, column = 3)
        Radiobutton(frame2, text = "Vert", variable = self.v1 , value = 3, command = self.processFilter).grid(row = 1, column = 4)
        Radiobutton(frame2, text = "Møte nr", variable = self.v1 , value = 4, command = self.processFilter).grid(row = 1, column = 5)
        Radiobutton(frame2, text = "Dato", variable = self.v1 , value = 5, command = self.processFilter).grid(row = 1, column = 6)
        
        self.filterValue = 0
        
        
        frame3 = Frame(root) #Søkefelt
        frame3.pack()
        self.search = StringVar()
        Label(frame3, text = "Søk").grid(row = 1, column = 1)
        Entry(frame3, textvariable=self.search).grid(row =1,column= 2)
        Button(frame3, text = "Søk", command = self.processSearch).grid(row= 1, column = 3)
        Button(frame3, text = "Tøm", command = self.processDelete).grid(row= 1, column = 4)
        
        
        self.t = Text(root, bg = "white", height = 30, width = 200)
        self.t.pack()
    
    
    
        root.mainloop()
    
    def processFilter(self):
        value = self.v1.get()
        self.filterValue = value
    
    def processSearch(self):
        self.t.insert(END, f'{"Whisky":<40}{"Tema":<40}{"Land":<20}{"Vert":<20}{"Møte nr":<20}{"Dato":<20}\n')
        text = self.search.get().lower()
        result = []
        for i in self.whiskylist:
            check = i[self.filterValue]
            check = check.lower()
            if text in check:
                result.append([j for j in i])
        for i in result:
            self.t.insert(END, f'{i[0]:<40}{i[1]:<40}{i[2]:<20}{i[3]:<20}{i[4]:<20}{i[5]:<20}\n')
            
    def processDelete(self):
        self.t.delete('1.0', END)
        




    




WhiskyBible()


#for i in whiskylist:
#    print(i[1])