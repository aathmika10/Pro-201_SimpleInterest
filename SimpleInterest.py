from tkinter import *

window=Tk()
window.title("SIMPLE INTEREST")
window.geometry("650x600")
window.configure(bg="#d2a5ff")

headingLabel=Label(window,text="SIMPLE INTEREST",fg="black",bg="#d2a5ff",font=("Times new roman",15),bd=3)
headingLabel.place(x=260,y=20)

principleLabel=Label(window,text="Enter the principle amount: ", fg="black", bg="#d2a5ff",font=("Cambria",13),bd=2)
principleLabel.place(x=50,y=70)

principleInput=Entry(window,text="",bd=2,width=20)
principleInput.place(x=275,y=70)

rateOfInterestLabel=Label(window,text="Enter the rate of interest: ",fg="black",bg="#d2a5ff",font=("Cambria",13),bd=2)
rateOfInterestLabel.place(x=50,y=110)

rateOfInterestInput=Entry(window,text="",bd=2,width=20)
rateOfInterestInput.place(x=275,y=110)

timeLabel=Label(window,text="Enter the time: ",fg="black", bg="#d2a5ff",font=("Cambria",13),bd="2")
timeLabel.place(x=50,y=150)

timeInput=Entry(window,text="",bd=2,width=20)
timeInput.place(x=275,y=150)
                
def calculateSI():
    p=float(principleInput.get())
    r=float(rateOfInterestInput.get())
    t=float(timeInput.get())
    i=(p*r*t)/100
    interest=round(i,2)
    resultLabel.destroy()
    msg=Label(resultBox,text="Interest on Rs."+str(p)+" at the rate of interest "+ str(r)+ "\n for "+str(t)+ " years is Rs."+ str(interest),bg="white",font=("Cambria",13),width=50)
    msg.place(x=50,y=405)
    msg.pack()

button=Button(window,text="Calculate",bd=3,bg="white",fg="black",font=("Cambria",13),command=calculateSI)
button.place(x=250,y=280)

resultBox=LabelFrame(window,text="Result",bd=1,fg="black",font=("Cambria",13))
resultBox.pack(padx=25,pady=25)
resultBox.place(x=50,y=400)

resultLabel=Label(resultBox,text="The simple interest will be displayed here.",bd=2,fg="black",font=("cambria",13))
resultLabel.place(x=50,y=20)
resultLabel.pack()

window.mainloop()