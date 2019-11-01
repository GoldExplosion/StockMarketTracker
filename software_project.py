from tkinter import *
import Display3
root = Tk()
root.title("STOCKZ")
heading=Label(root, 
		 text="STOCKZ\n Invest and Innovate\n",
                 font=5,
                 bg="yellow",
         width=200)
heading.pack()
space=Label(root,text="\n\n")
space.pack()

heading1=Label(root, 
		 text="Select the stock company: \n",
                 font=5)
heading1.pack()

url1="https://finance.yahoo.com/quote/GOOG/"
url2="https://finance.yahoo.com/quote/AMZN/"
url3="https://finance.yahoo.com/quote/WMT/"
url4="https://finance.yahoo.com/quote/NKE/"
url5="https://finance.yahoo.com/quote/AAPL/"
url6="https://finance.yahoo.com/quote/005930.KS/"
button1 = Button(root, text='GOOGLE', width=25, command=lambda: Display3.Display(url1)) 
button1.pack()
button1 = Button(root, text='AMAZON', width=25, command=lambda: Display3.Display(url2)) 
button1.pack()
button1 = Button(root, text='WALMART', width=25, command=lambda: Display3.Display(url3)) 
button1.pack()
button1 = Button(root, text='NIKE', width=25, command=lambda: Display3.Display(url4)) 
button1.pack()
button1 = Button(root, text='APPLE', width=25, command=lambda: Display3.Display(url5)) 
button1.pack()
button1 = Button(root, text='SAMSUNG', width=25, command=lambda: Display3.Display(url6)) 
button1.pack()
space1=Label(root,text="\n\n\n")
space1.pack()
button = Button(root, text='PORTFOLIO', width=25, command="NONE") 
button.pack()

root.mainloop()
