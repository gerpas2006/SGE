def intdiv(a:int,b:int) -> int:
    try:
        return a // b
    except TypeError:
        print("Operador incorrecto")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    except Exception:
        print("Error")


intdiv(3,0)
intdiv(3,'0')

def intdiv3(a:int,b:int) -> int:
    try:
        return a // b
    except (TypeError,ZeroDivisionError):
        print("Comprueba el operando, hay mas errores")
    except Exception:
        print("Error")


intdiv3(7,0)

values = [4,2,7]
try:
    r = values[3]
except IndexError:
    print("Error,el indice señaldo no esta")
else:
    print(f"El número buscado es {r}")
finally:
    print("Que tengas un buen día")

def getint(numero):
    try:
        resul = int(numero)
        return resul
    except ValueError:
        print("Tienes que poner un número no una palabra")
    except Exception:
        print("Error")

getint('pedro')
