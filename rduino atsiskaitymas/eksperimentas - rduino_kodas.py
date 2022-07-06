
#kolkas visas failas nenaudojamas

import serial.tools.list_ports


def pradeda_irasyti():
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()
    portList = []
    for onePort in ports:
        portList.append(str(onePort))
        print(str(onePort))
    val = input("select Port: COM")
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
            # print(packet.decode('utf').rstrip('\n'))


pradeda_irasyti()










## teisingas pavyzdys
# def pradeda_irasyti():
#     ports = serial.tools.list_ports.comports()
#     serialInst = serial.Serial()
#     portList = []
#     for onePort in ports:
#         portList.append(str(onePort))
#         print(str(onePort))
#     val = input("select Port: COM")
#     for x in range(0, len(portList)):
#         if portList[x].startswith("COM" + str(val)):
#             portVar = "COM" + str(val)
#             print(portList[x])
#     serialInst.baudrate = 9600
#     serialInst.port = portVar
#     serialInst.open()
#     while True:
#         if serialInst.in_waiting:
#             packet = serialInst.readline()
#             with open('rduino_data.txt', 'a') as fa:
#                 fa.write(packet.decode('utf').rstrip('\n'))
#             # print(packet.decode('utf').rstrip('\n'))