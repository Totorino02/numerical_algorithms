
def euler(f, t0, y0, step=0.05, nb_iter=20):
    yn = y0
    tn = t0
    for i in range(nb_iter):
        yn = yn + step * f(tn, yn)
        tn = tn + step

        print(yn, tn)


def runge_kutta_2(f, t0, y0, step=0.05, nb_iter=20):
    """method d euler modifiee"""
    yn = y0
    tn = t0
    for i in range(nb_iter):
        y = yn + step * f(tn, yn)
        yn = yn + (step / 2) * (f(tn, yn) + f(tn+step, y))
        tn = tn + step

        print(i, y, yn, tn)


def runge_kutta_4(f, t0, y0, step=0.1, nb_iter=20):
    yn = y0
    tn = t0
    for i in range(nb_iter):
        k1 = step * f(tn, yn)
        k2 = step * f(tn + step/2, yn + k1/2)
        k3 = step * f(tn + step/2, yn + k2/2)
        k4 = step * f(tn + step, yn + k3)
        yn = yn + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
        tn = tn + step

        print(i, yn)


k = lambda x, y : -y + x + 1

euler(k, 0, 1)
print("\n\n\n")
runge_kutta_2(k, 0, 1, 0.1)
print("\n\n\n")
runge_kutta_4(k, 0, 1)
