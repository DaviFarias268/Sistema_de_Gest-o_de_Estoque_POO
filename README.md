# 📦 Sistema de Gestão de Estoque (POO)

Um sistema simples e eficiente de gestão de estoque desenvolvido em **Python** utilizando o paradigma de **Programação Orientada a Objetos (POO)**. O projeto permite cadastrar, listar, alterar e remover produtos do estoque através de um menu interativo no terminal.

---

## 🚀 Funcionalidades

- **📥 Cadastrar Produto:** Adiciona um novo produto ao estoque com nome, preço, quantidade e código identificador único.
- **📋 Listar Produtos:** Exibe todos os produtos cadastrados no estoque.
- **✏️ Alterar Produto:** Permite atualizar individualmente o nome, preço, quantidade ou código de um produto existente.
- **🗑️ Deletar Produto:** Remove um produto do estoque através do seu código.
- **🛡️ Tratamento de Exceções:** Validação de entradas do utilizador com blocos `try/except` para prevenir erros (como introdução de texto em campos numéricos).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Paradigma:** Programação Orientada a Objetos (POO)
- **Estruturas utilizadas:** `match/case`, `try/except`, listas, classes e métodos.

---

## 📂 Estrutura do Código

O projeto está dividido principalmente em duas classes:

1. **`Produtos`**: Modela a estrutura de cada item do estoque (atributos: `produto`, `preco`, `quantidade`, `codigo`).
2. **`Estoque`**: Responsável pelo gerenciamento do conjunto de produtos (métodos: `cadastrar`, `listar_produtos`, `alterar`, `deletar`).

---

## 🔧 Como Executar o Projeto

### Pré-requisitos
Ter o **Python 3.10** ou superior instalado na máquina.
