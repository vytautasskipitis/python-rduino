from tkinter import *
import serial.tools.list_ports
import matplotlib.pyplot as plt

# lenteleje esancios funkcijos
def pradeda_irasyti_1():
    status["text"] = 'suzinokite savo COM numeri ir iveskite skaiciu i laukeli'
    #pradeda_irasyti()

def suzinoti():
    ports = serial.tools.list_ports.comports()
    portList = []
    for onePort in ports:
        portList.append(str(onePort))
        status["text"] = (str(onePort))

def portas():
    ivesta1_1 = laukas1_1.get()

    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()
    portList = []
    for onePort in ports:
        portList.append(str(onePort))
    val = ivesta1_1
    for x in range(0, len(portList)):
        if portList[x].startswith("COM" + str(val)):
            portVar = "COM" + str(val)
            print(portList[x])
    serialInst.baudrate = 9600
    serialInst.port = portVar
    serialInst.open()
    while True:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            with open('rduino_data.txt', 'a') as fa:
                fa.write(packet.decode('utf').rstrip('\n'))

def diagrama_1():
    with open('rduino_data.txt', 'r') as fr:
        garsas = []
        atstumas_misraine = []
        misraine = fr.readlines()
        for i in misraine:
            try:
                garsas.append(int(i))
            except:
                atstumas_misraine.append(i)

    atstumas = []
    for sakinys in atstumas_misraine:
        for simbolis in sakinys.split():
            if simbolis.isdigit():
                atstumas.append(int(simbolis))

    # grafikai
    import matplotlib.pyplot as plt

    plt.plot(atstumas)
    plt.ylabel('atstumas cm')
    plt.show()

    plt.plot(garsas)
    plt.ylabel('garso stiprumas 0-1024')
    plt.show()

def diagrama_2():
    pass

def baigia_irasyt():
    #problema ,kad tk uzluzta prasidejus irasymui
    pass

def trinti_viska():
    with open('rduino_data.txt', 'w') as fw:
        contents = fw.write('')
    status["text"] = "rduino_data.txt - duomenys istrinti"


# lenteles interface
langas = Tk()

mygtukas1_0 = Button(langas, text="pradeti irasyma", command=pradeda_irasyti_1)
mygtukas1_1 = Button(langas, text="pasirinkus COM() spausti cia", command=portas)
mygtukas1_2 = Button(langas, text="suzinoti savo COM numeri", command=suzinoti)
mygtukas1_3 = Button(langas, text="sustabdo irasinejima", command=baigia_irasyt)
mygtukas2_0 = Button(langas, text="diagrama", command=diagrama_1)
mygtukas2_1 = Button(langas, text="d2", command=diagrama_2)
mygtukas3 = Button(langas, text="isrinti visus duomenis", command=trinti_viska)
laukas1_1 = Entry(langas)

status = Label(langas, text="cia bus info", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=5, columnspan=4)

mygtukas1_0.grid(row=0, column=0, sticky=E)
mygtukas1_1.grid(row=0, column=2, sticky=E)
mygtukas1_2.grid(row=0, column=3, sticky=E)
mygtukas2_0.grid(row=1, column=0, sticky=E)
mygtukas2_1.grid(row=1, column=1, sticky=E)
mygtukas3.grid(row=4, column=0, sticky=E)
laukas1_1.grid(row=0, column=1)

langas.mainloop()







