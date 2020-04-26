import math, random
from matplotlib import pyplot as plt

n = 14
N = 256
p = int(N/2)
w = 1800
w_coef = []
w_coef_new = []
F = [0 for _ in range(N)]
F1 = []
F2 = []

def get_signal(w, n, xmin=0, xmax=1):
    A = [xmin + (xmax - xmin) * random.random() for _ in range(n)]
    fi = [xmin + (xmax - xmin) * random.random() for _ in range(n)]
    def f(t):
        x = 0
        for i in range(n):
            x += A[i] * math.sin(w/n*t*i + fi[i])
        return x
    return f


gen = get_signal(w, n)
S = [gen(i) for i in range(0,N)]

for i in range(p):
    w_coef.append([])
    for j in range(p):
        w_coef[i].append(math.cos((4*math.pi/N)*i*j) + math.sin((4*math.pi/N)*i*j))


for i in range(N):
    w_coef_new.append(math.cos((2*math.pi/N)*i) + math.sin((2*math.pi/N)*i))

for i in range(p):
    temp1 = 0
    temp2 = 0
    for j in range(p):
        temp1 += S[2*j+1] * w_coef[i][j]
        temp2 += S[2*j] * w_coef[i][j]
    F1.append(temp1)
    F2.append(temp2)

for i in range(N):
    if (i < p):
        F[i] += F2[i] + w_coef_new[i] * F1[i]
    else:
        F[i] += F2[i - p] - w_coef_new[i] * F1[i - p]


fig = plt.figure()
ax_1 = fig.add_subplot(211)
ax_2 = fig.add_subplot(212)

ax_1.plot(range(N), S)
ax_2.plot(range(N), F)

ax_1.set(title='S')
ax_2.set(title='F')

plt.show()