from tkinter import *

fields = ('Storage Size(GB)', 'Class A Requests (PUT, COPY, POST, LIST)', 'Class B Requests (GET)', 'Monthly Outbound Bandwidth(GB)', 'Total in U$ Dollars')

Dollar = 3.92
StorageSTD = 0.0264
StorageCOLD = 0.0072
DataRetrievalCOLD = 0.05
OutboundBandwidth = 0.18
AsperaHighSpeed = 0.08
ClassA = 0.000005
ClassB = 0.0000004


def calculateSTD(entries):
    StorageValue = float(entries['Storage Size(GB)'].get())
    ClassAValue = float(entries['Class A Requests (PUT, COPY, POST, LIST)'].get())
    ClassBValue = float(entries['Class B Requests (GET)'].get())
    OutboundBandwidthValue = float(entries['Monthly Outbound Bandwidth(GB)'].get())

    Price = (StorageSTD * StorageValue) + (OutboundBandwidth * OutboundBandwidthValue) + (ClassA * ClassAValue) + (
                ClassB * ClassBValue)
    if (var.get()):
        Price = Price + OutboundBandwidthValue * AsperaHighSpeed
    entries['Total in U$ Dollars'].delete(0, END)
    entries['Total in U$ Dollars'].insert(0, round(Price,2))
    print("%.2f" % float(Price))
    return Price


def calculateCold(entries):
    StorageValue = float(entries['Storage Size(GB)'].get())
    ClassAValue = float(entries['Class A Requests (PUT, COPY, POST, LIST)'].get())
    ClassBValue = float(entries['Class B Requests (GET)'].get())
    OutboundBandwidthValue = float(entries['Monthly Outbound Bandwidth(GB)'].get())

    Price = (StorageCOLD * StorageValue) + ((OutboundBandwidth + DataRetrievalCOLD) * OutboundBandwidthValue) + (
                ClassA * ClassAValue) + (ClassB * ClassBValue)
    if (var.get()):
        Price = Price + OutboundBandwidthValue * AsperaHighSpeed
    entries['Total in U$ Dollars'].delete(0, END)
    entries['Total in U$ Dollars'].insert(0, round(Price,2))
    print("%.2f" % float(Price))


def makeform(main, fields):
    entries = {}
    for field in fields:
        row = Frame(main)
        lab = Label(row, width=36, text=field + ": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    main = Tk()
    main.title("ICOS Simple Calculator")
    var = IntVar()
    ents = makeform(main, fields)
    c = Checkbutton(
        main, text="Aspera High-Speed", variable=var)
    c.pack(side=LEFT)
    main.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(main, text='Calculate Standard',
                command=(lambda e=ents: calculateSTD(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(main, text='Calculate Cold Storage',
                command=(lambda e=ents: calculateCold(e)))
    b2.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(main, text='Exit', command=main.quit)
    b3.pack(side=LEFT, padx=5, pady=5)
    main.mainloop()
