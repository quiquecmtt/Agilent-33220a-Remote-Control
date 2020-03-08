import agilent33220a as agi
import numpy as np
import matplotlib.pyplot as plt
import arbitraryfunctions as af

#instrument=agi.connect_device()
#t=np.linspace(-32768,32767)
#function=np.round(t/6553.6)
function=af.jime()
plt.plot(function)
plt.show()
print(len(function))
#instrument.load_signal(function,"MATI") #Solo acepta letras, numeros y '_' el nombre de la funcion
#instrument.output_af("MATI",6,5000,99)
#instrument.output_on()
#instrument.catalog()
#instrument.af_attributes("MATI")
#instrument.erase_af("QUIQUE_FUNC")
