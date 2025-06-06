from biblioteca_ordenar import livros, livros_ordenados_por_titulo, livros_ordenados_por_autor, livros_ordenados_por_ano, livros_ordenados_por_genero

bibli_current = livros

ocorrencia = True

while ocorrencia:
    print("\nOla, digite help para ver os comandos.")
    input_cli = input("\n").strip().lower()

    match input_cli:
        case "help":
            print("\nComandos:\n")
            print("'exibir' para ver a lista")
            print("'ordenar'")
            print("'buscar'")
            print("'exit' para sair")

        case "exibir":
            for i, livro in enumerate(bibli_current):
                print(f"{i} {livro}")

        case "ordenar":
            while True:
                print("Como deseja ordenar digite o numero correspondente:\n")
                print("1.Titulo")
                print("2.Autor")
                print("3.Ano")
                print("4.Genero")
                print("5.Voltar a lista padrão")
                print("6.Cancelar")
                ordenar_metodo = input("\n").strip()

                if ordenar_metodo == "1":
                    bibli_current = livros_ordenados_por_titulo
                    print("Ordenado por 'titulo'")
                    break

                elif ordenar_metodo == "2":
                    bibli_current = livros_ordenados_por_autor
                    print("Ordenado por 'Autor'")
                    break

                elif ordenar_metodo == "3":
                    bibli_current = livros_ordenados_por_ano
                    print("Ordenado por 'Ano'")
                    break

                elif ordenar_metodo == "4":
                    bibli_current = livros_ordenados_por_genero
                    print("Ordenado por 'Genero'")
                    break

                elif ordenar_metodo == "5":
                    bibli_current = livros
                    print("Biblioteca padrão")
                    break

                elif ordenar_metodo == "6":
                    print("Voltando ao menu..")
                    break

                else:
                    print("comando invalido")
                    continue


        case "buscar":
            lista_l = []

            peso_titulo = 0
            peso_autor = 0
            peso_ano = 0
            peso_genero = 0

            busca_in = input("Digite o livro sendo o seu titulo, autor, ano, ou genero: ").strip().lower()

            for livro in bibli_current:
                if busca_in == livro["titulo"].lower():
                    lista_l.append(livro)
                    peso_titulo += 1
                
                elif busca_in == livro["autor"].lower():
                    lista_l.append(livro)
                    peso_autor += 1

                elif busca_in == livro["ano"]:
                    lista_l.append(livro)
                    peso_ano += 1

                elif busca_in == livro["genero"].lower():
                    lista_l.append(livro)
                    peso_genero += 1
                
                else:
                    continue

            if not lista_l:
                print("livro nao encontrado")

            else:
                maior_peso = max(peso_titulo, peso_autor, peso_ano, peso_genero)

                if peso_titulo == maior_peso:
                    print(f"\nLivro encontrado por titulo:")

                elif peso_autor == maior_peso:
                    print(f"\nLivros encontrados por autor:")

                elif peso_ano == maior_peso:
                    print(f"\nLivros publicados no ano:")
                            
                elif peso_genero == maior_peso:
                    print(f"\nLivros encontrados por genero:")

                for livro in lista_l:
                    print(livro)

        case "exit":
            ocorrencia = False
    
        case _:
            print("Comando invalido, tente novamente.")
            continue

print("\nPrograma terminado.\n")