import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Stelle:
    def __init__(self, file_path):
        # Carica il file usando il percorso fornito
        self.data = pd.read_csv(file_path, sep = " ")
        self.age_bins = [(0, 1), (1, 5), (5, np.inf)]  # Definisce i range per i sottogruppi di età
        self.age_labels = ["< 1 Gyr", "1 - 5 Gyr", "> 5 Gyr"]
        print(self.data.columns)

    def plot_color_magnitude(self):
        print(self.data.head())
        plt.figure(figsize=(10, 6))
        scatter = plt.scatter(
            self.data['b_y'],
            self.data['M_ass'],
            c=self.data['age_parent'],
            cmap='viridis',
            alpha=0.6
        )
        plt.colorbar(scatter, label='Età (Gyr)')
        plt.xlabel("Colore (b_y)")
        plt.ylabel("Magnitudine (M_ass)")
        plt.title("Diagramma Colore-Magnitudine delle Stelle")
        plt.savefig('fig88.png')

# Esempio di utilizzo
file_path = r"/mnt/c/Users/Sara/Desktop/pandas/Nemo_6670.dat"  # Usa il percorso corretto con stringa raw
stelle = Stelle(file_path)
stelle.plot_color_magnitude()
#ciaooooooo                               
