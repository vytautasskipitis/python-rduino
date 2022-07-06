
# #rdata be tarpu liste
# with open('rduino_data.txt', 'r') as fr:
#     text_columns = fr.readlines()
#     data_be_tarpu = list(filter(lambda x: x != '\n', text_columns))
#
# #rdata be \n
# with open('rduino_data.txt', 'r') as fr:
#     rdata_eilute = [int(i.split(',')[-1]) for i in data_be_tarpu]
#
# print(rdata_eilute)





with open('rduino_data.txt', 'r') as fr:
    garsas = []
    atstumas_misraine = []
    misraine = fr.readlines()
    for i in misraine:
        try:
            garsas.append(int(i))
        except:
            atstumas_misraine.append(i)

print(garsas)
print(atstumas_misraine)


atstumas = []
for sakinys in atstumas_misraine:
    for simbolis in sakinys.split():
        if simbolis.isdigit():
            atstumas.append(int(simbolis))

print(atstumas)




#grafikai
import matplotlib.pyplot as plt

plt.plot(atstumas)
plt.ylabel('atstumas cm')
plt.show()


plt.plot(garsas)
plt.ylabel('garso stiprumas 0-1024')
plt.show()

#
#
# #garso suoliai
# pakilimas = []
# #kokiam periode skaiciuot suoli
# count = 1
#
# for i in rdata_eilute:
#     #snypstimas sulyginamas iki 0
#     if i < 100:
#         i = 0
#
#     pakilimas.append(i)
#     count -= 1
#
#     #pakilimu paieska
#     if sum(pakilimas) > 200:
#         print("sum > 200")
#     if count <= 0:
#         del pakilimas[0]
