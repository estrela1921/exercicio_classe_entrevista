class Entrevistado:
    def __init__(self, idade, cidade, estado, salario_atual, escolaridade):
        self.idade = idade
        self.cidade = cidade
        self.estado = estado
        self.salario_atual = salario_atual
        self.escolaridade = escolaridade

    def imprimirDados(self):
        dados = f"{self.idade},{self.cidade},{self.estado},{self.salario_atual},{self.escolaridade}"
        return dados

# Exemplo de uso da classe:
entrevistado = Entrevistado(30, "São Paulo", "SP", 5000, "Ensino Superior Completo")
dados_entrevistado = entrevistado.imprimirDados()
print(dados_entrevistado)