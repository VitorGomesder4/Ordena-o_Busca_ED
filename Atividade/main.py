from biblioteca_ordenar import livros, livros_ordenados_por_titulo, livros_ordenados_por_autor, livros_ordenados_por_ano, livros_ordenados_por_genero

bibli_current = livros

ocorrencia = True

while ocorrencia:
    print("Ola, digite help para ver os comandos.")
    input_cli = input("\n").strip().lower()

    match input_cli:
        case "help":
            print("\nComandos:\n")
            print("ordenar")
            print("buscar")