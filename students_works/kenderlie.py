def carre():
    """
    Yon fonksyon tres senmp pou kalkile kare yon nonmb, et remet ou repons lan ak yon fraz.
    """
    x = float(input("Mete nomb ou vle a la: "))
    return f"The square of {x} is : ", x**2

if __name__ == "__main__":
    carre()