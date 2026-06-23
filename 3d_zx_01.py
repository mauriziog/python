import numpy as np

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Errore: il pacchetto matplotlib non è installato. "
        "Installa con: python -m pip install matplotlib"
    ) from exc

m = np.zeros(256)
a = np.cos(np.pi / 4)

plt.figure(figsize=(8, 6))
plt.title("Grafico 3D (Conversione BASIC)")
plt.xlim(0, 255)
plt.ylim(0, 175)

# Liste per accumulare i punti e disegnare tutto insieme (molto più veloce)
px = []
py = []

for y in range(1, 142, 5):
    e = a * y
    c = (y - 70) ** 2
    for x in range(1, 142):
        d = x - 70
        z = 80 * np.exp(-0.001 * (c + d * d))
        x1 = int(round(x + e))
        y1 = z + e
        
        # Tutto questo blocco deve essere indentato dentro il ciclo 'for x'
        if 0 <= x1 < 255:
            if y1 >= m[x1]:
                m[x1] = y1
                px.append(x1)
                py.append(y1)

# Disegna tutti i punti accumulati in un colpo solo
plt.plot(px, py, 'k.', markersize=1)
plt.show()