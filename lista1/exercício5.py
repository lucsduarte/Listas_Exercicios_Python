# Faça um Programa que converta metros para centímetros.


def conv_cm_p_metros(cm):
    m = cm / 100
    return m


cm = float(input("Quantos cm? "))
print("Essa medida em metros é {}".format(conv_cm_p_metros(cm)))
