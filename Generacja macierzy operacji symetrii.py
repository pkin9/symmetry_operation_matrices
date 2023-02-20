# Generacja macierzy operacji symetrii dla podanej grupy punktowej (w notacji Schönflies’a)

import numpy as np
import math as m


def rotation_axis(n, axis):
    row1_1 = float(m.cos((2 * m.pi) / n))
    row1_2 = float(m.sin((2 * m.pi) / n))
    if axis == 'z':
        cn = np.matrix([[row1_1, -row1_2, 0], [row1_2, row1_1, 0], [0, 0, 1]])
        return cn
    elif axis == 'y':
        cn = np.matrix([[row1_1, 0, row1_2], [0, 1, 0], [-row1_2, 0, row1_1]])
        return cn
    elif axis == 'x':
        cn = np.matrix([[1, 0, 0], [0, row1_1, -row1_2], [0, row1_2, row1_1]])
        return cn


def reflection(axis):
    if 'xy' in axis:
        σxy = np.diag([1, 1, -1])
        return σxy
    elif 'yz' in axis:
        σyz = np.diag([-1, 1, 1])
        return σyz
    elif 'xz' in axis:
        σxz = np.diag([1, -1, 1])
        return σxz


def rotation_reflection_axis(n):
    row1_1 = float(m.cos((2 * m.pi) / n))
    row1_2 = float(m.sin((2 * m.pi) / n))
    σz = np.diag([1, 1, -1])
    cn = np.matrix([[row1_1, row1_2, 0], [-row1_2, row1_1, 0], [0, 0, 1]])
    sn = np.dot(σz, cn)
    b = n
    a = 1
    for i in range(1, n):
        if (b % 2) != 0:
            print("S", n, "^", i + 1, " = ", sn)
        elif (n % 2) == 0:
            print("C", n / 2, "^", a, " = ", sn)
            a += 1
        sn = np.dot(sn, sn)
        b -= 1


def get_n():
    while True:
        n = input("get n: ")
        if n.isnumeric() is True and n.isnumeric() > 0:
            return int(n)
        else:
            print("n must be a positive number")


def main():
    i = np.diag([-1, -1, -1])
    e = np.diag([1, 1, 1])

    while True:
        print("Options: "
              "1. C1 "
              "2. Cs "
              "3. Ci "
              "4. Cn "
              "5. Cnh "
              "6. Cnv "
              "7. Dn "
              "8. Dnh "
              "9. Dnd "
              "10. S2n "
              "11. C∞v "
              "12. D∞h "
              "13. Td "
              "14. Oh "
              "15. Ih "
              "\nTo exit type Exit")

        point_group = input("Point group: ")

        if point_group.isnumeric():
            point_group = float(point_group)

        elif point_group == "Exit":
            break

        else:
            raise ValueError("Given point group must be a number")

        if point_group in range(1, 16):
            print("E = \n", e)

            if point_group == 2:
                axis = 'yz'
                yz = reflection(axis)
                print("σh = ", yz)

            elif point_group == 3:
                print("i = \n", i)

            elif point_group == 4:
                n = get_n()
                axis = 'z'
                if n == 1:
                    print('invalid option')
                else:
                    cn = rotation_axis(n, axis)
                    print("C", n, " = ", cn)
                    for i in range(1, n - 1):
                        cn = np.dot(cn, cn)
                        print("C", n, axis, "^", i + 1, " = ", cn)

            elif point_group == 5:
                n = get_n()
                if n == 1:
                    print('invalid option')

                else:
                    axis = 'xy'
                    rot_ax = 'z'
                    cn = rotation_axis(n, rot_ax)
                    print("C", n, rot_ax, " = ", cn)
                    xy = reflection(axis)
                    print("σh = ", xy)
                    if n > 2:
                        for i in range(1, n - 1):
                            cn = np.dot(cn, cn)
                            print("C", n, rot_ax, "^", i + 1, " = ", cn)

            elif point_group == 6:
                n = get_n()
                if n == 1:
                    print('invalid option')

                else:
                    axis = 'xz'
                    rot_ax = 'z'
                    cn = rotation_axis(n, rot_ax)
                    print("C", n, rot_ax, " = ", cn)
                    xz = reflection(axis)
                    print("σv1 = ", xz)
                    if n == 2:
                        yz = reflection('yz')
                        print("σv1 = ", yz)

                    elif n > 2:
                        for i in range(1, n - 1):
                            cn = np.dot(cn, cn)
                            σ = np.dot(cn, xz)
                            print("C", n, rot_ax, "^", i + 1, " = ", cn)
                            print("σv", i + 1, " = ", σ)

            elif point_group == 7:
                n = get_n()

                if n == 1:
                    print('invalid option')

                else:
                    rot_ax = 'z'

                    if n > 2:
                        cn = rotation_axis(n, rot_ax)
                        print("C", n, rot_ax, " = ", cn)
                        rot_ax_per = 2

                        cn2 = rotation_axis(2, 'x')

                        cn_per = np.dot(cn, cn2)
                        print("C2,1 = ", cn_per)

                        for i in range(1, n - 1):
                            cn = np.dot(cn, cn)
                            cn_per_2 = cn * cn2
                            print("C", n, rot_ax, "^", i + 1, " = ", cn)
                            print("C2,", i + 1, " = ", cn_per_2)

                    elif n == 2:
                        print("C", n, "z = ", rotation_axis(2, 'z'))
                        print("C", n, "x = ", rotation_axis(2, 'x'))
                        print("C", n, "y = ", rotation_axis(2, 'y'))

            elif point_group == 8:
                n = get_n()

                if n == 1:
                    print('invalid option')

                else:
                    rot_ax = 'z'

                    if n > 2:
                        cn = rotation_axis(n, rot_ax)
                        print("C", n, rot_ax, " = ", cn)
                        rot_ax_per = 2

                        cn2 = rotation_axis(2, 'x')

                        cn_per = np.dot(cn, cn2)
                        print("C2,1 = ", cn_per)

                        for i in range(1, n - 1):
                            cn = np.dot(cn, cn)
                            cn_per_2 = cn * cn2
                            print("C", n, rot_ax, "^", i + 1, " = ", cn)
                            print("C2,", i + 1, " = ", cn_per_2)

                        if (n % 2) == 0:
                            print("i = \n", i)

                    elif n == 2:
                        print("C", n, "x = ", rotation_axis(2, 'x'))
                        print("C", n, "z = ", rotation_axis(2, 'z'))
                        print("C", n, "y = ", rotation_axis(2, 'y'))

                axis = 'xy'
                xy = reflection(axis)
                print("σh = ", xy)

            elif point_group == 9:
                n = get_n()

                if n == 1:
                    print('invalid option')

                else:
                    rot_ax = 'z'
                    axis = 'xz'
                    xz = reflection(axis)

                    if n > 2:
                        cn = rotation_axis(n, rot_ax)
                        print("C", n, rot_ax, " = ", cn)
                        print("σv1 = ", np.dot(xz, cn))
                        rot_ax_per = 2

                        cn2 = rotation_axis(2, 'x')

                        cn_per = np.dot(cn, cn2)
                        print("C2,1 = ", cn_per)

                        for i in range(1, n - 1):
                            cn = np.dot(cn, cn)
                            σ = np.dot(cn, xz)
                            cn_per_2 = cn * cn2
                            print("C", n, rot_ax, "^", i + 1, " = ", cn)
                            print("C2,", i + 1, " = ", cn_per_2)
                            print("σv", i + 1, " = ", σ)

                    elif n == 2:
                        print("C", n, "x = ", rotation_axis(2, 'x'))
                        print("C", n, "z = ", rotation_axis(2, 'z'))
                        print("C", n, "y = ", rotation_axis(2, 'y'))

            elif point_group == 10:
                n = get_n()

                if (n % 2) == 0:
                    rotation_reflection_axis(2 * n)

                else:
                    print("invalid option")

            elif point_group == 11:
                print("C∞, ∞σv")

            elif point_group == 12:
                print("C∞, ∞σv, S∞, ∞C2, i = ", i)

            elif point_group == 13:
                print("4C3, 4C3^2, 3C2, 3S4, 3S4^3, 6σd")

            elif point_group == 14:
                print("4C3, 4C3^2, 6C2, 3C4, 3C4^3, 3C2, i, 3S4, 3S4^3, 3σh, 6σd")

            elif point_group == 15:
                print("12C5, 12C5^2, 20C3, 15C2, i, 12S10, 12S10^3, 20S6, 15σ")

        else:
            print("Choice not valid")


if __name__ == "__main__":
    main()

