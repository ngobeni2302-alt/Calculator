import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"], 
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
blue = "#A2A2A2"
black = "#1C1C1C"
purple = "#FFFFFF"
green = "#2D8E09"
white = "white"

#window setup

window = tkinter.Tk() #create the window 
window.title("Ntsako's Calculator") # calculator name 
window.resizable(False, False) # not to be resizable for length and width 

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background= black, foreground= white, anchor="e", width = column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text = value, font =("Arial", 30), width=column_count-1, height=1, command = lambda  value = value: button_clicked(value))
        

        if value in top_symbols:
            button.config(foreground= black, background= blue)
        elif value in right_symbols:
            button.config(foreground= purple, background= green)
        else:
            button.config(foreground= white, background=blue)
        button.grid(row= row + 1, column=column)

frame.pack()

A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None 

def remove_decimal(num):
    if num %1 == 0:
        num = int(num)
    return str(num)

def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator 


    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_decimal(numA / numB)    

                clear_all()    
                
        elif value in "÷×-+":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            operator = value

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_decimal(result)
        
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_decimal(result)

    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value 

        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value



window.mainloop()

