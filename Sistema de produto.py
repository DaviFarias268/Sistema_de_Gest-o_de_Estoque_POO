class Produtos:
    def __init__(self, produto, preco, quantidade, codigo):
        self.produto = produto
        self.preco = preco
        self.quantidade = quantidade
        self.codigo = codigo

    def __str__(self):
        return f"Produto: {self.produto}, Quantidade: {self.quantidade}, Preco: {self.preco}, Codigo: {self.codigo}"


class Estoque:

    def __init__(self):
        self.produtos = []  # Lista vazia de produtos

    def cadastrar(self):
        # CADASTRANDO OS PRODUTOS COM TRATAMENTO DE ERRO
        try:
            nome_prduto = str(input("Digite o nome do produto: ").strip())
            valor_produto = float(input("Digite o valor do produto: ").strip())
            quantidade_produto = int(input("Digite a quantidade do produto: ").strip())
            codigo_produto = int(input("Escreva o codigo do produto: ").strip())

            # ADICIONANDO O PRODUTO NA LISTA
            cadastro_produto = Produtos(nome_prduto, valor_produto, quantidade_produto, codigo_produto)
            self.produtos.append(cadastro_produto)
            print("Produto cadastrado com sucesso!")

        except ValueError:
            print("Erro: Digite apenas números válidos para valor, quantidade e código.")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return

        for product in self.produtos:
            print(product)

    def alterar(self):
        if not self.produtos:
            print("Nenhum produto para alterar.")
            return

        print("===========ALTERANDO O PRODUTO============")
        for product in self.produtos:
            print(product)

        print("1 - ALTERAR NOME")
        print("2 - ALTERAR VALOR")
        print("3 - ALTERAR QUANTIDADE")
        print("4 - ALTERAR CODIGO")

        try:
            opcao = int(input("Digite um valor das opções: "))

            match opcao:
                case 1:
                    codigo_produto = int(input("Digite o codigo do produto: ").strip())
                    new_nome = str(input("Digite o novo nome do produto: ").strip())
                    for product in self.produtos:
                        if product.codigo == codigo_produto:
                            product.produto = new_nome
                            print("Nome alterado com sucesso!")

                case 2:
                    codigo_produto = int(input("Digite o codigo do produto: ").strip())
                    new_preco = float(input("Digite o novo preco do produto: ").strip())
                    for product in self.produtos:
                        if product.codigo == codigo_produto:
                            product.preco = new_preco
                            print("Preço alterado com sucesso!")

                case 3:
                    codigo_produto = int(input("Digite o codigo do produto: ").strip())
                    new_quantidade = int(input("Digite a nova quantidade do produto: ").strip())
                    for product in self.produtos:
                        if product.codigo == codigo_produto:
                            product.quantidade = new_quantidade
                            print("Quantidade alterada com sucesso!")

                case 4:
                    codigo_produto = int(input("Digite o codigo do produto: ").strip())
                    new_codigo = int(input("Digite o novo codigo do produto: ").strip())
                    for product in self.produtos:
                        if product.codigo == codigo_produto:
                            product.codigo = new_codigo
                            print("Código alterado com sucesso!")

                case _:
                    print("Opção inválida.")

        except ValueError:
            print("Erro: Entrada inválida. Certifique-se de digitar um número.")

    def deletar(self):
        if not self.produtos:
            print("Nenhum produto para deletar.")
            return

        print("===========DELETANDO O PRODUTO============")
        for product in self.produtos:
            print(product)

        try:
            codigo_produto = int(input("Digite o codigo do produto: ").strip())
            for product in self.produtos:
                if product.codigo == codigo_produto:
                    self.produtos.remove(product)
                    print("Produto deletado com sucesso!")
                    break
            else:
                print("Produto com o código informado não foi encontrado.")

        except ValueError:
            print("Erro: Digite um número inteiro válido para o código.")


estoq = Estoque()

while True:
    print("\n1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Alterar produto")
    print("4 - Deletar produto")
    print("5 - Sair")

    try:
        opcao = int(input("Digite um valor das opcao: "))

        match opcao:
            case 1:
                estoq.cadastrar()
            case 2:
                estoq.listar_produtos()
            case 3:
                estoq.alterar()
            case 4:
                estoq.deletar()
            case 5:
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida.")

    except ValueError:
        print("Erro: Por favor, insira apenas números.")