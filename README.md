## 📚 Stack Implementation in Python

This project contains a basic implementation of a **Stack** (LIFO data structure) using a singly linked list in Python.

### 🧱 Structure

- `Node` class:
  - Represents each element in the stack.
  - Stores a `value` and a reference to the `next` node.

- `Stack` class:
  - Initializes with a single node.
  - Supports the following operations:
    - `push(value)`: Adds a new node to the top of the stack.
    - `pop()`: Removes and returns the top node from the stack.
    - `print_stack()`: Prints the values in the stack from top to bottom.

### 🚀 Example Usage

my_stack = Stack(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
my_stack.pop()
my_stack.print_stack()

### 📌 Output

5
4
3
2
1

## 📚 Implementação de Pilha em Python

Este projeto contém uma implementação básica de uma **Pilha** (estrutura de dados LIFO) usando lista ligada simples em Python.

### 🧱 Estrutura

- Classe `Node`:
  - Representa cada elemento da pilha.
  - Armazena um `valor` e uma referência para o próximo nó (`next`).

- Classe `Stack`:
  - Inicializa com um único nó.
  - Suporta as seguintes operações:
    - `push(valor)`: Adiciona um novo nó ao topo da pilha.
    - `pop()`: Remove e retorna o nó do topo da pilha.
    - `print_stack()`: Imprime os valores da pilha do topo até a base.

### 🚀 Exemplo de Uso

my_stack = Stack(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
my_stack.pop()
my_stack.print_stack()

### 📌 Saída

5
4
3
2
1
