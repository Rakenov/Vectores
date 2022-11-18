class Vector:

    ## Metodos##

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def addition(self, b):
        x = self.x + b.x
        y = self.y + b.y
        z = self.z + b.z
        r = Vector(x, y, z)
        return r

    def subtraction(self, b):
        x = self.x - b.x
        y = self.y - b.y
        z = self.z - b.z
        r = Vector(x, y, z)
        return r

    def division_by_number(self, num):
        x = self.x / num
        y = self.y/num
        z = self.z/num
        r = Vector(x, y, z)
        return r

    def multiply_by_number(self, num):
        x = self.x * num
        y = self.y * num
        z = self.z * num
        r = Vector(x, y, z)
        return r

    def product_point(self, b):
        x = self.x*b.x
        y = self.y*b.y
        z = self.z*b.z
        r = Vector(x, y, z)
        return r

    def product_cross(self, b):
        x = self.y*b.z - self.z*b.y
        y = self.z*b.x - self.x*b.z
        z = self.x*b.y - self.y*b.x
        r = Vector(x, y, z)
        return r

    def show(self):
        print("(", self.x, ",", self.y, ",", self.z, ")")


Ax = int(input("Ingrese x:"))
By = int(input("Ingrese y:"))
Cz = int(input("Ingrese z:"))

Ax2 = int(input("Ingrese x2:"))
By2 = int(input("Ingrese y2:"))
Cz2 = int(input("Ingrese z2:"))

a = Vector(Ax, By, Cz)
b = Vector(Ax2, By2, Cz2)

print("Vector n°1:", a.show())
print("Vector n°2:", b.show())

print("Elija una de las siguientes opcines:")
print("1)Suma de vectores:")
print("2)Resta de vectores")
print("3)Multiplicacion vector-número")
print("4)Division vector-número")
print("5)Producto punto")
print("6)Producto cruz")
print("7)Salir")

option = int(input("Opcion: "))

if (option == 1):
    r = a.addition(b)
    r.show()
elif (option == 2):
    r = a.subtraction(b)
    r.show()
elif (option == 3):
    num = int(input("Ingrese un número:"))
    r = a.multiply_by_number(num)
    r.show()
elif (option == 4):
    num = int(input("Ingrese un número:"))
    if (num != 0):
        r = a.division_by_number(num)
        r.show()
    else:
        (print("Imposible dividir por 0."))
elif (option == 5):
    r = a.product_point(b)
    r.show()
elif (option == 6):
    r = a.product_cross(b)
    r.show()
elif (option == 7):
    print("Saliendo.")
