"""
Module sa pemet ou kalkule integrale par metod simpson ak trapeze.
"""

import ast
from math import log, cos, sin, exp
from dataclasses import dataclass, field
from tkinter import Variable
from graph_function import graph1, graph2


@dataclass(order=True)
class functions:
    sort_index: int = field(init=False, repr=False)
    type: str
    a: float = 1
    b: float = None
    c: float = None
    funct: str = None
    power: int = None
    var: Variable = "x"
    globals()[var] = "x"

    def __post_init__(self):
        self.sort_index = self.power

    def __str__(self) -> str:
        return f"The {self.type} function, is a function powered at level {self.power}, which has the equation: y = {self.eq_func}"

    @property
    def eq_func(self, value: float = None) -> ast.Expression:

        if value is not None:
            self.var = value
        else:
            self.var = self.var

        if self.type == "linear":
            equation_form = self.a * self.var + self.b
        elif self.type == "parametric":
            equation_form = (
                (self.a**2) * (self.var**2)
                + 2 * (self.a * self.b * self.var)
                + (self.b**2)
            )
        elif self.type == "cubic":
            equation_form = (
                (self.a**3) * (self.var**3)
                + 3 * ((self.a**2) * self.b * (self.var**2))
                + 3 * (self.a * (self.b**2) * self.var)
                + (self.b**3)
            )
        elif self.type == "other":
            equation_form = exp_funct(self.funct, self.var)
        return equation_form

    def calcul(self, value: float):
        y = self.eq_func(value)
        return y

    def __add__(self, other):
        equation = self.eq_func + other.eq_func
        functions.eq_func = equation
        return functions.eq_func

    def graph(self):
        abscisse = graph1(100)
        ordonnee = []
        for value in abscisse:
            imag = self.calcul(value)
            ordonnee.append(imag)
        courbe = graph2([abscisse, ordonnee])
        return courbe

    def integrale_trap(self):
        a: int = input()
        b: int = input()
        n: int = input()
        pas = (b - a) / n
        k = a
        Somme = []

        while k <= n:
            somme = pas * ((self.calcul(k) + self.calcul(k + pas)) / 2)
            Somme.append(somme)
            k += pas
        integrale = sum(Somme)

        return integrale


y1 = functions(type="cubic", power=3)

print(y1)
print(y1.eq_func)
