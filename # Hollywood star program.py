# Hollywood star program


import tkinter 
import tkinter.font 


class MyGUI: 
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.canvas = tkinter.Canvas(self.main_window, width=400, height=400)
        
        #creating the star and the text
        self.star_id = self.canvas.create_polygon(200, 50, 250, 150, 150, 100, 250, 100, 160, 150, fill='yellow')
        self.text_id = self.canvas.create_text( 200, 200, text = 'Emmanuel',
                   font=("Times New Roman", 25), fill='black')
        
        self.my_button = tkinter.Button(self.main_window, text = "Change Colors", command=self.change_colors)
        
        # Original colors
        self.star_color = 'yellow'
        self.text_color = 'black'
        
        #packing
        self.canvas.pack()
        self.my_button.pack()
        
        
        self.main_window.mainloop()

    def change_colors(self):
        if self.star_color == 'yellow':
            self.canvas.itemconfig(self.star_id, fill='black')
            self.canvas.itemconfig(self.text_id, fill='white')
            
            self.star_color = 'black'
            self.text_color = 'white'
        
        else:
         self.canvas.itemconfig(self.star_id, fill='yellow')
         self.canvas.itemconfig(self.text_id, fill='black')

         self.star_color = 'yellow'
         self.text_color = 'black'
    
         
        
        
if __name__ == '__main__':
    my_gui = MyGUI()
    