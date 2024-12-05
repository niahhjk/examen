# Clase Catalogue: Maneja los libros del sistema
class Catalogue:
    def __init__(self):
        self.books = ["Libro 1", "Libro 2", "Libro 3"] 

    def get_books(self):
        return self.books

    def check_available_books(self, book_title):
        return book_title in self.books

    def update_catalogue(self, book_title):
        self.books.append(book_title)
        print(f"'{book_title}' se agregó al catálogo.")

# Clase Subject: Representa al usuario que interactúa con el sistema
class Subject:
    def __init__(self, name):
        self.name = name

    def search_author(self, author):
        print(f"{self.name} está buscando libros del autor '{author}'.")

    def print_receipt(self, book_title):
        print(f"Recibo generado: '{book_title}' ha sido procesado.")

# Clase Loan: Maneja el préstamo de libros
class Loan:
    def __init__(self, catalogue):
        self.catalogue = catalogue  # Relación con el catálogo

    def check_out(self, book_title):
        if self.catalogue.check_available_books(book_title):
            print(f"Préstamo exitoso: '{book_title}'.")
            return True
        else:
            print(f"Error: '{book_title}' no está disponible.")
            return False

# Función principal para simular el sistema
def main():
    # Crear catálogo y usuario
    catalogue = Catalogue()
    user = Subject("John")
    loan = Loan(catalogue)

    # Mostrar libros disponibles
    print("Libros disponibles en el catálogo:", catalogue.get_books())

    # Buscar un autor
    user.search_author("Autor A")

    # Intentar realizar un préstamo
    book_title = "Libro 1"
    if loan.check_out(book_title):
        user.print_receipt(book_title)

    # Agregar un nuevo libro
    catalogue.update_catalogue("Libro 4")
    print("Libros disponibles ahora:", catalogue.get_books())

# Ejecutar el programa principal
if __name__ == "__main__":
    main()

