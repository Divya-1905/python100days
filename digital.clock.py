from tkinter import Label,Tk # this are the module import
import time
app_clock = Tk()
app_clock.title("digital clock")#digital clock are the arguments
app_clock.geometry('500x150')
background ="blue"
text_font =("Boulder",45,"bold")
border_width = 25
forground = 'black'
label = Label(app_clock,font=text_font,bg=background,bd=border_width)
label.grid(row=0,column=1)
def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200,digital_clock)
digital_clock()
app_clock.mainloop()#run the function to the mainloop o/p this open the window