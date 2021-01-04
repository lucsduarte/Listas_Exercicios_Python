# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def area_q():
    l = float(input("Dê o lado do quadrado: "))
    area = l**2
    return area


def double_area(area):
    db_area = 2*area
    return print("O dobro da área é {:.3f}".format(db_area))


area = area_q()
double_area(area)



