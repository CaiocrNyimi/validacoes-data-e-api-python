from acesso_cep import BuscaEndereco

cep = "69008038"
objeto_cep = BuscaEndereco(cep)
objeto_cep.acessa_via_cep()
#api = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(api.text)

bairro, localidade, uf = objeto_cep.acessa_via_cep()
print(bairro, localidade, uf)