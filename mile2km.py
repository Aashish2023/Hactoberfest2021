from tkinter import *
win = Tk()
win.minsize(300,200)
win.title("MILE TO KM CONVERTOR")
def mile2km(val):
    km = int(val)*1.6
    return round(km,2)
def click():
    ques=mile_value.get()
    ans= mile2km(ques)
    ans_km.config(text=str(ans))

########################################################
isequaltext=Label(text="is equal to")
isequaltext.grid(column=0,row=2,padx=10,pady=10)

mile_value=Entry()
mile_value.grid(column=2,row=2,padx=5,pady=5)

topic_mile=Label(text="MILE")
topic_mile.grid(column=3,row=2)

topic_km=Label(text="KM")
topic_km.grid(column=3,row=3)

ans_km=Label(text="0",font=("Arial",20,"bold"))
ans_km.grid(column=2,row=3)

button=Button(text="Calculate",font=("Arial",20,"bold"),command=click)
button.grid(column=2,row=4)







#########################################################
win.mainloop()