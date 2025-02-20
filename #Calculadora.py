import tkinter as Tk

def suma():
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    resultado = num1 + num2
    label_resultado.config(text= "Resultado: " + str(resultado))

def resta():
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    resultado = num1 - num2
    label_resultado.config(text= "Resultado: " + str(resultado))

def multi():
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    resultado = num1 * num2
    label_resultado.config(text = "Resultado: " + str(resultado))

def divi():
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    resultado = num1 / num2
    label_resultado.config(text = "Resultado: " + str(resultado))
    if(num1 == 0 or num2 == 2):
        print("No se puede realizar división entre 0")

def borrar():
    entry_num1.delete(0, Tk.END)
    entry_num2.delete(0, Tk.END)
    label_resultado.config(text = "Resultado: ")

def insertar_numero(num):
    app.focus_get().insert(Tk.END, num)

app = Tk.Tk()
app.title("Calculadora")

label_num1 = Tk.Label(app, text = "Num 1: ")
entry_num1 = Tk.Entry(app) 

label_num2 = Tk.Label(app, text = "Num 2: ")
entry_num2 = Tk.Entry(app)

label_resultado = Tk.Label(app, text = "Resultado: ")
entry_resultado = Tk.Entry(app)
button_suma = Tk.Button(app, text= "+", command = suma, width=5, height=1)
button_resta = Tk.Button(app, text = "-", command = resta, width=5, height=1)
button_multi = Tk.Button(app, text = "*", command= multi, width=5, height=1)
button_divi = Tk.Button(app, text = "/", command= divi, width=5, height=1)
button_borrar = Tk.Button(app, text = "Borrar", command= borrar, width=10, height=1)

for i in range(10):
    button_num = Tk.Button(app, text=str(i), command=lambda num=i: insertar_numero(num), width=5, height=1)
    if i == 0:
        button_num.grid(row=5, column=1)
    else:
        button_num.grid(row=(i-1)//3 + 2, column=(i-1)%3)

label_num1.grid(row=0, column=0, padx=5, pady=5)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

label_num2.grid(row=1, column=0, padx=5, pady=5)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

label_resultado.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

button_suma.grid(row=2, column=3)
button_resta.grid(row=3, column=3)
button_multi.grid(row=4, column=3)
button_divi.grid(row=5, column=3)
button_borrar.grid(row=6, column=3)

app.geometry("325x250")
app.mainloop()
