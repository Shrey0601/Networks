import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

distance = []

df = pd.read_csv('datapoints.csv', header=0, names=['Distance', 'Intensity'])

val = np.array(df['Intensity'])

act_dist = np.array(df['Distance'])


for i in act_dist:
    distance.append(math.log(i, 10))

def PLE(distance, val):
    model = LinearRegression()
    model.fit(np.array(distance).reshape(-1,1), np.array(val).reshape(-1,1))
    pred = model.predict(np.array(distance).reshape(-1,1))
    plt.scatter(distance, val, color='g')
    plt.plot(distance, pred, color='k')
    plt.xlabel('Logarithmic Distance')
    plt.ylabel('RSSI')
    plt.title('Path Loss Exponent')
    plt.show()
    slope = np.polyfit(distance, val, 1)[0]
    # print(model.predict(np.array(distance).reshape(-1, 1)))
    Var = np.var(np.array(np.array(val).reshape(-1,1)-pred))
    return abs(slope/10), Var           # return the path loss exponent (PLE) in dBm/cm


Path_Loss, Var = PLE(distance, val)
print("Path Loss Exponent: " + str(Path_Loss) + " dBm/cm")
print("Variance: " + str(Var) + " dBm^2")

Pd0 = -45.5

sig = [-28, -34, -39, -45, -46]

obs_dist = [21, 42, 63, 84, 105]

def Pd(Pd0, Path_Loss, val):
    Pdd = []
    for i in range(5):
        Pdd.append(100*(10**((Pd0-sig[i])/(10*Path_Loss))))
    return Pdd

def error(distance, predictions):
    diatnces, predictions = np.array(distance), np.array(predictions)
    return np.mean(np.abs(distance - predictions))

Pdd = Pd(Pd0, Path_Loss, val)

# print(Pdd)

print("Mean Absolute Error: " + str(error(obs_dist, Pdd)) + " cm")

