def Christie ():
    nom = str(input("mete nomw la:"))
    prenom = str(input("met prenomw la:"))
    sex = str(input ("ki sexe ou:"))
    dat_ou_fet_la = int(input ("mete ane ou fet:"))
    #laj = int(input ("mete laj ou la:"))
    peyi = str(input ("mete peyi ou fet lan:"))
    manmanw = str(input ("mete nom manmanw la:"))
    papaw = str(input ("mete nom papaw la:"))
    numero = int(input ("mete numero telefon ou la:"))
    adres = str(input ("ki kote ou rete:"))
    
    laj = 2023 - dat_ou_fet_la
    
    print(nom,prenom,sex,dat_ou_fet_la,laj,peyi,manmanw,papaw,numero,adres)
    
if __name__ == "__main__":
    Christie()
    