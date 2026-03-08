class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # El título y autor se almacenan en una tupla (inmutable)
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.info[0]}' de {self.info[1]} [Categoría: {self.categoria}, ISBN: {self.isbn}]"