#frequency comparator
'''
do = 132.000
dos = 139.788
re = 148.104
res = 148.104
mi = 166.320
fa = 176.220
fas = 186.648
sol = 197.736
sols = 209.484
la = 222.024
las = 235.224
si = 249.216
sis = 264.000
'''
import pyaudio
import numpy as np
from matplotlib import pyplot as plt
import time

#No violao as notas que queremos tem as seguintes frequencias em hz
c1 = 330.1 # e
c2 = 246.2 # b
c3 = 196.0 # g
c4 = 146.8 # d
c5 = 110.0 # a
c6 = 82.4  # e

corda = 0.0

cordas = [c1,c2,c3,c4,c5,c6]

media = 0.0 

chunk = 1024       # Amostras exibidas por frame
formato = pyaudio.paFloat32
canais = 1
taxa = 2000       # Amostras de audio por segundo

onda_x = 0
onda_y = 0
espectro_x = 0
espectro_y = 0
dados = []

audio = pyaudio.PyAudio()

stream = audio.open(format=formato, channels=canais, rate=taxa,
                    input=True, output=True, frames_per_buffer=chunk)

while True:
    try:
        dados_bytes = stream.read(chunk)
        dados_int = np.fromstring(dados_bytes, np.float32)
        '''
        onda_x = range(chunk)
        onda_y = dados_int[:chunk]
        '''
        espectro_x = np.fft.fftfreq(chunk, 1.0/taxa)
        y = np.fft.fft(dados_int[:chunk])
        espectro_y = [np.sqrt(b.real**2 + b.imag**2) for b in y]
        '''
        plt.clf()
        plt.subplot(211)
        plt.plot(onda_x, onda_y)
        plt.axis([0, chunk, -0.4, 0.4])
        plt.xlabel("Tempo")
        plt.ylabel("Amplitude")
        plt.subplot(212)
        plt.plot(espectro_x, espectro_y)
        plt.axis([0, taxa/2, 0, 50])
        plt.xlabel("Frequência [Hz]")
        plt.ylabel("Espectro de amplitude")
        plt.pause(.01)
        '''
        
        index = np.argmax(espectro_y)
        frq_atual = abs(espectro_x[index])
        print frq_atual
        
        menor_index = 0       
        
        for i in cordas: #qual corda se trata
            media = abs(frq_atual - cordas)
            menor = min(media)
            menor_index = np.argmin(media)
            corda = menor_index
            print corda

        if(corda == 0): 
            corda = c1
            print "Corda Mizinha"
        if(corda == 1): 
            corda = c2
            print "Corda Si"
        if(corda == 2): 
            corda = c3
            print "Corda Sol"
        if(corda == 3): 
            corda = c4
            print "Corda Re"
        if(corda == 4): 
            corda = c5
            print "Corda La"
        if(corda == 5): 
            corda = c6
            print "Corda Mizao"
                       
        
        time.sleep(0.2)

    except KeyboardInterrupt:
        break