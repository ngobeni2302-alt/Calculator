import tkinter

button_values = [
    ["clear", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0])

#for the numbers, find a way to minimize them instead of expanding or making the move further and further 
light_grey = "#D4D4D2"
black = "#1C1C1C"
dark_grey = "#2C055A5F"
orange = "#2D8E09"
white = "white"

#window setup

window = tkinter.Tk() #create the window 
window.title("Ntsako's Calculator") # calculator name 
window.resizable(False, False) # not to be resizable for length and width 

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background= black, foreground= white)

label.grid(row  = 0, column=0)

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text = value, font =("Arial", 30), width=column_count-1, height=1, command = lambda  value = value: button_clicked(value))
        button.grid(row= row + 1, column=column)
frame.pack()

def button_clicked(value):
    pass
window.mainloop()

