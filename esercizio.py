import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
class Stelle:
  def __init__(self,file_path):
   self.data = pd.read_csv(file_path)
   self.age_bins = [(0, 1), (1, 5), (5, np.inf)]  # Definire i range per i sottogruppi di età
   self.age_labels = ["< 1 Gyr", "1 - 5 Gyr", "> 5 Gyr"]
    
  def plot_color_magnitude(self):
        plt.figure(figsize=(10, 6))
        scatter = plt.scatter(
            self.data['b-y'], 
            self.data['M_ass'], 
            c=self.data['age_parent'], 
            cmap='viridis', 
            alpha=0.6
        )
        plt.colorbar(scatter, label='Età (Gyr)')
        plt.xlabel("Colore (b-y)")
        plt.ylabel("Magnitudine (M_ass)")
        plt.title("Diagramma Colore-Magnitudine delle Stelle")
        plt.show()
file_path = r"C:\Users\Sara\Desktop\pandas\Nemo_6670.dat"  # Usa il percorso corretto con stringa raw
stelle = Stelle(file_path)
stelle.plot_color_magnitude()
