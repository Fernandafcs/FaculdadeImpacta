from flask import Flask, request # Importa a biblioteca

app = Flask(__name__) # Inicializa a aplicação

@app.route('/') # Nova rota
def main():
  resultado = 'Entre as notas na URL'    

  primeira = request.args.get('primeira')
  segunda = request.args.get('segunda')

  if primeira and segunda:
        
    primeira = float(primeira)
    segunda = float(segunda)

    media = (primeira + segunda) / 2
    
    resultado = (f"Primeira Nota: {primeira} <p> Segunda Nota: {segunda} <p> Media: {media}")
  return resultado

if __name__ == '__main__':
  app.run(debug=True) # Executa a aplicação





