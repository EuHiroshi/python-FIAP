# Funções open()
# open("<caminhoDoArquivo><nomeDoArquivo>", "w") => indica que voce esta abrindo um arquivo para modo de escrita(w -> write) // caderno
# open("<caminhoDoArquivo><nomeDoArquivo>", "r") => indica que voce esta abrindo um arquivo para modo de leitura(r -> read) // livro
# open("<caminhoDoArquivo><nomeDoArquivo>", "a") => indica que voce esta abrindo um arquivo para modo de leitura e escrita(a -> append) // diario
# open("<caminhoDoArquivo><nomeDoArquivo>", "x") => permite criar um novo arquivo em modo exclusivo(eXclusive)
# open("<caminhoDoArquivo><nomeDoArquivo>", "t") => o arquivo que for aberto com o parametro "t", irá retornar o seu conteudo como string(t -> text)
# voce pode combinar os modos(texto ou binário) com as açoes(w, r, a, x) usando ou nao "+", por exemplo, "w+b" ou "wb"