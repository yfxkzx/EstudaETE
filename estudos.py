

from flask import Blueprint, render_template, request
from flask_login import login_required

estudos_bp = Blueprint('estudos_bp', __name__)

materiais_estudo = [
    {
        "materia": "Português",
        "assunto": "Interpretação de Texto",
        "video": "https://www.youtube.com/playlist?list=PL-Portugues",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-de-interpretacao-de-texto/",
            "https://exercicios.brasilescola.uol.com.br/exercicios-redacao/exercicios-sobre-interpretacao-texto.htm"
        ]
    },
    {
        "materia": "Português",
        "assunto": "Identificar ideias principais e secundáras em um texto",
        "video": "https://www.youtube.com/watch?v=-Em_S_2HPbE&list=PLnK301if6PkwjGGmXGu9p8wEZYbEzgqD9",
        "exercicios": [
            "https://www.tudosaladeaula.com/2023/08/simulado-de-portugues-d9-diferenciar-as-partes-principais-de-um-texto-8o-e-9o-ano/",
            "https://tudoportugues.com/atividade-sobre-ideia-principal-e-ideia-secundaria-8ano-9ano/"
        ]
    },
    {
        "materia": "Português",
        "assunto": "Intertextualidade",
        "video": "https://www.youtube.com/watch?v=WUHfO8zx2bI&list=PLnK301if6PkyvxsCylUHcj8yhJSMh71T-",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-sobre-intertextualidade/",
            "https://exerciciosweb.com.br/portugues/intertextualidade-exercicios-com-gabarito/"
        ]
    },
    {
        "materia": "Português",
        "assunto": "Pontuação",
        "video": "https://www.youtube.com/watch?v=BqOR1DEIuzY&list=PLnK301if6Pkx1a4t7WgXzs2zSDWl09p11",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-de-pontuacao/",
            "https://www.tudosaladeaula.com/2024/10/atividade-sobre-os-sinais-de-pontuacao-anos-finais/"
        ]
    },
    {
        "materia": "Português",
        "assunto": "Norma padrão e variedade da língua",
        "video": "https://www.youtube.com/watch?v=6fBOVygtNoU&list=PLnK301if6Pkxa-cSrGb-Es-bTiQlpST3V",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-variacoes-linguisticas/",
            "https://linhaporlinha.com.br/variacao-linguistica-exercicios/"
        ]
    },
    {
        "materia": "Português",
        "assunto": "Linguagem do texto literário",
        "video": "https://www.youtube.com/watch?v=9T7-gOm0nGk&list=PLnK301if6PkxwfDwSxNKdBxa9dBt1qVH6",
        "exercicios": [
            "https://exercicios.brasilescola.uol.com.br/exercicios-literatura/exercicios-sobre-linguagem-literaria.htm",
            "https://www.todamateria.com.br/exercicio-sobre-textos-literarios-e-nao-literarios/"
        ]
    },
    {
        "materia": "Português",
        "assunto": "Sintaxe de concordância e regência",
        "video": "https://www.youtube.com/watch?v=8eTyH-HY6p8&list=PLnK301if6PkzDPocBmpbumJ5QbXBDvX3_",
        "exercicios": [
            "https://exerciciosweb.com.br/portugues/exercicios-sobre-concordancia-e-regencia/",
            "https://www.todamateria.com.br/exercicios-de-regencia-verbal/"
        ]
    },
    {
        "materia": "Português",
        "assunto": "Coordenação e Subordinação",
        "video": "https://www.youtube.com/watch?v=QBmeh_m26eQ&list=PLnK301if6Pkwygzq3RhqS2ALgKpcFLyQU",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-de-oracoes-coordenadas/",
            "https://www.todamateria.com.br/exercicios-de-oracoes-subordinadas/"
        ]
    },
    {
        "materia": "Português",
        "assunto": "Estrutura e formação das palavras",
        "video": "https://www.youtube.com/watch?v=U_nRXQh5L40&list=PLnK301if6PkyFjgSx90R6FN4cFGGx6NCo",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-sobre-formacao-de-palavras/",
            "https://www.tudosaladeaula.com/2017/08/atividade-de-estrutura-e-formacao-de-palavras-com-gabarito/"
        ]
    },
    {
        "materia": "Português",
        "assunto": "Recursos de estilo: conotação e denotação, figuras de linguagem",
        "video": "https://www.youtube.com/watch?v=n0e75nRstcU&list=PLnK301if6Pkx6rXMXpLTQdGgJ0iZPa0GF",
        "exercicios": [
            "https://www.todamateria.com.br/denotacao-e-conotacao-exercicios/",
            "https://www.todamateria.com.br/exercicios-de-figuras-de-linguagem/"
        ]
    },

    #MATEMÁTICA -----------------------------------------------------------------------------------------------------------

    {
        "materia": "Matemática",
        "assunto": "As 4 operações",
        "video": "https://www.youtube.com/watch?v=4PqECm1OA7U&list=PLnK301if6PkxlQpg85bT5HMrFyW6MQoEE",
        "exercicios": [
            "https://www.todamateria.com.br/atividades-com-as-quatro-operacoes/",
            "https://www.tudosaladeaula.com/2022/08/problemas-envolvendo-as-quatro-operacoes-4o-e-5o-ano-com-gabarito/"
            "https://acessaber.com.br/atividades/atividade-de-matematica-problemas-as-quatro-operacoes-4o-ano/"
        ]
    },


    {
        "materia": "Matemática",
        "assunto": "Operações e problemas com frações",
        "video": "https://www.youtube.com/watch?v=ZU-DAqtVkmI&list=PLnK301if6Pkw4M5RKWdqMOEUlzgaRazZQ",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-de-fracoes/",
            "https://exercicios.brasilescola.uol.com.br/exercicios-matematica/exercicios-sobre-fracoes.htm"
        ]
    }, 
    {
        "materia": "Matemática",
        "assunto": "Operações e problemas com numeros decimais",
        "video": "https://www.youtube.com/watch?v=_Ur59IV_2Ik&list=PLnK301if6PkxSqHfFuSmdhuEEHuOEWRuY",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-sobre-operacoes-com-numeros-decimais/",
            "https://www.tudosaladeaula.com/2024/11/atividade-de-operacoes-com-numeros-reais-anos-finais/"
            "https://exercicios.mundoeducacao.uol.com.br/exercicios-matematica/exercicios-sobre-numeros-decimais.htm"
        ]
    },
    {
        "materia": "Matemática",
        "assunto": "Potenciação",
        "video": "https://www.youtube.com/watch?v=FzkAWvOAEUI&list=PLnK301if6PkzTAXsUYZ7zjWrRgSbZJzNQ",
        "exercicios": [
            " https://www.todamateria.com.br/exercicios-de-potenciacao/",
            "https://educador.com.br/exercicios-de-potenciacao/"
        ]
    },
    {
        "materia": "Matemática",
        "assunto": "Raiz quadrada",
        "video": "https://www.youtube.com/watch?v=oJx5IbJYYfQ&list=PLnK301if6PkwWfw8ZLDv79B0OUcIsQjrm",
        "exercicios": [
            " https://www.todamateria.com.br/exercicios-sobre-raiz-quadrada-para-o-7-ano/",
            "https://exercicios.mundoeducacao.uol.com.br/exercicios-matematica/exercicios-sobre-raiz-quadrada.htm"
        ]
    },
    {
        "materia": "Matemática",
        "assunto": "Expressões com números reais",
        "video": "https://www.youtube.com/watch?v=LwOvCw6dfiI&list=PLnK301if6PkwPkwwrJjEexTMziUgg-21f",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-de-expressoes-numericas/",
            "https://exercicios.brasilescola.uol.com.br/exercicios-matematica/exercicios-sobre-numeros-reais.htm"
            "https://matematicabasica.net/exercicios-sobre-numeros-reais/"
        ]
    },
    {
        "materia": "Matemática",
        "assunto": "Sistema de medidas ",
        "video": "https://www.youtube.com/watch?v=105pfqwyduw&list=PLnK301if6PkyiuSm93-_jdzEGTftEe3kl",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-sobre-unidades-de-medidas/",
            "https://gabarite.com.br/simulado-concurso/9022-exercicios-sistema-de-unidade-de-medidas-com-gabarito"
            "https://exercicios.brasilescola.uol.com.br/exercicios-quimica/exercicios-sobre-unidades-medida.htm"
        ]
    },
    {
        "materia": "Matemática",
        "assunto": "Razão e proporção",
        "video": "https://www.youtube.com/watch?v=bM9v6Bgp8qM&list=PLnK301if6PkyBh0zC92zNCQ3KPVFzQ0M0 ",
        "exercicios": [
            "https://www.todamateria.com.br/razao-e-proporcao-exercicios/",
            "https://www.todamateria.com.br/razao-e-proporcao/"
        ]
    },{
        "materia": "Matemática",
        "assunto": "Regra de 3",
        "video": " https://www.youtube.com/watch?v=mnle8NcUYkQ&list=PLnK301if6PkwwJvJ2fzlnERYRJ3IWt0UJ ",
        "exercicios": [
            "https://www.todamateria.com.br/regra-de-tres-simples-exercicios/",
            "https://www.todamateria.com.br/regra-de-tres-composta-exercicios/"
            " "
        ]
    },{
        "materia": "Matemática",
        "assunto": "Ângulos",
        "video": "https://www.youtube.com/watch?v=nAvqZSglTmA&list=PLnK301if6PkxwSxdmWRbIDxyvar5ZPE1O ",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-sobre-angulos/",
            "https://exercicios.brasilescola.uol.com.br/exercicios-matematica/exercicios-sobre-Angulos.htm"
            " "
        ]
    },
    {
        "materia": "Matemática",
        "assunto": "Polígonos",
        "video": "https://www.youtube.com/watch?v=LI8rDyEMQ74&list=PLnK301if6Pky8b5AGtJ_vEMkoLGonwTJC",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-sobre-poligonos/",
            "https://exercicios.brasilescola.uol.com.br/exercicios-matematica/exercicios-sobre-poligonos.htm"
        ]
    },
    {
        "materia": "Matemática",
        "assunto": "Cevianas",
        "video": "https://www.youtube.com/watch?v=pq1pze39p-I&list=PLnK301if6Pky5z6hjDERNUb35d7zvP5_k",
        "exercicios": [
            "https://www.exercicios-resolvidos.com/2021/03/exercicios-resolvidos-sobre-cevianas.html",
            "https://exerciciosweb.com.br/matematica/triangulos-e-pontos-notaveis-exercicios-com-gabarito/"
        ]
    },
    {
        "materia": "Matemática",
        "assunto": "Semelhaça de Triângulos",
        "video": "https://www.youtube.com/watch?v=JBP0ryUtJmg&list=PLnK301if6PkxUQZGthH3M8vnX2D_nYZBD",
        "exercicios": [
            "https://www.todamateria.com.br/semelhanca-de-triangulos-exercicios/",
            "https://exercicios.brasilescola.uol.com.br/exercicios-matematica/exercicios-sobre-semelhanca-entre-triangulos.htm"
        ]
    },
    {
        "materia": "Matemática",
        "assunto": "Triângulos",
        "video": "https://www.youtube.com/watch?v=Ka3GluTldeY&list=PLnK301if6PkxoZRDrn902pVIs9WbC62se",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-sobre-triangulos-explicados/",
            "https://www.cadernodeeducacao.com.br/2024/01/exercicios-sobre-triangulos-com-gabarito.html"
        ]
    },
    {
        "materia": "Matemática",
        "assunto": "Média, Moda e Mediana",
        "video": "https://www.youtube.com/watch?v=GIzwKJL33_g&list=PLnK301if6PkzZHqg5X4vopk3aKIRBsf6m",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-de-media-moda-e-mediana/",
            "https://www.significados.com.br/exercicios-sobre-media-moda-e-mediana-para-treinar/"
        ]
    },
    {
        "materia": "Matemática",
        "assunto": "Porcentagem",
        "video": "https://www.youtube.com/watch?v=azedx0uou64&list=PLnK301if6PkwWsmUaL-ctk_j4fppXXYZO",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-de-porcentagem/",
            "https://www.significados.com.br/exercicios-sobre-porcentagem/"
        ]
    },
    {
        "materia": "Matemática",
        "assunto": "Fatoração",
        "video": "https://www.youtube.com/watch?v=hgr3iNJdLzE&list=PLnK301if6PkwZTzbxG368SaUfI1PbhM38",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-de-fatoracao-de-polinomios/",
            "https://escolaeducacao.com.br/exercicios-de-fatoracao/"
        ]
    },
    {
        "materia": "Matemática",
        "assunto": "Sistemas lineares",
        "video": "https://www.youtube.com/watch?v=tBU853Fh4e8&list=PLnK301if6Pky6IsN7RJmI7oz1x2xPmYYi",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-de-sistemas-lineares-resolvidos/",
            "https://www.significados.com.br/exercicios-sobre-sistemas-lineares/"
        ]
    },
    {
        "materia": "Matemática",
        "assunto": "Equações do 1º grau",
        "video": "https://www.youtube.com/watch?v=Tu08PYjt-2Q&list=PLnK301if6PkxyQIYhBwF-56LikwwuhsJe",
        "exercicios": [
            "https://www.todamateria.com.br/equacao-do-1-grau-com-uma-incognita-exercicios/",
            "https://www.significados.com.br/exercicios-sobre-equacao-do-1-grau/"
        ]
    },
    {
        "materia": "Matemática",
        "assunto": "Polinômios",
        "video": "https://www.youtube.com/watch?v=UBUOTEaGH3g&list=PLnK301if6PkxFLWizJehIHrQJmZh-6nru",
        "exercicios": [
            "https://www.todamateria.com.br/exercicios-de-polinomios-adicao-e-subtracao/",
            "https://tecsaladeaula.com.br/12-exercicios-de-polinomios-para-8o-e-9o-ano-com-gabarito/"
        ]
    },
    {
        "materia": "Matemática",
        "assunto": "Produtos notáveis",
        "video": "https://www.youtube.com/watch?v=UECy1XbL6w8&list=PLnK301if6PkwCkQNqtqBmXDlmqKqvZ56h",
        "exercicios": [
            "https://www.todamateria.com.br/produtos-notaveis-exercicios/",
            "https://lereaprender.com.br/exercicios-sobre-produtos-notaveis/"
        ]
    },
    
]


@estudos_bp.route('/estudos', methods=['GET'])
@login_required
def estudos():
    materia_escolhida = request.args.get('materia')
    
    if materia_escolhida:
        filtrados = [m for m in materiais_estudo if m["materia"] == materia_escolhida]
    else:
        filtrados = materiais_estudo

    materias_disponiveis = sorted(set(m["materia"] for m in materiais_estudo))

    return render_template(
        'estudos.html',
        estudos=filtrados,
        materias=materias_disponiveis,
        materia_escolhida=materia_escolhida
    )
