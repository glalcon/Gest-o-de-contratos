from flask import Flask, render_template

app = Flask (__name__)

@app.route ('/')
def ola_mundo():
    titulo = "Gestão de Contratos"
    usuario =(
        {"nome":"glalcon","membro_ativo": True},
        {"nome":"maria","membro_ativo": False},
        {"nome":"samantha","membro_ativo": False}
    )
    return render_template('index.html', titulo=titulo, usuarios=usuario)

@app.route ('/sobre')
def pagina_sobre():
    return """
    <b>Maneiro</b>:Curta essa musica
    <a href="https://www.youtube.com/watch?v=TvX29A17-Kk&list=RDMMTvX29A17-Kk&start_radio=1">maneira</a>    
    """


app.run(debug=True)
