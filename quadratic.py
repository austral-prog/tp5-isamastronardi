# Replace the "ANSWER HERE" for your answer

def roots(a, b, c): #las roots las guardas primero en una variable de resuktado y dsp que te de el resultado
    discriminante = (b**2-4*a*c)
    if discriminante>=0:
        r1 = (-b+(discriminante**(1/2)))/2*a
        r2 = (-b-(discriminante**(1/2)))/2*a
        if r1!=r2:
            return f"({r1}, {r2})"
        else:
            return f"({r1})"
    else:
        return f"( )"
resultado = roots(2, 4, 2)
#print(f"Retorna: {resultado}")

def value_y(a, b, c, x): 
    y = a*(x**2)+b*x+c
    return y
resultado_2 = value_y(1, 2, 3, 1)
#print(f"Retorna:{resultado_2}")


def to_string(a, b, c): 
    ecuacion = ""
    if a!=0:
        a_1=f"{a} * X^2 "
        ecuacion = a_1
    if b!=0:
        if ecuacion=="":
            b_1=f"{b} * X "
            ecuacion = b_1
            #ecuacion din msd
        else:
            b_1=f"+ {b} * X "
            ecuacion = ecuacion + b_1
            #con mas
    if c!=0:
        if ecuacion =="":
            ecuacion =c
        else:
            c_1=f"+ {c}"
            ecuacion = ecuacion + c_1
    return f"f(x) = {ecuacion}"
ecuacion_final = to_string(2, 4, 6)
print(f"Retorna: {ecuacion_final}")
    

def derivation(a, b, c):
    resultado_3 = ""
    a = int(a)
    b= int(b)
    if a != 0:
        resultado_3 += f"{2 * a} * X"
    if b != 0:
        if resultado_3=="":
            resultado_3 = f"{b}"
        else:
            resultado_3 +=f" + {b}"
    if resultado_3 == "":
        resultado_3 = 0
    return f"f'(x) = {resultado_3}"
ecuacion_ultima = derivation(4, 3, 2)
print(f"Retorna: {ecuacion_ultima}")


