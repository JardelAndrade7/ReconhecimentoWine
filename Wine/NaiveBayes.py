import math

class NaiveBayes:
    def __init__(self, wine_data):
        self.dadosWine = wine_data
        self.sumarios = {}

    # Para cada categoria da Wine, serão calculados a média e o desvio padrão dos 13 atributos das instâncias.
    def sumarizar_por_classe(self):
        separado = self.separar_por_classe()
        sumarios = {}
        for valor_classe, instancias in separado.items():
            atributos = zip(*instancias)
            medias = [self.calcularMedia(atributo) for atributo in atributos]
            atributos = zip(*instancias)
            desvios = [self.calcularDesvio(atributo) for atributo in atributos]
            mediasDesvios = list(zip(medias, desvios))
            sumarios[valor_classe] = mediasDesvios
        self.sumarios = sumarios

    # As instâncias da Wine serão organizadas em um dicionário que conterá chaves que dizem respeito à cada categoria da Wine e associada a cada chave uma lista de instâncias que dizem respeito a ela.
    def separar_por_classe(self):
        separado = {}
        quantidadeIndices = len(self.dadosWine['Wine'])
        for i in range(quantidadeIndices):
            instancia = (
                float(self.dadosWine['Alcohol'][i]), float(self.dadosWine['Malic.acid'][i]), float(self.dadosWine['Ash'][i]),
                float(self.dadosWine['Acl'][i]), float(self.dadosWine['Mg'][i]), float(self.dadosWine['Phenols'][i]),
                float(self.dadosWine['Flavanoids'][i]), float(self.dadosWine['Nonflavanoid.phenols'][i]),
                float(self.dadosWine['Proanth'][i]), float(self.dadosWine['Color.int'][i]), float(self.dadosWine['Hue'][i]),
                float(self.dadosWine['OD'][i]), float(self.dadosWine['Proline'][i])
            )
            valorClasse = self.dadosWine['Wine'][i]
            if valorClasse not in separado:
                separado[valorClasse] = []
            separado[valorClasse].append(instancia)
        return separado

    def calcularMedia(self, valores):
        return sum(valores) / float(len(valores))

    def calcularDesvio(self, valores):
        media = self.calcularMedia(valores)
        variancia = sum([pow(x - media, 2) for x in valores]) / float(len(valores) - 1)
        return math.sqrt(variancia)

    # Calcular a probabilidade de encontrar um valor de um atributo x em uma distribuição normal (média e desvio)
    def calcularProbabilidadeValorAtributo(self, x, media, desvio):
        if desvio == 0:
            return 1 if x == media else 0
        exponent = math.exp(-((x - media) ** 2 / (2 * desvio ** 2)))
        return (1 / (math.sqrt(2 * math.pi) * desvio)) * exponent

    # Calcular a probabilidade de uma instância da Wine pertencer a cada uma das categorias.
    def calcularProbabilidadeClasse(self, vetorInstancia):
        probabilidade = {}
        for valorClasse, sumariosClasse in self.sumarios.items():
            probabilidade[valorClasse] = 1
            for i in range(len(sumariosClasse)):
                media, desvio = sumariosClasse[i]
                x = vetorInstancia[i]
                probabilidade[valorClasse] *= self.calcularProbabilidadeValorAtributo(x, media, desvio)
        return probabilidade

    # Dos três valores resultantes do método calcularProbabilidadeClasse, é identificado o maior, e a categoria que está associada a esse valor é retornada.
    def predizer(self, vetorInstancia):
        probabilidades = self.calcularProbabilidadeClasse(vetorInstancia)
        melhorRotulo, melhorProbabilidade = None, -1
        for valorClasse, probabilidade in probabilidades.items():
            if melhorRotulo is None or probabilidade > melhorProbabilidade:
                melhorProbabilidade = probabilidade
                melhorRotulo = valorClasse
        return melhorRotulo

    def treinar(self):
        self.sumarizar_por_classe()

    def testar(self, dadosTeste):
        predicoes = []
        for instancia in dadosTeste:
            resultado = self.predizer(instancia)
            predicoes.append(resultado)
        return predicoes