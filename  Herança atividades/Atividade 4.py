class ItemBiblioteca:
    def __init__(self, titulo: str, codigo: int):
        self.titulo = titulo
        self.codigo = codigo
        self.disponivel = True

    def emprestar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True

class Livro(ItemBiblioteca):
    def __init__(self, titulo: str, codigo: int, autor: str, num_paginas: int):
        super().__init__(titulo, codigo)
        self.autor = autor
        self.num_paginas = num_paginas

class Usuario:
    def __init__(self, nome: str):
        self.nome = nome
        self.itens_emprestados = []

    def pegar_item(self, item: ItemBiblioteca):
        if item.disponivel:
            item.emprestar()
            self.itens_emprestados.append(item)
            print(f"Sucesso: '{item.titulo}' foi emprestado para {self.nome}.")
        else:
            print(f"Erro: O item '{item.titulo}' não está disponível no momento.")

    def devolver_item(self, item: ItemBiblioteca):
        if item in self.itens_emprestados:
            item.devolver()
            self.itens_emprestados.remove(item)
            print(f"Sucesso: '{item.titulo}' foi devolvido por {self.nome}.")
        else:
            print(f"Erro: {self.nome} não possui o item '{item.titulo}' para devolver.")

    def ver_historico(self):
        print(f"\nItens atualmente com {self.nome}:")
        if not self.itens_emprestados:
            print("- Nenhum item emprestado.")
        else:
            for item in self.itens_emprestados:
                print(f"- {item.titulo} (Código: {item.codigo})")
        print()

livro1 = Livro("O Senhor dos Anéis", 101, "J.R.R. Tolkien", 1200)
livro2 = Livro("Dom Casmurro", 102, "Machado de Assis", 256)

usuario1 = Usuario("Lucas")
usuario2 = Usuario("Mariana")

usuario1.pegar_item(livro1)
usuario2.pegar_item(livro1)
usuario1.pegar_item(livro2)
usuario1.ver_historico()
usuario1.devolver_item(livro1)
usuario2.pegar_item(livro1)
usuario2.ver_historico()
