class Carrinho:
    def __init__(self):
        self.produtos = list()

    def _checar_carrinho(self):
        if len(self.produtos) == 0:
            print('Adicione um item no carrinho primeiro.')
            return True

    def adicionar(self, produto):
        if type(produto.produto) == dict:
            self.produtos.append(produto.produto)

    def mostrar(self):
        if self._checar_carrinho():
            return

        print(f'\n{"="*50}\n{"Lista de compras":^50}\n{"="*50}')

        for produto in self.produtos:
            for nome, valor in produto.items():
                print('{:<40} R${:.2f}'.format(nome, valor))
        print("{}\n{:<40} R${}".format("-"*50, "Total:", self.somar()))

    def somar(self):
        if self._checar_carrinho():
            return

        valor_total = 0
        for produto in self.produtos:
            for valor in produto.values():
                valor_total += valor
        return valor_total


class Produto:
    def __init__(self, nome, preco=0.0):
        self.produto = {str(nome).capitalize(): float(preco)}


if __name__ == "__main__":
    carrinho = Carrinho()
    carrinho.mostrar()
    carrinho.adicionar(Produto('celular xiaomi redmi note8 64gb', 1299.99))
    carrinho.adicionar(Produto('teste', 420.69))
    carrinho.mostrar()
