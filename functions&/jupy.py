import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as anim

x = np.linspace(0, 4, 256)
delta_t = 0.01

figure = plt.figure("Propagation d'une onde sinusoidale")
plt.axis([0, 4, -3, 3])
plt.xlabel("(en metre)"), plt.ylabel("(en metre)")


courbe = plt.plot([], [], "g-", lw=1.5)


def onde(i):
    t = i * delta_t
    y = 2 * np.cos((2 * np.pi / 0.85) * (x - 2.3 * t))
    courbe.set_data(x, y)
    return courbe


animation = anim.FuncAnimation(
    figure, onde, frames=256, interval=delta_t * 1000, repeat=False
)
plt.show()
plt.close()