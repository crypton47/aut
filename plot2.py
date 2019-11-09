import numpy as np
import matplotlib.pyplot as plt

#x = [1, 2, 3, 4, 5]
#y1 = [1, 1, 2, 3, 5]
#y2 = [0, 4, 2, 6, 8]
#y3 = [1, 3, 5, 7, 9]


x = [4, 16, 32, 128, 1024]

y1 = [0.00124192237854, 0.00151085853577, 0.00211906433105, 0.00492215156555,0.0415089130402] # AES

y2 = [0.00253820419312, 0.00468516349792, 0.00763010978699, 0.0237510204315, 0.184070110321] # BLowfish


y3 = [0.00467705726624, 0.0151901245117, 0.0287110805511, 0.1069419384, 0.841156959534] # 3des

y4 = [0.00115585327148, 0.00145888328552, 0.00165987014771, 0.0036940574646,0.0307610034943] # ChaCha




y = np.vstack([y1, y2, y3, y4])

labels = ["ChaCha", "AES", "Blowfish", "3DES"]

fig, ax = plt.subplots()
ax.stackplot(x, y4, y1, y2,y3, labels=labels)
ax.legend(loc='upper left')
plt.show()

fig, ax = plt.subplots()
ax.stackplot(x, y)
plt.show()
