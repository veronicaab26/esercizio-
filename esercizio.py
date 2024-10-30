import pandas as pd 
import numpy as np 
#lettura del file dati 
df = pd.read_csv('Nemo_6670.dat', sep=' ')
#creiamo una classe 
class Stelle:
  def _init_(self, M_ass, b_y, age_parent):
    self.M_ass = M_ass
    self.b_y = b_y
    self.age_parent = age_parent 
    
