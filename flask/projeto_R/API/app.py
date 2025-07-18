from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Criando um banco dos desenvolvedores
desenvolvedores = [
    {
        "ID": "0",
        "Nome": "Tovany",
        "Habilidade": "Nenhuma",
    },

    {
        "ID": "1",
        "Nome": "Rafael",
        "Habilidade": ["Uber", "Casado"]
    }

]

# Ter acesso aos desenvolvedores por meio do ID deles, no caso, a posição na lista que eles estão.
## Deleta, Altera alguma coisa, do desenvolvedor
@app.route("/dev/<int:id>", methods = ["GET", "PUT", "DELETE"]) # PUT altera algo
def desenvolvedor(id):
    if request.method == "GET":
        try:
            response = desenvolvedores[id]
            
        except IndexError:
            mensagem = "Desenvolvedor não encontrado".format(id)
            response = {"status": "erro", "Mensagem": mensagem}

        return jsonify(response)
    

    # Vai servir para atualizar os recursos sem inserir nada novo, no caso no final da lista. Sò atualizar
    elif request.method == "PUT":
        dados = json.loads(request.data) # No put, ele recebe o dado, e logo se entende que ele é um dado no formato json 
        desenvolvedores[id] = dados;
        return jsonify(dados)

    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        print(desenvolvedores)
        return jsonify({"Status": "Sucesso", "Mensagem": "Registro excluido com sucesso", "N°Pessoas": len(desenvolvedores)})
    


# Esse já vai atualizar a lista inserindo algo novo
@app.route("/dev", methods = ["POST", "GET"])
def listar_desenvolvedores():

    if request.method == "POST":
        dados = json.loads(request.data);
        posicao = len(desenvolvedores);
        dados["ID"] = posicao;
        desenvolvedores.append(dados);
        return jsonify(desenvolvedores[posicao]);

if __name__ == "__main__":
    app.run(debug = True)