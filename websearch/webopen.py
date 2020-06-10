import webbrowser
import tkinter as tk 

window=tk.Tk() 

window.title("search")
window.minsize(100,70)

def search():
    x=url.get()
    webbrowser.open(x, new=5)

label=tk.Label(window,text="enter the url",bg='grey',fg='white')
label.grid(column=0,row=1)
url=tk.StringVar()
urlentered=tk.Entry(window,width=15,bg='grey',fg='white',textvariable= url)
urlentered.grid(column=1,row=1)

button=tk.Button(window,text="search",command=search)
button.grid(column=0,row=2)



window.mainloop()
