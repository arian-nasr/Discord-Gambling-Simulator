# -*- coding: utf-8 -*-
"""Betting Strategy Simulator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-kMmSZSg4jTi8pHmKpbajvCway_thH1_
"""

import random
import matplotlib.pyplot as plt
import numpy as np

def simulate():
    balance, highlow, counter, betamount, data = 30000, ['high', 'low'], 0, 500, []
    while (balance > 0) and (counter < 2000000):
        data.append(balance)
        counter += 1
        balance = balance - betamount
        if random.choice(highlow) == 'high':
            balance, betamount = (balance + 2*betamount), 500
        else:
            if 2*betamount > balance:
                betamount = balance
            else:
                betamount = 2*betamount
    return counter

realcounter, realdata = 0, []
while realcounter < 500000:
    realcounter += 1
    realdata.append(simulate())
print(realdata)
print('mean', np.mean(realdata))
print('variance', np.var(realdata, ddof=1))
plt.plot(realdata)
plt.ylabel('iterations until crash')
plt.xlabel('iteration')
plt.show()