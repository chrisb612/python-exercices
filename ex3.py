nValues = [0, 2, 450, 42, 34]


def main():
    facture(10,12)
    
    
    
def prix_livraison(prix: float) -> float:
    fee = prix / 10.0
    if fee < 5.0:
        fee = 5.0
    elif fee > 100.0:
        fee = 100.0
    return fee
    
def facture(n: int, p: float) -> float:
    l= prix_livraison(p)
    r = reduction(n)
    print(f"Prix: {n*p}")
    print(f"Reduction: -{r}%")
    print(f"Livraison: {l}")
    print("-------")
    print(f"Prix total (dont livraison) : {(p*n + r)-(p*n+r)*r/100}")
    

def test_livraison():
    for n in nValues:
        r = prix_livraison(n)
        if r < 5 or r > 100:
            print(False)
        else:   
            print(r)


def test_reduc():
    for n in nValues:
        r = reduction(n)
        if n >= 10 and n < 50:
            print(r == 10)
        elif n >= 50:
            print(r == 20)
        else:
            print(r == 0)
    
def reduction(n: int) -> int:
    if n >= 10 and n < 50:
        return 10
    elif n >= 50:
        return 20
    else:
        return 0
    
main()