# animal = [é gordinho?, tem perna curta?, faz *auau*?]
# Sim = 1
# Não = 0

porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro4 = [1, 1, 1]
cachorro5 = [0, 1, 1]
cachorro6 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro4, cachorro5, cachorro6]

# 1 = Porco
# -1 = Cachorro
marcacoes = [1, 1, 1, -1, -1, -1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

animal_misterioso1 = [1, 1, 1]
animal_misterioso2 = [1, 0, 0]
animal_misterioso3 = [0, 0, 1]

teste = [animal_misterioso1, animal_misterioso2, animal_misterioso3]

marcacoes_teste = [-1, 1, -1]

resultado = modelo.predict(teste)

diferencas = resultado - marcacoes_teste

acertos = [acerto for acerto in diferencas if acerto == 0]

total_de_acertos = len(acertos)
total_de_elemetos = len(teste)

taxa_de_acerto = (total_de_acertos  / total_de_elemetos) * 100

print(resultado)
print(diferencas)
print(taxa_de_acerto)