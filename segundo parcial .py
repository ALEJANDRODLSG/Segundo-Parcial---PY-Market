import csv

class PYMarket:
    def __init__(self, filename):
        """Inicializa la clase con el nombre del archivo y una lista vacía de productos."""
        self.filename = filename
        self.productos = []

    def cargar_datos(self):
        """Carga los productos desde el archivo CSV y maneja excepciones."""
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    producto = {
                        "nombre_producto": row["nombre_producto"],
                        "precio": float(row["precio"]),
                        "porcentaje_descuento": float(row["porcentaje_descuento"])
                    }
                    self.productos.append(producto)
            print("Datos cargados exitosamente.")
        except FileNotFoundError:
            print("Error: El archivo no se encontró.")
        except ValueError:
            print("Error: El archivo contiene datos inválidos.")
        except Exception as e:
            print(f"Ocurrió un error al cargar los datos: {e}")

    def calcular_precio_promedio(self):
        """Calcula el precio promedio de los productos."""
        if not self.productos:
            print("No hay productos cargados.")
            return None
        total = sum(producto["precio"] for producto in self.productos)
        promedio = total / len(self.productos)
        return promedio

    def aplicar_descuentos(self):
        """Aplica el descuento especificado en 'porcentaje_descuento' a cada producto."""
        for producto in self.productos:
            descuento = producto["porcentaje_descuento"] / 100
            aplicar_descuento_lambda = lambda precio: precio * (1 - descuento)
            producto["precio"] = aplicar_descuento_lambda(producto["precio"])
        print("Descuentos aplicados a todos los productos según el porcentaje especificado.")


py_market = PYMarket("productos.csv")


py_market.cargar_datos()


promedio = py_market.calcular_precio_promedio()
if promedio is not None:
    print("\n" + "*" * 40)
    print(f"* Precio promedio de los productos: ${promedio:.2f} *")
    print("*" * 40 + "\n")


py_market.aplicar_descuentos()


print("Productos después de aplicar el descuento:")
print("*" * 50)
for producto in py_market.productos:
    print(f"* {producto['nombre_producto']}: ${producto['precio']:.2f}")
print("*" * 50)