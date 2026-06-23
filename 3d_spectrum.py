import numpy as np
import matplotlib.pyplot as plt

# 10 DIM m(255)
# Inizializziamo un array di zeri per simulare l'orizzonte massimo
m = np.zeros(255)

# 15 LET a=COS (PI/4)
a = np.cos(np.pi / 4)

# Prepariamo la finestra per il disegno (simile allo schermo dello ZX Spectrum)
plt.figure(figsize=(8, 6))
plt.title("Grafico 3D (Conversione BASIC)")
plt.xlim(0, 255)
plt.ylim(0, 175)  # Margine verticale stimato basato sui calcoli di y1

# 20 FOR y=1 TO 141 STEP 5
for y in range(1, 142, 5):
    # 25 LET e=a*y
    e = a * y
    
    # 27 LET c=y-70 / 29 LET c=c*c
    c = (y - 70) ** 2
    
    # 30 FOR x=1 TO 141
    for x in range(1, 142):
        # 34 LET d=x-70
        d = x - 70
        
        # 40 LET z=80*EXP (-0.001*(c+d*d))
        z = 80 * np.exp(-0.001 * (c + d * d))
        
        # 50 LET x1=x+e / 60 LET y1=z+e
        # Nota: Arrotondiamo a intero per usarlo come indice dell'array e coordinata pixel
        x1 = int(round(x + e))
        y1 = z + e
        
        # 70 IF y1>=m(x1) THEN LET m(x1)=y1: PLOT x1,y1
        # Gestiamo il limite dell'indice (m ha dimensione 255)
        if 0 <= x1 < 255:
            if y1 >= m[x1]:
                m[x1] = y1
                # Disegniamo il singolo punto (pixel)
                plt.plot(x1, y1, 'k.', markersize=1)

# Mostra il risultato a schermo
plt.show()
