livros = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "genero": "Romance"},
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "genero": "Distopia"},
    {"titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien", "ano": 1954, "genero": "Fantasia"},
    {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "ano": 1943, "genero": "Fábula"},
    {"titulo": "Capitães da Areia", "autor": "Jorge Amado", "ano": 1937, "genero": "Drama"},
    {"titulo": "Orgulho e Preconceito", "autor": "Jane Austen", "ano": 1813, "genero": "Romance"},
    {"titulo": "A Revolução dos Bichos", "autor": "George Orwell", "ano": 1945, "genero": "Satírico"},
    {"titulo": "Cem Anos de Solidão", "autor": "Gabriel García Márquez", "ano": 1967, "genero": "Realismo Mágico"},
    {"titulo": "Harry Potter e a Pedra Filosofal", "autor": "J.K. Rowling", "ano": 1997, "genero": "Fantasia"},
    {"titulo": "A Metamorfose", "autor": "Franz Kafka", "ano": 1915, "genero": "Ficção Existencialista"},
] #Criando a nossa biblioteca de livros


#Criando uma lista ordenada de livros por titulo
livros_ordenados_por_titulo = sorted(livros, key=lambda livro: livro["titulo"]) #Nova lista ordenada com uma função sem nome que retorna o valor do dicionario "titulo"

#Criando uma lista ordenada de livros por autor
livros_ordenados_por_autor = sorted(livros, key=lambda livro: livro["autor"]) #Nova lista ordenada com uma função sem nome que retorna o valor do dicionario "autor"

#Criando uma lista ordenada de livros por ano de lançamento
livros_ordenados_por_ano = sorted(livros, key=lambda livro: livro["ano"]) #Nova lista ordenada com uma função sem nome que retorna o valor do dicionario "ano"

#Criando uma lista ordenada de livros por genero
livros_ordenados_por_genero = sorted(livros, key=lambda livro: livro["genero"]) #Nova lista ordenada com uma função sem nome que retorna o valor do dicionario "genero"