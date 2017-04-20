from app.maxmin import max_val, min_val

if __name__ == '__main__':

    xnum = int(input("Escriba primer numero a evaluar: "))
    ynum = int(input("Escriba un segundo numero a evaluar: "))

    print("El numero mayor es el: "+ str(max_val(xnum,ynum)) + " y el menor seria: " + str(min_val(xnum,ynum)))
