"""
Module sa pemet ou kreye objet tip fonksyon.
"""

import ast
from dataclasses import dataclass, field
import math
from tkinter import Variable
from fnmatch import fnmatch
from typing_extensions import Self
from graph_function import graph1, graph2


def find(value, pattern="*"):
    "fonksyon sa a jwenn yon objet nan yon module"
    return [x for x in dir(value) if fnmatch(x, pattern)]


@dataclass(order=True)
class Expressions:
    "Creates an expression object when calledS"
    var: Variable = None
    expr: ast.Expression = None
    pow: float = None

    @property
    def pow_var(self):
        "creates a parametric equation expression"
        globals()[self.var] = self.var
        y_exp = f"{self.var}**{self.pow}"
        return f"y = {y_exp}"

    @property
    def exp(self):
        "creates a function expression"
        for elem in self.expr:
            essai = isinstance(elem, str)
            if essai:
                self.var = elem

        expression = f"{self.expr}"
        _y = f"{expression}"
        return _y


@dataclass
class Functionmaker:
    """
    classe sa a kreye objet fonction tankou nenpot expression an,
    oubyen fonksyon ki utilise fonction ki soti nan module math yo.
    """

    name: str = None
    o_type: str = None
    formula: Expressions = None

    @property
    def type_assign(self):
        """
        fonction sa jwenn korespondans ant kek expression yon
        fonction ak fonction ki nan modulee math la
        """
        if self.name is not None:
            l_func = find(math, self.name)
            for elem in l_func:
                func = elem
        else:
            pass
        return func

    @property
    def eq_exp(self):
        "Returns the equation of a given function."
        if self.o_type is not None:
            equation = Expressions(expr=self.formula)
        return equation.exp


@dataclass(order=True, frozen=True)
class Functions:
    "creates a Function object"
    sort_index: int = field(init=False, repr=False)
    equat: str
    name: str = "function"
    power: int = 1
    type: str = None

    def __post_init__(self):
        object.__setattr__(self, "sort_index", self.power)

    def __str__(self):
        return f"""The {self.name}, is a function powered at level {self.power},"
        which has the equation: y = {self.eq_func}"""

    def __add__(self, other: Self):
        new_eq: str = self.eq_func + other.eq_func
        return Functions(new_eq)

    def eq_func(self) -> str:
        "returns the equation of the function object"
        equation = Functionmaker(o_type=self.type, formula=self.equat)
        return f"{equation.eq_exp}"

    def calcul(self, value: float) -> float:
        "calculate the image of a function for a given value"
        eq_calcul = f"{self.eq_func}".replace("(x)", str(value))
        imag = ast.literal_eval(eq_calcul)
        if imag - round(imag) == 0.0:
            imag = round(imag)
        return f"{self.eq_func} = {z},  for x = {value}"

    def calcul_for_graph(self, value: float) -> float:
        """makes the same calcul as the previous function, but for the
        next function only"""
        calcul_dimag = self.eq_func.replace("(x)", str(value))
        imag = ast.literal_eval(calcul_dimag)
        if imag - round(imag) == 0.0:
            imag = round(imag)
        return imag

    @property
    def graph(self):
        "fonction sa a graph quelque soit objet Functions* que ou genyen an"
        abscisse = graph1(100)
        ordonnee = []
        for elem in abscisse:
            imag = self.calcul_for_graph(elem)
            ordonnee.append(imag)
        courbe = graph2([abscisse, ordonnee])
        return courbe

    def integrale_trap(self, _a, _b, _n) -> float:
        """li kalkule integrale yon objet tip Functions, sou yon enterval defini ak
        methode trapeze la"""
        hauteur = (_b - _a) / _n
        moyenne = 0
        while _a < _b:
            moyenne = moyenne + hauteur * (
                (self.calcul_for_graph(_a) + self.calcul_for_graph(_a + hauteur)) / 2
            )
            _a += hauteur
        integrale = round(moyenne, 3)
        return integrale


y = Expressions(var="x", pow=2)
print(y.pow_var)

z = Expressions(expr="(x)**2 + 2")
print(z.exp)

x = Functionmaker("cos")
print(x.type_assign)

a = Functionmaker(o_type="parametric", formula="2*((x)**2)+5")
print(a.eq_exp)

b = Functions(power=2, type="parametric", equat="2*((x)**2) + 4*(x) + 1")
print(b.eq_func)
print(b.calcul(4))


c = Functions(name="logarithm function", power=1, type="other", equat="log((x))")
print(c.eq_func)
print(c.calcul(1))

d = Functions(name="exponential function", power=1, type="other", equat="sin((x))")
print(d)
print(d.eq_func)
print(d.calcul(1))
print(d.graph)


e = c + d
# pati __add__ method la pa mache nan klas mwen an
# #bug
print(e)
