class livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"titulo: {self.titulo}, autor: {self.autor}, paginas {self.paginas}"
    
    def comparar_tamanho(self, outro_livro):
        if self.paginas > outro_livro.paginas:
            print(f"O livro '{self.titulo}' é maior ({self.paginas} páginas) que '{outro_livro.titulo}' ({outro_livro.paginas} páginas)")

        elif self.paginas < outro_livro.paginas:
            print(f"O livro '{outro_livro.titulo}' é maior ({outro_livro.paginas} páginas) que '{self.titulo}' ({self.paginas} páginas)")

        else:
            print(f"Ambos os livros têm o mesmo número de páginas ({self.paginas} páginas).")

livro1 = livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1200)
livro2 = livro("O Hobbit", "J.R.R. Tolkien", 310)

print(livro1)
print(livro2)

print("        ")

livro1.comparar_tamanho(livro2)