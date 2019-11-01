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
space=Label(root,text="")
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
url7="https://finance.yahoo.com/quote/ADS.DE/"
url8="https://finance.yahoo.com/quote/FOSL/"
url9="https://finance.yahoo.com/quote/GM/"
url10="https://in.finance.yahoo.com/quote/DELL/"
url11="https://finance.yahoo.com/quote/GS/"
url12="https://finance.yahoo.com/quote/PUM.DE/"
url13="https://finance.yahoo.com/quote/LEVI/"
url14="https://finance.yahoo.com/quote/KO/"
url15="https://finance.yahoo.com/quote/HPE/"
url16="https://in.finance.yahoo.com/quote/NESTLEIND.NS/"
url17="https://finance.yahoo.com/quote/YUM/"
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
button1 = Button(root, text='ADIDAS', width=25, command=lambda: Display3.Display(url7)) 
button1.pack()
button1 = Button(root, text='FOSSIL', width=25, command=lambda: Display3.Display(url8)) 
button1.pack()
button1 = Button(root, text='CHEVROLET', width=25, command=lambda: Display3.Display(url9)) 
button1.pack()
button1 = Button(root, text='DELL', width=25, command=lambda: Display3.Display(url10)) 
button1.pack()
button1 = Button(root, text='GOLDMANN SACHS', width=25, command=lambda: Display3.Display(url11)) 
button1.pack()
button1 = Button(root, text='PUMA', width=25, command=lambda: Display3.Display(url12)) 
button1.pack()
button1 = Button(root, text='LEVIS', width=25, command=lambda: Display3.Display(url13)) 
button1.pack()
button1 = Button(root, text='COCACOLA', width=25, command=lambda: Display3.Display(url14)) 
button1.pack()
button1 = Button(root, text='HEWLETT PACKARD', width=25, command=lambda: Display3.Display(url15)) 
button1.pack()
button1 = Button(root, text='NESTLE', width=25, command=lambda: Display3.Display(url16)) 
button1.pack()
button1 = Button(root, text='KFC', width=25, command=lambda: Display3.Display(url17)) 
button1.pack()


space1=Label(root,text="\n\n\n")
space1.pack()
button = Button(root, text='PORTFOLIO', width=25, command="NONE") 
button.pack()

root.mainloop()
