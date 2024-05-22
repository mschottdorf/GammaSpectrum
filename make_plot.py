import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def load_file(path):
    fr = open("counts.dat", "r")
    n = -1
    data = []
    for line in fr:
        if n == -1:
            p = line.split()
            a = float(p[1]); b = float(p[2])
        else:
            count = int(line)
            data.append([n,a+b*n,count])
        n = n + 1
    fr.close()
    return np.array(data)


data = load_file("./counts.dat")

sns.set_style("darkgrid", {"grid.color": ".6", "grid.linestyle": ":"})

plt.figure(figsize=(7,5))
plt.plot(data[:,1], data[:,2],'-',linewidth=.5)

# http://nucleardata.nuclear.lu.se/toi/nuclide.asp?iZA=830214
plt.annotate(r'$^{214}$Bi',xy=(609,2800), xytext=(609,3200),arrowprops={}, ha='center')
plt.annotate(r'$^{214}$Bi',xy=(768,400), xytext=(768,800),arrowprops={}, ha='center')
plt.annotate(r'$^{214}$Bi',xy=(934,300), xytext=(934,700),arrowprops={}, ha='center')
plt.annotate(r'$^{214}$Bi',xy=(1120,600),xytext=(1120,1000),arrowprops={}, ha='center')
plt.annotate(r'$^{214}$Bi',xy=(1238,300),xytext=(1238,700),arrowprops={}, ha='center')
plt.annotate(r'$^{214}$Bi',xy=(1377,300),xytext=(1377,700),arrowprops={}, ha='center')
plt.annotate(r'$^{214}$Bi',xy=(1764,400),xytext=(1764,800),arrowprops={}, ha='center')

# http://nucleardata.nuclear.lu.se/toi/nuclide.asp?iZA=820214
plt.annotate(r'$^{214}$Pb',xy=(242, 1400),xytext=(242, 1800),arrowprops={}, ha='right')
plt.annotate(r'$^{214}$Pb',xy=(295, 2600),xytext=(295, 3000),arrowprops={}, ha='right')
plt.annotate(r'$^{214}$Pb',xy=(352, 4000),xytext=(352, 4400),arrowprops={}, ha='center')

# http://nucleardata.nuclear.lu.se/toi/nuclide.asp?iZA=880226
plt.annotate(r'$^{226}$Rn',xy=(186, 1000),xytext=(186, 1400),arrowprops={}, ha='right')

#http://nucleardata.nuclear.lu.se/toi/nuclide.asp?iZA=190040
plt.annotate(r'$^{40}$K',xy=(1461,100),xytext=(1461,500),arrowprops={}, ha='center')


plt.xlim([0,2000])
plt.ylim([-10,4700])
plt.ylabel('Counts')
plt.xlabel('E [keV]')

plt.savefig("./plot.svg")

plt.show()
