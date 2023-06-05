"""
suite module integrale la
"""
# pylint: disable =missing-function-docstring, invalid-name

from f_class import functions


function = functions("Parametric function", "x", 2)


f = function.eq_func

expression = function

#methode des trapezes

def integrale_f(f):
    a: int = input()
    b: int = input()
    n: int = input()
    pas = (b-a)/n
    k = a
    Somme = []

    while k < n:
        somme = pas*((f(k)+f(k+1))/2)
        Somme.append(somme)

    integrale = sum(Somme)

    return integrale

