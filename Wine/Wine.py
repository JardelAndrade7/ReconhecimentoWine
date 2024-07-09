import csv

class Wine:

    # A classe pode ser instanciada inicializando seus atributos, mas deixando-os sem valores, ou colocando valores neles, se for recebido um arquivo CSV
    def __init__(self, caminho_arquivo=None):
        self.atributos = {
            'Wine': [],
            'Alcohol': [],
            'Malic.acid': [],
            'Ash': [],
            'Acl': [],
            'Mg': [],
            'Phenols': [],
            'Flavanoids': [],
            'Nonflavanoid.phenols': [],
            'Proanth': [],
            'Color.int': [],
            'Hue': [],
            'OD': [],
            'Proline': []
        }
        if caminho_arquivo:
            self.importar(caminho_arquivo)

    # Os valores são capturados do CSV através do método importar
    def importar(self, caminho_arquivo):
        try:
            with open(caminho_arquivo, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Pular o cabeçalho
                for linha in reader:
                    self.adicionar_dados(*linha)
        except FileNotFoundError as e:
            print(f"Arquivo não encontrado: {e}")

    # Os valores são colocados nos atributos através do método adicionar_dados
    def adicionar_dados(self, wine, alcohol, malic_acid, ash, acl, mg, phenols, flavanoids,
                        nonflavanoid_phenols, proanth, color_int, hue, od, proline):
        self.atributos['Wine'].append(int(wine))
        self.atributos['Alcohol'].append(float(alcohol))
        self.atributos['Malic.acid'].append(float(malic_acid))
        self.atributos['Ash'].append(float(ash))
        self.atributos['Acl'].append(float(acl))
        self.atributos['Mg'].append(float(mg))
        self.atributos['Phenols'].append(float(phenols))
        self.atributos['Flavanoids'].append(float(flavanoids))
        self.atributos['Nonflavanoid.phenols'].append(float(nonflavanoid_phenols))
        self.atributos['Proanth'].append(float(proanth))
        self.atributos['Color.int'].append(float(color_int))
        self.atributos['Hue'].append(float(hue))
        self.atributos['OD'].append(float(od))
        self.atributos['Proline'].append(float(proline))

    def obter_dados(self):
        return self.atributos