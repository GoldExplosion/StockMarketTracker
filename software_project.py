from tkinter import *

import Display3
root = Tk()
root.title("STOCKZ")
heading=Label(root, 
		 text="STOCKZ\n Invest and Innovate\n",
                 font=5,
                 bg="yellow")
heading.grid(row = 0, column = 2, sticky = W, pady = 2)
space=Label(root,text="")
space.grid(row = 1, column = 0, sticky = W, pady = 2)

heading1=Label(root, 
		 text="Select the stock company: \n",
                 font=5)
heading1.grid(row = 2, column = 0, sticky = W, pady = 2)

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
button1.grid(row = 3, column = 0)
button2 = Button(root, text='AMAZON', width=25, command=lambda: Display3.Display(url2)) 
button2.grid(row = 3, column = 1)
button3 = Button(root, text='WALMART', width=25, command=lambda: Display3.Display(url3)) 
button3.grid(row = 3, column = 2)
button4 = Button(root, text='NIKE', width=25, command=lambda: Display3.Display(url4)) 
button4.grid(row = 3, column = 3)
button5 = Button(root, text='APPLE', width=25, command=lambda: Display3.Display(url5)) 
button5.grid(row = 4, column = 0)
button6 = Button(root, text='SAMSUNG', width=25, command=lambda: Display3.Display(url6)) 
button6.grid(row = 4, column = 1)
button7 = Button(root, text='ADIDAS', width=25, command=lambda: Display3.Display(url7)) 
button7.grid(row = 4, column = 2)
button8 = Button(root, text='FOSSIL', width=25, command=lambda: Display3.Display(url8)) 
button8.grid(row = 4, column = 3)
button9 = Button(root, text='CHEVROLET', width=25, command=lambda: Display3.Display(url9)) 
button9.grid(row = 5, column = 0)
button10 = Button(root, text='DELL', width=25, command=lambda: Display3.Display(url10)) 
button10.grid(row = 5, column = 1)
button11 = Button(root, text='GOLDMANN SACHS', width=25, command=lambda: Display3.Display(url11)) 
button11.grid(row = 5, column = 2)
button12 = Button(root, text='PUMA', width=25, command=lambda: Display3.Display(url12)) 
button12.grid(row = 5, column = 3)
button13 = Button(root, text='LEVIS', width=25, command=lambda: Display3.Display(url13)) 
button13.grid(row = 6, column = 0)
button14 = Button(root, text='COCACOLA', width=25, command=lambda: Display3.Display(url14)) 
button14.grid(row = 6, column = 1)
button15 = Button(root, text='HEWLETT PACKARD', width=25, command=lambda: Display3.Display(url15)) 
button15.grid(row = 6, column = 2)
button16 = Button(root, text='NESTLE', width=25, command=lambda: Display3.Display(url16)) 
button16.grid(row = 6, column = 3)
button17 = Button(root, text='KFC', width=25, command=lambda: Display3.Display(url17)) 
button17.grid(row = 7, column = 0)


space1=Label(root,text="")
space1.grid(row = 8, column = 0)
button = Button(root, text='PORTFOLIO', width=25, command="NONE") 
button.grid(row = 9, column = 0)

root.mainloop()
