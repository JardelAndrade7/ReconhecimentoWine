from Wine import Wine
from NaiveBayes import NaiveBayes
from sklearn.model_selection import train_test_split

# Caminho para o arquivo CSV da base de dados Wine
caminho_arquivo = "Wine.csv"

# Importando os dados da base Wine
dadosWine = Wine(caminho_arquivo)
atributos = dadosWine.obter_dados()

# Criando os vetores de atributos e classes
instancias = list(zip(atributos['Alcohol'], atributos['Malic.acid'], atributos['Ash'], atributos['Acl'],
                     atributos['Mg'], atributos['Phenols'], atributos['Flavanoids'],
                     atributos['Nonflavanoid.phenols'], atributos['Proanth'], atributos['Color.int'],
                     atributos['Hue'], atributos['OD'], atributos['Proline']))
classes = atributos['Wine']

# Dividindo os dados em treinamento e teste (70% treinamento, 30% teste)
instanciasTreino, instanciasTeste, classesTreino, classesTeste = train_test_split(instancias, classes, test_size=0.3, random_state=42, stratify=classes)

# Organizando os dados de treino
dadosTreino = {
    'Wine': classesTreino,
    'Alcohol': [instancia[0] for instancia in instanciasTreino],
    'Malic.acid': [instancia[1] for instancia in instanciasTreino],
    'Ash': [instancia[2] for instancia in instanciasTreino],
    'Acl': [instancia[3] for instancia in instanciasTreino],
    'Mg': [instancia[4] for instancia in instanciasTreino],
    'Phenols': [instancia[5] for instancia in instanciasTreino],
    'Flavanoids': [instancia[6] for instancia in instanciasTreino],
    'Nonflavanoid.phenols': [instancia[7] for instancia in instanciasTreino],
    'Proanth': [instancia[8] for instancia in instanciasTreino],
    'Color.int': [instancia[9] for instancia in instanciasTreino],
    'Hue': [instancia[10] for instancia in instanciasTreino],
    'OD': [instancia[11] for instancia in instanciasTreino],
    'Proline': [instancia[12] for instancia in instanciasTreino],
}

# Instanciando um NaiveBayes com os dados de treino.
naive_bayes = NaiveBayes(dadosTreino)

# Treinando o modelo com os dados de treino já recebidos.
naive_bayes.treinar()

# Testando o modelo com os dados de teste
predicoes = naive_bayes.testar(instanciasTeste)

# Calculando a quantidade de erros de predições que o teste gerou em relação aos dados originais utilizados
quantidade_erros = 0
for i in range(len(predicoes)):
    if predicoes[i] != classesTeste[i]:
        quantidade_erros += 1

# Exibindo resultados
print()
print("Total: ", len(predicoes))
print("Erros: ", quantidade_erros)
print()