"""Un programa que registre el capital
"""
import os
import sqlite3
from datetime import date



fecha = date.today()
print(fecha)
with open("Movimientos"+str(fecha),"w") as guarda:
    guarda.write("FinaDEV\n")
    guarda.write("Ingresos\n")
    guarda.write("ID    Concepto    Monto   Fecha\n")
    #for a in ingresos:
        #guarda.write(str(a[0])+"    "+ str(a[1])+ "     "+ str(a[2])+"     " + str(a[3]))
        #guarda.write("\n")
