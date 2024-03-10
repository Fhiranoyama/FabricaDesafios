#1 Fat calculator

#2 Conceito do Aplicativo.
    - Esse projeto foi criado com intuito de ajudar em dietas para calcular quantidade calorica de cada alimentos para que pessoas que possuem comorbidades ou ate mesmo life-styles mais fit possam comer cientes de suas Kcal diarias, onde cada busca de realiza no banco de dados e traz alimentos e sua quantidade calorica, e fica armazenado cada pesquisa para que a pessoa possa calcular no final do dia cada alimentaçao feita.

#2 Setup do ambiente virtual

    - Inserindo ambiente virtual: python -m venv venv   
    - Ativando e ambiente virtual: .\venv\Scripts\activate
    - Instalando Django: pip install django
    - Instalando Django Rest: pip install djangorestframework
    - Instalando Requests: pip install requests

#2  Documentaçao Relevantes
    
    - https://stackabuse.com/creating-a-rest-api-in-python-with-django/
    - https://mazer.dev/pt-br/git/boas-praticas/commits-semanticos/

#2 Api

    - https://caloriasporalimentoapi.herokuapp.com/api/calorias/?descricao=Frango

#2 Testes do Insomnia

    - Testes do Get estao funcionando conforme o esperado trazendo a partir de um alimento todos alimentos mais proximos apartir da pesquisa e todas suas calorias em orden, apartir do link http://127.0.0.1:8000/nutri, e possivel em parametros colocar food_name  e o aliemnto desejado "frango", alguns alimentos dos bancos de dado podem ter 1 ou mais nomes e chance de estarem com a 1 letra maiuscula assim como "Pudim".

    - Teste do post esta funcionando pelo link http://127.0.0.1:8000/nutri/ colocando em Json e posivel salvar no banco uma lista de alimentos e suas kcal como {"descricao":"Abacate", "calorias":"49kcal", "quantidade":1}.

    - Testes no patch indicam que as atualizaçoes sao possiveis pelo link http://127.0.0.1:8000/update-item/8 e possivel atualizar os alimentos salvos.

    - Teste do delete permite usuarios usando http://127.0.0.1:8000/update-item/2 remover os itens indesejados feitos no banco de dados armazenados.

    - Teste de Post 
    
