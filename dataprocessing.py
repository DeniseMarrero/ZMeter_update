import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import cm
import matplotlib.colors as cmcolors

#read each line from a file
TEER_1 = list()

plt.close('all')

filename = 'TEER results/Caco_2_t2_Channel2_TEER'

fin = open(filename, 'r', encoding='latin')

state = 0
for line in fin:
    line = line.replace('\n', '')
#    line = line.replace(',', '.')
    fields = line.split('\t')
    
    if state == 0:
        if fields[0]=='Frequencies:':
            state += 1
            Freqs = []
            for f in fields[1:]:
                if len(f)>0:
                    ff = np.float(f)
                    Freqs.append(ff)
            Freqs = np.array(Freqs)
    elif state == 1:
        if fields[0] == 'Date':
            state +=1
            Times = []
            Zmeas = np.array([])
    elif state == 2:
        Times.append(datetime.strptime(fields[0], '%d/%m/%Y %H:%M:%S'))        
        Zi = [np.float(f) for f in fields[4::4]]
        Zr = [np.float(f) for f in fields[3::4]]
        Zmea = np.vectorize(np.complex)(np.array(Zr),np.array(Zi))
        Zmeas = np.vstack((Zmeas, Zmea)) if Zmeas.size else Zmea

Times = np.array(Times)
Td = Times - Times[0]
Tsec = [d.seconds for d in Td]

Cmap = cm.ScalarMappable(norm=cmcolors.Normalize(vmin=0, vmax=Tsec[-1]),
                         cmap='jet')

fig, (axm, axp) = plt.subplots(2,1)

for t, z in zip(Tsec, Zmeas):
    axm.loglog(Freqs, np.abs(z).transpose(),
               color=Cmap.to_rgba(t))    
    axp.semilogx(Freqs, np.angle(z, deg=True).transpose(),
                 color=Cmap.to_rgba(t))

    
fig, axt = plt.subplots()
axt.plot(Tsec, np.abs(Zmeas[:, 2]))

   