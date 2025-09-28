from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy.exc import IntegrityError
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from datetime import timedelta
from models import Usuario
from questoes_portugues import banco_questoes, questao_aleatoria
from questoes_matematica import banco_questoes_mat, questao_matematica_nao_repetida
from estudos import estudos_bp
from duvidas import duvidas_bp
from flask import flash
from db import db
import hashlib



app = Flask(__name__)
app.secret_key = 'lancode'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

def hash(txt):
    return hashlib.sha256(txt.encode('utf-8')).hexdigest()

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        
        login_error = session.pop('login_error', None)
        register_error = session.pop('register_error', None)
        return render_template('login.html', login_error=login_error, register_error=register_error)

    nome = request.form.get('nomeForm')
    senha = request.form.get('senhaForm')
    
   
    if not nome or not senha:
        session['login_error'] = 'Por favor, preencha todos os campos.'
        return redirect(url_for('login'))
    
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    user = Usuario.query.filter_by(nome=nome, senha=senha_hash).first()

    if not user:
        session['login_error'] = 'Nome de usuário ou senha incorretos.'
        return redirect(url_for('login'))

    login_user(user)
    return redirect(url_for('home'))

@app.route('/registrar', methods=['POST'])
def registrar():
    try:
        nome = request.form['nomeForm']
        senha = request.form['senhaForm']
        
     
        if not nome or not senha:
            session['register_error'] = 'Por favor, preencha todos os campos.'
            return redirect(url_for('login'))
            
        
        if len(senha) < 4:
            session['register_error'] = 'A senha deve ter pelo menos 4 caracteres.'
            return redirect(url_for('login'))
            
        novo_usuario = Usuario(nome=nome, senha=hash(senha))
        db.session.add(novo_usuario)
        db.session.commit()
        login_user(novo_usuario)
        flash('Conta criada com sucesso!', 'success')
        return redirect(url_for('home'))
    
    except IntegrityError:
        db.session.rollback()
        session['register_error'] = 'Este nome de usuário já existe. Por favor, escolha outro.'
        return redirect(url_for('login'))
    
    except Exception as e:
        db.session.rollback()
        session['register_error'] = 'Erro ao criar conta. Tente novamente.'
        return redirect(url_for('login'))

app.register_blueprint(estudos_bp)




import random
def questao_aleatoria_nao_repetida(materia='portugues'):
    if materia == 'portugues':
        banco = banco_questoes
        key = 'respondidas'
    else:
        banco = banco_questoes_mat
        key = 'respondidas_matematica'
    
    respondidas = session.get(key, [])
    
    
    if len(respondidas) > 50:  
        respondidas = respondidas[-50:]
        session[key] = respondidas
    
    restantes = [q for q in banco if q['enunciado'] not in respondidas]

    if not restantes:
        return None

    nova = random.choice(restantes)
    return nova

@app.route('/portugues', methods=['GET', 'POST'])
def portugues():
    session.permanent = True
    
    
    if 'respondidas' not in session:
        session['respondidas'] = []
    
   
    if len(session.get('respondidas', [])) > 100:
        session['respondidas'] = session['respondidas'][-50:]  
    
   
    print(f"=== PORTUGUES ===")
    print(f"Method: {request.method}")
    print(f"Tem questao_atual: {'questao_atual' in session}")
    print(f"Tem resposta: {'resposta' in session}")
    print(f"Respondidas: {len(session['respondidas'])}")
    print(f"Tamanho sessão: {len(str(session))} bytes")

   
    if request.method == 'POST':
        
        if 'resposta' in session:
            return redirect(url_for('portugues'))
            
        questao = session.get('questao_atual')
        letra_selecionada = request.form.get('alternativa')

        if questao and letra_selecionada:
            correta = questao['correta']
            resultado = 'acertou' if letra_selecionada == correta else 'errou'

            if resultado == 'acertou' and current_user.is_authenticated:
                current_user.acertos_portugues = (current_user.acertos_portugues or 0) + 1
                db.session.commit()

            
            session['resposta'] = {
                'selecionada': letra_selecionada,
                'resultado': resultado
            }
            
           
            enunciado_hash = str(hash(questao['enunciado'])) 
            if enunciado_hash not in session['respondidas']:
                session['respondidas'].append(enunciado_hash)
            
            print(f"Resposta salva: {resultado}")
        
        return redirect(url_for('portugues'))

    
    if request.args.get('f5') == '1':
        session.pop('questao_atual', None)
        session.pop('resposta', None)
        return redirect(url_for('portugues'))

   
    if 'resposta' in session and 'questao_atual' in session:
        resposta = session['resposta']
        questao = session['questao_atual']
        
        print("=== MOSTRANDO FEEDBACK ===")
        resolucao_corrigida = questao.get('resolucao', '')
        if isinstance(resolucao_corrigida, tuple):
            resolucao_corrigida = ' '.join(str(item) for item in resolucao_corrigida)
        
        return render_template(
            'portugues.html',
            enunciado=questao['enunciado'],
            enunciado2=questao.get('enunciado2', ''), 
            texto_questao=questao.get('texto', ''),
            imagem_path=questao['imagem'],
            alternativas=questao['alternativas'],
            resposta_correta=questao['correta'],
            resolucao=resolucao_corrigida,
            assunto=questao.get('assunto', ''),
            selecionada=resposta['selecionada'],
            resultado=resposta['resultado']
        )


    
    
    session.pop('resposta', None)
    
    nova_questao = questao_aleatoria_nao_repetida('portugues')

    if not nova_questao:
        
        session['respondidas'] = []
        nova_questao = questao_aleatoria_nao_repetida('portugues')
        if not nova_questao:
            return "Erro: Nenhuma questão disponível"

    session['questao_atual'] = nova_questao
    print(f"Nova questão: {nova_questao['enunciado'][:50]}...")

    resolucao_corrigida = nova_questao.get('resolucao', '')
    if isinstance(resolucao_corrigida, tuple):
        resolucao_corrigida = ' '.join(str(item) for item in resolucao_corrigida)

    return render_template(
        'portugues.html',
        enunciado=nova_questao['enunciado'],
        enunciado2=nova_questao.get('enunciado2', ''),
        texto_questao=nova_questao.get('texto', ''),
        imagem_path=nova_questao['imagem'],
        alternativas=nova_questao['alternativas'],
        resposta_correta=nova_questao['correta'],
        resolucao=resolucao_corrigida,
        assunto=nova_questao.get('assunto', ''),
        selecionada=None,
        resultado=None
    )

@app.route('/proxima_questao')
def proxima_questao():
    print("=== PRÓXIMA QUESTÃO ===")
    session.pop('questao_atual', None)
    session.pop('resposta', None)
    return redirect(url_for('portugues'))


@app.route('/matematica', methods=['GET', 'POST'])
def matematica():
    session.permanent = True
    
    if 'respondidas_matematica' not in session:
        session['respondidas_matematica'] = []
    
    
    if len(session.get('respondidas_matematica', [])) > 100:
        session['respondidas_matematica'] = session['respondidas_matematica'][-50:]
    
    print(f"=== MATEMATICA ===")
    print(f"Method: {request.method}")
    print(f"Tem questao_atual: {'questao_atual' in session}")
    print(f"Tem resposta: {'resposta' in session}")
    print(f"Respondidas: {len(session['respondidas_matematica'])}")
    print(f"Tamanho sessão: {len(str(session))} bytes")

    if request.method == 'POST':
        if 'resposta' in session:
            return redirect(url_for('matematica'))
            
        questao = session.get('questao_atual')
        letra_selecionada = request.form.get('alternativa')

        if questao and letra_selecionada:
            correta = questao['correta']
            resultado = 'acertou' if letra_selecionada == correta else 'errou'

            if resultado == 'acertou' and current_user.is_authenticated:
                current_user.acertos_matematica = (current_user.acertos_matematica or 0) + 1
                db.session.commit()

            session['resposta'] = {
                'selecionada': letra_selecionada,
                'resultado': resultado
            }
            
           
            enunciado_hash = str(hash(questao['enunciado']))
            if enunciado_hash not in session['respondidas_matematica']:
                session['respondidas_matematica'].append(enunciado_hash)
            
            print(f"Resposta MAT salva: {resultado}")
        
        return redirect(url_for('matematica'))

    if request.args.get('f5') == '1':
        session.pop('questao_atual', None)
        session.pop('resposta', None)
        return redirect(url_for('matematica'))

   
    if 'resposta' in session and 'questao_atual' in session:
        resposta = session['resposta']
        questao = session['questao_atual']
        
        print("=== MAT MOSTRANDO FEEDBACK ===")
        resolucao_corrigida = questao.get('resolucao', '')
        if isinstance(resolucao_corrigida, tuple):
            resolucao_corrigida = ' '.join(str(item) for item in resolucao_corrigida)
        
        return render_template(
            'matematica.html',
            enunciado=questao['enunciado'],
            enunciado2=questao.get('enunciado2', ''), 
            texto_questao=questao.get('texto', ''),
            imagem_path=questao['imagem'],
            alternativas=questao['alternativas'],
            resposta_correta=questao['correta'],
            resolucao=resolucao_corrigida,
            assunto=questao.get('assunto', ''),
            selecionada=resposta['selecionada'],
            resultado=resposta['resultado']
        )

    
    print("=== MAT BUSCANDO NOVA QUESTÃO ===")
    session.pop('resposta', None)
    
    nova_questao = questao_aleatoria_nao_repetida('matematica')

    if not nova_questao:
        session['respondidas_matematica'] = []
        nova_questao = questao_aleatoria_nao_repetida('matematica')

    session['questao_atual'] = nova_questao

    resolucao_corrigida = nova_questao.get('resolucao', '')
    if isinstance(resolucao_corrigida, tuple):
        resolucao_corrigida = ' '.join(str(item) for item in resolucao_corrigida)

    return render_template(
        'matematica.html',
        enunciado=nova_questao['enunciado'],
        enunciado2=nova_questao.get('enunciado2', ''),
        texto_questao=nova_questao.get('texto', ''),
        imagem_path=nova_questao['imagem'],
        alternativas=nova_questao['alternativas'],
        resposta_correta=nova_questao['correta'],
        resolucao=resolucao_corrigida,
        assunto=nova_questao.get('assunto', ''),
        selecionada=None,
        resultado=None
    )

@app.route('/proxima_questao_matematica')
def proxima_questao_matematica():
    session.pop('questao_atual', None)
    session.pop('resposta', None)
    return redirect(url_for('matematica'))


@app.route('/limpar_sessao')
def limpar_sessao():
    session.clear()
    return "Sessão limpa!"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear() 
    return redirect(url_for('home'))

@app.route('/simulado', methods=['GET', 'POST'])
def simulado():
    if request.method == 'POST':
        respostas = request.form
        questoes = session.get('questoes_simulado', [])
    
        
        respostas_fornecidas = 0
        for i in range(len(questoes)):
            if f'resposta_{i}' in respostas:
                respostas_fornecidas += 1
                
        if respostas_fornecidas < len(questoes):
            flash('Você precisa responder todas as questões antes de finalizar!', 'error')
            return redirect(url_for('simulado'))

        session['respostas_parciais'] = {k: v for k, v in respostas.items() if k.startswith('resposta_')}
        
        acertos = 0
        erros = 0
        for i, q in enumerate(questoes):
            resposta_usuario = respostas.get(f'resposta_{i}')
            q['usuario'] = resposta_usuario 

            if resposta_usuario == q['correta']:
                acertos += 1
            else:
                erros += 1

        session['resultado'] = {
            'acertos': acertos,
            'erros': erros,
            'questoes': questoes
        }

        session.pop('questoes_simulado', None)

        return redirect(url_for('home'))

    session.pop('resultado', None)
    respostas_parciais = session.get('respostas_parciais', {})

    try:
        port = random.sample(banco_questoes, 10)
        mat = random.sample(banco_questoes_mat, 10)
    except ValueError:
        flash('Erro: é necessário ter pelo menos 10 questões em cada banco.', 'error')
        return redirect(url_for('home'))

    todas = port + mat
    session['questoes_simulado'] = todas

    return render_template(
        'simulado.html',
        questoes=todas,
        respostas_usuario=respostas_parciais
    )

@app.route('/finalizar_simulado')
def finalizar_simulado():
    session.clear()
    return redirect(url_for('home'))
@app.route('/duvida')
def duvida():
    return render_template('duvida.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/conteudos')
def conteudos():
    return render_template('conteudos.html', conteudos=conteudos)

@app.route('/duvida')
def quiz():
    return render_template('duvida.html')

import os

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

