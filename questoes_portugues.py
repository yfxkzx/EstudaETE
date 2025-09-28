import random
banco_questoes = [
    {
        "enunciado": "A palavra 'comodidade' apresentada no texto abaixo, é formada pelo processo de sufixação, assim como o grupo de palavras:",
        "imagem": "static/imagens/bradesco.jpg",
        "alternativas": {
            "A": "paz, ciência",
            "B": "comumente, baronesa",
            "C": "infeliz, casa",
            "D": "encanto, ideia",
            "E": "água, boiada"
        },
        "correta": "B",
        "resolucao": "A palavra 'comodidade' é formada por sufixação. 'Comumente' (comum + mente) e 'baronesa' (barão + esa) também são formadas por sufixação. Logo, a alternativa correta é a letra B.",
        "assunto": "Formação de palavras – sufixação"
    },
    {
  "enunciado": "No trecho: \"Embora fizesse frio, não levei agasalhos\", o conectivo \"embora\" exprime ideia de:",
  "texto": None,
  "imagem": None,
  "enunciado2": None,
  "alternativas": {
    "a": "concessão",
    "b": "causa",
    "c": "finalidade",
    "d": "tempo",
    "e": "comparação"
  },
  "correta": "a",
  "resolucao": "O conectivo \"embora\" introduz uma oração subordinada concessiva, indicando uma circunstância contrária à expectativa expressa na oração principal, ou seja, expressa ideia de concessão.",
  "assunto": "Coordenação e subordinação"
},
    {
        "enunciado": "No exemplo: 'conseguimos trazer todos os animais: os cachorros, gatos e os papagaios' a palavra 'animais' assume a função semântica de:",
        "imagem": "",
        "alternativas": {
            "A": "heterônimio em relação às palavras: cachorros, gatos, papagaios.",
            "B": "antônimo do verbo 'conseguir'.",
            "C": "hipônimo em relação às palavras: cachorros, gatos papagaios.",
            "D": "sinõnimo do verbo 'trazer'.",
            "E": "hipônimo da palavra 'gatos'."
        },
        "correta": "C",
        "resolucao": "'Animais' é o hiperônimo (categoria maior) que inclui os hipônimos 'cachorros', 'gatos' e 'papagaios'. Portanto, eles são exemplos de animais. A chave correta é C.",
        "assunto": "Relações semânticas – hiperônimo e hipônimo"
    },
    {
        "enunciado": "O artigo 'o', no texto abaixo, possui função de:",
        "imagem": "static/imagens/cocacola.jpeg",
        "alternativas": {
            "A": "adjetivo.",
            "B": "pronome indefinido.",
            "C": "preposição.",
            "D": "conjunção.",
            "E": "pronome demostrativo."
        },
        "correta": "E",
        "resolucao": "No uso apresentado, o artigo 'o' funciona como um pronome demonstrativo, indicando algo já mencionado ou conhecido no contexto. É um uso comum em publicidade ou linguagem informal.",
        "assunto": "Classes gramaticais – pronomes demonstrativos"
    },
    {
        "enunciado": "Assinale a alternativa adequada, em relação à tira abaixo, da personagem argentina Mafalda e seu amigo Manolito (descendente de portugueses).",
        "imagem": "static/imagens/mafalda1.jpeg",
        "alternativas": {
            "A": "Na fala de Mafalda, o pronome 'este' refere-se a qualquer país estrangeiro.",
            "B": "Na fala de Mafalda, o pronome 'este' refere-se ao país Argentina.",
            "C": "Na fala de Mafalda, o pronome 'este' refere-se ao país de origem de Manolito, Portugal.",
            "D": "Na fala de Mafalda, o pronome 'este' refere-se a um país que está grafado em um dos balões da tirinha.",
            "E": "Na fala de Mafalda, o pronome 'este' se refere-se à nação portuguesa."
        },
        "correta": "B",
        "resolucao": "A tira sugere um comentário irônico da Mafalda sobre o próprio país, a Argentina. O pronome 'este' refere-se ao país onde ela vive, destacando sua insatisfação. Por isso, a correta é B.",
        "assunto": "Pronomes demonstrativos e interpretação textual"
    },
    {
        "enunciado": "No texto publicitário do desodorante Rexona, o pronome 'te' possui como referente:",
        "imagem": "static/imagens/rexona.jpeg",
        "alternativas": {
            "A": "o abandono à marca Rexona.",
            "B": "um elemento extratextual: o leitor/consumidor do desodorante Rexona.",
            "C": "o ícone usado para representar a marca Rexona, no texto publicitário.",
            "D": "exclusivamente o autor da publicidade do desodorante Rexona.",
            "E": "o desodorante Rexona."
        },
        "correta": "B",
        "resolucao": "A alternativa correta é B, pois o artigo 'o' faz referência ao consumidor do desodorante Rexona, funcionando como elemento extratextual no texto publicitário.",
        "assunto": "Referência pronominal e texto publicitário"
    },
    {
        "enunciado": "Assinale a alternativa em que a concordância nominal está incorreta.",
        "imagem": "",
        "alternativas": {
            "A": "Os governos inglês e francês não assinou o acordo de paz.",
            "B": "Tinha extraordinária força e coragem.",
            "C": "Tinha força e coragem extraordinárias.",
            "D": "Muito obrigadas disseram elas.",
            "E": "Há menos pessoas no recinto."
        },
        "correta": "A",
        "resolucao": "A alternativa A está incorreta. O sujeito composto 'os governos inglês e francês' exige o verbo no plural: 'não assinaram'. As demais alternativas estão com a concordância nominal correta.",
        "assunto": "Concordância nominal e verbal"
    },
    {
        "enunciado": "As palavras 'BUM' e 'BUÁÁÁ' que aparecem, respectivamente, no primeiro quadrinho e no terceiro quadrinho da tirinha acima, constituem-se em um processo de formação de palavras chamado de:",
        "imagem": "static/imagens/tirinha1.jpeg",
        "alternativas": {
            "A": "onomatopeia",
            "B": "sigla",
            "C": "abreviação vocabular",
            "D": "hibridismo",
            "E": "derivação parassintética"
        },
        "correta": "A",
        "resolucao": "Essas palavras imitam sons e são exemplos clássicos de onomatopeia.",
        "assunto": "Figuras de linguagem – onomatopeia"
    },
    {
        "enunciado": "Marque a alternativa em que existe a ideia de comparação:",
        "imagem": "",
        "alternativas": {
            "A": "O mingau virou água.",
            "B": "Prestamos-lhes nossos sinceros pêsames.",
            "C": "Teus olhos são luzes brilhantes.",
            "D": "Teus cabelos são como a luz do dia.",
            "E": "Como chegou atrasado não poderá realizar a prova."
        },
        "correta": "D",
        "resolucao": "A alternativa D apresenta claramente uma comparação: 'Teus cabelos são como a luz do dia'. O uso de 'como' indica essa relação comparativa. As demais frases expressam outras ideias, como metáfora, causa ou constatação.",
        "assunto": "Figuras de linguagem – comparação"
    },
    {
        "enunciado": "Quanto às funções da linguagem, é correto afirmar que a imagem é predominantemente:",
        "imagem": "static/imagens/cartaz.jpeg", 
        "alternativas": {
            "A": "Jornalístico",
            "B": "Referencial",
            "C": "Apelativo ou conativo",
            "D": "Poético",
            "E": "Fático"
        },
        "correta": "C",
        "resolucao": "A função apelativa (ou conativa) tem como objetivo influenciar o comportamento do receptor, sendo comum em propagandas e mensagens publicitárias. Como se trata de uma imagem com essa finalidade, a alternativa correta é a letra C.",
        "assunto": "Funções da linguagem"
    },

    {
    "enunciado": "Do ponto de vista da constituição do gênero textual, observam-se, no texto abaixo, características de um (a):",
    "imagem": "static/imagens/noticia1.png", 
    "alternativas": {
        "A": "Conto",
        "B": "Artigo de opinião",
        "C": "Notícia",
        "D": "Artigo científico",
        "E": "Fábula"
    },
    "correta": "C",
    "resolucao": "O texto apresenta informações objetivas, linguagem impessoal e fatos recentes, características típicas do gênero notícia.",
    "assunto": "Gêneros textuais"
},
{
    "enunciado": "Marque a alternativa cujo termo destacado na frase está incorretamente classificado.",
    "imagem": "", 
    "alternativas": {
        "A": "As imobiliárias intensificam a venda de apartamentos novos. (complemento nominal)",
        "B": "As histórias infantis foram contadas por Andréa. (objeto idireto)",
        "C": "O juiz analisou o processo.(objeto direto)",
        "D": "A coleção de livros é composta de 10 volumes. (agente da passiva)",
        "E": "A obra foi paralisada pelos três fiscais (agente da passiva)"
    },
    "correta": "B",
    "resolucao": "O agente da passiva é o termo que executa a ação no caso de uma voz passiva. A ação de contar as histórias foi realizada por Andréa, portanto, ela é o agente da passiva. O objeto indireto é aquele que se liga ao verbo por meio de uma preposição, o que não ocorre aqui. Portanto, letra b",
    "assunto": "Funções sintáticas – agente da passiva, objeto direto/indireto, complemento nominal"
},  
    {
  
    "enunciado": "Na tirinha, o artigo 'os' no último balão, assume função de:",
    "imagem": "static/imagens/mafalda2.jpg",
    "alternativas": {
        "A": "Pronome interrogativo",
        "B": "Conjunção",
        "C": "Pronome indefinido",
        "D": "Pronome de tratamento",
        "E": "Pronome demonstrativo"
    },
    "correta": "D",
    "resolucao": "Na expressão 'só os de beleza', o artigo 'os' assume função de pronome de tratamento, pois é utilizado para referir-se a um grupo específico de forma distinta e formal, similar a expressões como 'os de bom senso' ou 'os de sabedoria'. Esse uso atribui um tratamento diferenciado à categoria mencionada, característico dos pronomes de tratamento.",
    "assunto": "Classes gramaticais - Pronomes"
    },
    {
    "enunciado": "A palavra 'FGTS' presente nesse texto, é resultado de um processo de formação de palavras chamado de:",
    "imagem": "static/imagens/fgts.jpg",
    "alternativas": {
        "A": "Sigla",
        "B": "Abreviação vocabular",
        "C": "Derivação sufixal",
        "D": "Onomatopeia",
        "E": "Derivação parassintética"
    },
    "correta": "A",
    "resolucao": "FGTS é a sigla de 'Fundo de Garantia do Tempo de Serviço'. Siglas são formadas pela inicial de cada palavra que compõe uma expressão, sendo um processo de formação de palavras muito comum na língua portuguesa para simplificar denominações longas.",
    "assunto": "Processo de formação de palavras"
    },
    {
    "enunciado": "Nos quatro primeiros versos do trecho da canção 'Paratodos' de Chico Buarque, há a presença da seguinte figura de linguagem:",
    "imagem": "static/imagens/paratodos.png", 
    "alternativas": {
        "A": "Zeugma",
        "B": "Elipse",
        "C": "Catacrese",
        "D": "Polissíndeto",
        "E": "Hipérbato"
    },
    "correta": "C",
    "resolucao": "Catacrese é o uso de uma palavra fora do seu sentido original por falta de um termo específico. No trecho da música, há expressões como 'perna de mesa' ou 'dente de alho', que são exemplos clássicos de catacrese.",
    "assunto": "Figuras de linguagem"
},
 {
    "enunciado": "A expressão coesiva 'por outro lado', no texto seguinte, apresenta:",
    "imagem": "static/imagens/noticia2.png", 
    "alternativas": {
        "A": "a finalidade de um argumento.",
        "B": "outro redirecionamento em relação ao que foi dito anteriormente.",
        "C": "a continuidade de um argumento.",
        "D": "a explicação de um argumento.",
        "E": "uma proposta que concorda com o que foi dito anteriormente"
    },
    "correta": "B",
    "resolucao": "A expressão 'por outro lado' é um conector que indica contraste ou oposição em relação ao que foi dito anteriormente. Ela introduz uma ideia contrária à decisão do STF, mostrando o posicionamento diferente da Câmara.",
    "assunto": "Coesão textual – conectores adversativos"
},
{
    "enunciado": "Assinale a alternativa em que a concordância verbal está incorreta.",
    "imagem": "",
    "alternativas": {
        "A": "As Minas Gerais fica ao norte de São Paulo.",
        "B": "Os Sertões contribuiu bastante para a historiografia brasileira.",
        "C": "Faz alguns minutos que estou esperando por você.",
        "D": "Vossas Excelências não sabem o quanto esse trabalho foi difícil de ser realizado.",
        "E": "Um grupo de turistas passeavam de barco."
    },
    "correta": "A",
    "resolucao": "A alternativa A apresenta erro de concordância verbal. O sujeito 'As Minas Gerais' está no plural, portanto o verbo também deveria estar: 'ficam'. A forma correta seria: 'As Minas Gerais ficam ao norte de São Paulo.'",
    "assunto": "Concordância verbal"
},
{
  "enunciado": "Assinale a alternativa em que a concordância nominal está incorreta.",
  "imagem": "",
  "alternativas": {
    "A": "É necessária cautela na resolução do problema.",
    "B": "Esse fato aconteceu bastantes vezes durante a viagem.",
    "C": "Minha amiga anda meio estranha desde que voltou das férias.",
    "D": "Encontrou argumentos o mais fáceis possível.",
    "E": "Não estamos sós."
  },
  "correta": "B",
  "resolucao": "A alternativa B apresenta erro de concordância nominal. A palavra 'bastantes' está incorreta, pois o correto é usar o advérbio 'bastante' que é invariável: 'bastante vezes'.",
  "assunto": "Concordância nominal"
},
{
  "enunciado": "Do ponto de vista da constituição do gênero textual, observam-se, no texto abaixo, características de um (a):",
  "texto": "O ministro do Supremo Tribunal Federal Teori Zavascki determinou anteontem que o Banco do Brasil desbloqueie ao governo de Minas Gerais os R$ 2,87 bilhões referentes aos depósitos judiciais oriundos de processos privados que, de acordo com a legislação estadual, deveriam ter sido pagos ao Executivo. A lei mineira permitia que o governo recebesse os recursos decorrentes de processos nos quais o Estado não é parte. Apesar de no fim do mês passado Teori ter acatado um pedido da Procuradoria-Geral da República (PGR) e suspendido o andamento dos processos relacionados à lei estadual, o ministro afirmou na decisão de anteontem que a sua manifestação liminar não possuía caráter retroativo, ou seja, não permitia que o BB bloqueasse o valor já liberado.",
  "imagem": "",
  "alternativas": {
    "a": "Conto",
    "b": "Artigo de opinião",
    "c": "Notícia",
    "d": "Artigo científico",
    "e": "Fábula"
  },
  "correta": "c",
  "resolucao": "A alternativa correta é a letra c) Notícia, pois o texto apresenta informações atuais, objetivas e fatuais sobre uma decisão do ministro do STF, característica típica do gênero textual notícia.",
  "assunto": "Gêneros textuais"
},
{
  "enunciado": "Leia os textos a seguir e responda à questão.",
  "texto": "TEXTO 1\n\nAbalou\n(Ivete Sangalo)\n\nVocê comigo é pá\nÉ mais do que sonhar\nAmor tão raro de se viver\nEu quero aproveitar esse momento pra te dizer...\n\n[...] \n\nAbalou, abalou, sacudiu balançou\nCoração é só felicidade\nAbalou, abalou isso sim é amor de verdade... 2x\n\nTEXTO 2\n\nEscolha uma:",
  "imagem": "static/imagens/bombril.jpeg",
  "enunciado2": "Qual a ração explícita entre esses textos?",
  "alternativas": {
    "a": "Hiperonímia",
    "b": "Antonímia",
    "c": "Intertextualidade",
    "d": "Personificação",
    "e": "Sinonímia"
  },
  "correta": "c",
  "resolucao": "A alternativa correta é a letra c) Intertextualidade, pois há referência a um texto conhecido da música popular (letra de Ivete Sangalo), demonstrando diálogo entre textos distintos.",
  "assunto": "Figuras e relações de linguagem"
},
{
    "enunciado":
        "Qual das palavras abaixo é formada por prefixação e sufixação? Marque a alternativa correta.\n\n"
        "Escolha uma:",
    "imagem": None,
    
    "alternativas": {
        "a": "sobretudo",
        "b": "história",
        "c": "entristecer",
        "d": "cantando",
        "e": "infelicidade"
    },
    "correta": "e",
    "resolucao": (
        "A formação por prefixação e sufixação ocorre quando uma palavra recebe ao mesmo tempo um prefixo (antes do radical) e um sufixo (depois do radical), "
        "sem perder sua autonomia.\n\n"
        "Vamos analisar as alternativas:\n"
        "a) \"sobretudo\" – palavra composta por justaposição, não há prefixo e sufixo adicionados ao mesmo radical.\n"
        "b) \"história\" – palavra primitiva, sem afixos.\n"
        "c) \"entristecer\" – possui prefixo (en-) e sufixo (-ecer), mas a base \"triste\" muda ligeiramente, então não é o melhor exemplo.\n"
        "d) \"cantando\" – apenas sufixação (-ando).\n"
        "e) \"infelicidade\" – possui prefixo \"in-\", radical \"felic\" e sufixo \"-idade\".\n\n"
        "Resposta correta: infelicidade (prefixação e sufixação)."
    ),
    "assunto": "Formação de palavras, prefixação e sufixação"
},
{
  "enunciado": "No trecho: “Quarenta e dois anos depois, Manuel Araya considera que tem de cumprir, ainda, uma última missão para Neruda: ‘Ajudar a provar que ele foi assassinado’”, os dois-pontos foram usados para:",
  "texto": "Cerca de quatro horas antes de Pablo Neruda morrer de um “câncer na próstata”, no domingo 23 de setembro de 1973, o homem que cuidava dele não pôde cumprir a sua última missão, interrompida pelos militares: comprar-lhe “um medicamento que, supostamente, aliviaria a dor do poeta”. Quarenta e dois anos depois, Manuel Araya considera que tem de cumprir, ainda, uma última missão para Neruda: “Ajudar a provar que ele foi assassinado”. O ex-funcionário está convencido de que o poeta não morreu pelas causas divulgadas oficialmente. É a única testemunha direta viva dos últimos dias do Nobel de Literatura, naqueles momentos iniciais do grande túnel que foi a ditadura de Augusto Pinochet, iniciado em 11 de setembro de 1973.",
  "imagem": None,
  "alternativas": {
    "a": "introduzir a frase que mostra qual a última missão de Manuel Araya para Neruda.",
    "b": "apresentar ao leitor uma lembrança do poeta Pablo Neruda.",
    "c": "mostrar uma sequência de fatos ocorridos após a morte de Pablo Neruda.",
    "d": "enumerar fatos.",
    "e": "inserir uma pergunta sobre a missão de Manuel Araya."
  },
  "correta": "a",
  "resolucao": "Os dois-pontos foram usados para **introduzir uma explicação** sobre o que seria a última missão de Manuel Araya para Neruda. Esse uso dos dois-pontos é típico quando se quer apresentar algo que será explicado ou exemplificado na sequência, como ocorre com a frase: \"Ajudar a provar que ele foi assassinado\".",
  "assunto": "Pontuação – uso dos dois-pontos"
},
{
  "enunciado": "Sobre o gênero desse texto é correto afirmar que:",
  "texto": "La Fontaine\n\nA Raposa convidou a Cegonha para jantar e lhe serviu sopa em um prato raso.\n\n— Você não está gostando de minha sopa? — perguntou, enquanto a cegonha bicava o líquido sem sucesso.\n\n— Como posso gostar? — a Cegonha respondeu, vendo a Raposa lamber a sopa que lhe pareceu deliciosa.\n\nDias depois foi a vez da Cegonha convidar a Raposa para comer na beira da lagoa. Serviu então a sopa num jarro largo embaixo e estreito em cima.\n\n— Hummmm, deliciosa! — exclamou a Cegonha, enfiando o comprido bico pelo gargalo. — Você não acha?\n\nA Raposa não achava nada, nem podia achar, pois seu focinho não passava pelo gargalo estreito do jarro. Tentou mais uma ou duas vezes e se despediu de mau humor, achando que, por algum motivo, aquilo não era nada engraçado.",
  "imagem": None,
  "enunciado2": "Sobre o gênero desse texto é correto afirmar que: \n 1- é um exemplo de género narrativo. \n II-os personagens são animais que são metaforizados a partir das condutas humanas, representando, assim, as virtudes ou vícios humanos. \n III esse texto, assim como a carta de reclamação, apresentam tempos verbais que exprimem possibilidades de acontecimentos. Escolha uma:",
  "alternativas": {
    "a": "Estão corretas I e II.", 
    "b": "Apenas I está correta.",
    "c": "Apenas II está correta.", 
    "d": "Apenas III está correta.",
    "e": "Estão corretas II e III."
  },
  "correta": "A",
  "resolucao": "A alternativa correta é a letra **a) Estão corretas I e II.**\n\n**I – Correta:** O texto é um exemplo de **gênero narrativo**, pois apresenta personagens, enredo, tempo e espaço.\n\n**II – Correta:** Os personagens são **animais com comportamentos humanos**, recurso típico das **fábulas**, que usam essas figuras para representar vícios e virtudes da sociedade.\n\n**III – Incorreta:** O texto **não utiliza tempos verbais para exprimir possibilidades** (como o modo subjuntivo em uma carta de reclamação), mas sim narrações em tempos do passado, típicos da fábula.\n\nPortanto, apenas as afirmações I e II estão corretas.",
  "assunto": "Gêneros textuais – Fábula"
},
{
  "enunciado": "Marque a alternativa correta.",
  "texto": None,
  "imagem": "static/imagens/tirinha2.jpeg",
  "alternativas": {
    "a": " A palavra 'se' da expressão ' se não' presente na tirinha é uma conjunção condicional.",
    "b": " A expressão ' se não ' presente na tirinha é uma locução adverbial de negação.",
    "c": " A expressão 'se não' presente na tirinha é uma locucão adverbial de dúvida.",
    "d": "A expressão  'se não' presente na tirinha é uma locução conjuntiva comparativa.",
    "e": "A expressão 'se não' presente na tirinha é uma locução conjuntiva concessiva."
  },
  "correta": "A",
  "resolucao": "Na frase “Eu nunca saberia se não tivesse tentado”, a expressão 'se não' introduz uma condição para o que está sendo dito. Isso caracteriza uma oração subordinada condicional, e o 'se' atua como conjunção condicional. Ou seja, a condição para saber alguma coisa era ter tentado.",
  "assunto": "Gêneros textuais – Fábula"
},
{
  "enunciado": "Há uma palavra formada por derivação prefixal e sufixal em:",
  "texto": None,
  "imagem": "static/imagens/tirinha2.jpeg",
  "alternativas": {
    "a": "Nave.",
    "b": "Suave.",
    "c": "Gente.",
    "d": "Infelizmente.",
    "e": "Entende."
  },
  "correta": "D",
  "resolucao": "A palavra 'infelizmente' é formada por derivação prefixal e sufixal. O radical é 'feliz', ao qual foi acrescentado o prefixo 'in-' e o sufixo '-mente'. Assim, temos uma palavra formada por prefixação (in-) e sufixação (-mente).",
  "assunto": " Derivação prefixal e sufixal"
},
{
    "enunciado": "O termo sublinhado indica uma circunstância de:",
    "texto": "Sempre me diziam que aquela cidade era bonita, mas eu não sabia que era <u>tanto</u>! Há uma vista maravilhosa, que fica diante do campo, e além disso, é possível ouvir os pássaros cantando alegremente.",
    "imagem": None,
    "alternativas": {
        "a": "Adição",
        "b": "Modo",
        "c": "Frequência",
        "d": "Intensidade",
        "e": "Atualidade"
    },
    "correta": "d",
    "resolucao": "O termo 'tanto' indica uma circunstância de intensidade, pois expressa o grau elevado da qualidade citada, ou seja, a grandeza da beleza da cidade. Por isso, a alternativa correta é intensidade.",
    "assunto": "Adjunto adverbial – Circunstância de intensidade"
},

{
  "enunciado": "No exemplo abaixo, veem-se o título e o subtítulo de uma notícia. Marque a alternativa correta.",
  "texto": "Atividade do comércio tem maior queda para outubro em 12 anos\n\nQueda de 3,3% ante setembro é pior resultado mensal do varejo neste ano.\n\nNo acumulado do ano, atividade varejista ainda registra expansão de 0,4%\n\n(Disponível em: http://g1.globo.com/economia/noticia/2015/11/atividade-do-comercio-tem-maior-queda-para-outubro-em-12-anos.html)",
  "imagem": None,
  "alternativas": {
    "a": "Depois de apresentar queda para dezembro, o mercado varejista mostra expectativa de diminuição para o ano seguinte.",
    "b": "Mesmo apresentarido queda para dezembro, o mercado varejista mostra aumento em relação aos demais meses do ano.",
    "c": "Mesmo apresentando queda para outubro, o mercado varejista mostra aumento de 80% em relação aos demais meses do ano.",
    "d": "Depois de apresentar queda para outubro, o mercado varejista mostra expectativa de diminuição para o ano seguinte.",
    "e": "Mesmo o comércio apresentando queda para outubro, o mercado varejista mostra aumento no acumulado do ano."
  },
  "correta": "e",
  "resolucao": "Apesar da queda de 3,3% na atividade do comércio em outubro, que representa o pior resultado mensal do ano, o texto informa que no acumulado do ano a atividade varejista ainda registra expansão de 0,4%. Portanto, a alternativa correta é a letra E, que mostra que apesar da queda em outubro, houve crescimento no acumulado do ano.",
  "assunto": "Interpretação de texto – Notícia econômica"
},
{
  "enunciado": "No primeiro quadro, na fala da professora, há a ocorrência de:",
  "texto": None,
  "imagem": "static/imagens/tirinha3.png",
  "enunciado2": None,
  "alternativas": {
    "a": "prosopopeia",
    "b": "catacrese",
    "c": "ironia",
    "d": "metáfora",
    "e": "aliteração"
  },
  "correta": "e",
  "resolucao": "A aliteração é caracterizada pela repetição de sons consonantais idênticos ou similares em palavras próximas. No trecho analisado, observa-se a repetição marcante do fonema /m/ em 'minha', 'mãe', 'me' e 'ama'.",
  "assunto": "Figuras de linguagem"
},
{
  "enunciado": "Marque a alternativa em que ocorre um caso de metonímia.",
  "texto": None,
  "imagem": None,
  "enunciado2": None,
  "alternativas": {
    "a": "Sentou-se para comer com os amigos.",
    "b": "Gostamos de ler Rachel de Queiroz.",
    "c": "Teus cabelos são luzes incandescentes.",
    "d": "Dei-lhe os pêsames.",
    "e": "Como chegou atrasado, não poderá realizar a prova."
  },
  "correta": "b",
  "resolucao": "A metonímia é uma figura de linguagem que substitui um termo por outro com o qual mantém uma relação de proximidade ou contiguidade. Na alternativa B, 'Rachel de Queiroz' (autora) substitui suas obras (livros), havendo uma relação entre o produtor e o produto, caracterizando metonímia.",
  "assunto": "Figuras de linguagem"
},
{
  "enunciado": "No trecho: 'Se não tivesse aderido aos protestos, não haveria se machucado', o conectivo 'se' poderia ser substituído, sem prejuízo para o sentido, por:",
  "texto": None,
  "imagem": None,
  "enunciado2": None,
  "alternativas": {
    "a": "mas",
    "b": "embora",
    "c": "a fim de que",
    "d": "porém",
    "e": "caso"
  },
  "correta": "e",
  "resolucao": "O conectivo 'se' introduz uma condição hipotética, função que também pode ser exercida por 'caso' sem alterar o sentido original da frase. As outras alternativas introduzem ideias de contraste ('mas', 'porém', 'embora') ou finalidade ('a fim de que'), que não se aplicam ao contexto.",
  "assunto": "Conectivos / Conjunções"
},
{
  "enunciado": "No trecho: 'O engenheiro e a médica saíram rapidamente. Seu filho permaneceu no local', ocorre:",
  "texto": None,
  "imagem": None,
  "enunciado2": None,
  "alternativas": {
    "a": "eufemismo",
    "b": "catacrese",
    "c": "metonímia",
    "d": "comparação",
    "e": "ambiguidade"
  },
  "correta": "e",
  "resolucao": "O pronome possessivo 'seu' gera ambiguidade, pois não fica claro se o filho pertence ao engenheiro, à médica ou ao casal. As outras figuras de linguagem não se aplicam: não há substituição por relação de contiguidade (metonímia), uso suavizado de expressão (eufemismo), uso impróprio de palavra (catacrese) ou termo comparativo.",
  "assunto": "Figuras de linguagem / Semântica"
},
{
  "enunciado": "Na charge abaixo, existe uma relação intertextual com um ditado popular bastante conhecido. Marque a alternativa referente a ele.",
  "texto": None,
  "imagem": "static/imagens/charge1.jpeg",
  "enunciado2": None,
  "alternativas": {
    "a": "Depois de fartos, não faltam pratos",
    "b": "A verdade gera o ódio",
    "c": "A instrução é a luz do espírito",
    "d": "Com tempo tudo se cura",
    "e": "A vaca foi pro brejo"
  },
  "correta": "e",
  "resolucao": "A charge faz uma paródia visual do ditado popular 'foi pro brejo', que significa que algo deu errado ou fracassou. A imagem da vaca literalmente no brejo, com a placa identificando o local, cria uma relação intertextual humorística com essa expressão idiomática.",
  "assunto": "Intertextualidade/Figuras de linguagem"
},
{
  "enunciado": "No trecho abaixo, o pronome relativo 'que' poderia ser substituído por:",
  "texto": "\"O Mapa da Violência é um trabalho desenvolvido pelo pesquisador Julio Jacobo Waiselfisz que, desde 1998, já divulgou 27 estudos. Todos eles, segundo a Flacso, trabalharam a distribuição por sexo das violências, sejam suicídios, homicídios ou acidentes de transporte, mas em 2012, dada a relevância do tema e as diversas solicitações nesse sentido, foi elaborado o primeiro mapa especificamente focado nas questões de género\".",
  "imagem": None,
  "enunciado2": None,
  "alternativas": {
    "a": "o qual",
    "b": "em que",
    "c": "na qual",
    "d": "a qual",
    "e": "no qual"
  },
  "correta": "a",
  "resolucao": "O pronome relativo 'que' refere-se ao pesquisador Julio Jacobo Waiselfisz (antecedente masculino singular). A substituição por 'o qual' mantém a correção gramatical e o sentido original, concordando em gênero e número com o antecedente. As outras alternativas não se aplicam: 'em que' (refere a lugar/tempo), 'na qual' (feminino), 'a qual' (feminino), 'no qual' (masculino mas exige preposição 'em').",
  "assunto": "Pronomes relativos"
},
{
  "enunciado": "A temática da tirinha da Mafalda faz uso de alguns sinais de pontuação, justificados pelo fato de:",
  "texto": None,
  "imagem": "static/imagens/charge2.webp",
  "enunciado2": None,
  "alternativas": {
    "a": "Vê-se que Mafalda se sente vulnerável aos apelos do consumismo.",
    "b": "As palavras entre aspas estão no modo imperativo negativo.",
    "c": "Tirinhas não podem ser utilizadas como meio de denúncia social.",
    "d": "Os questionamentos de Mafalda dizem respeito à preocupação com o fim do mundo.",
    "e": "Mafalda sente inquietude quanto à proposta de estímulo ao consumo."
  },
  "correta": "e",
  "resolucao": "Na tirinha, Mafalda demonstra incômodo com os comandos consumistas que ouve da televisão, como “USE”, “COMPRE” e “PROVE”. Ao questionar “O que eles pensam que nós somos?”, ela expressa sua inquietude diante da forma como a mídia trata as pessoas como meros consumidores. Por isso, a alternativa correta é a letra E, pois a tirinha revela a preocupação da personagem com o estímulo exagerado ao consumo.",
  "assunto": "Interpretação de texto/Recursos gráficos"
},
{
  "enunciado": "Sobre a linguagem empregada na tirinha, é correto afirmar que:",
  "texto": None,
  "imagem": "static/imagens/tirinha4.jpeg",
  "enunciado2": None,
  "alternativas": {
    "a": "corresponde a uma variedade linguística não padrão da língua portuguesa.",
    "b": "é uma linguagem empregada indistintamente por indivíduos de todas as classes sociais.",
    "c": "é uma linguagem cuja construção é inadmissível no uso da língua.",
    "d": "é uma linguagem usada apenas na modalidade escrita.",
    "e": "é uma linguagem que sofreu apenas influências de línguas estrangeiras."
  },
  "correta": "a",
  "resolucao": "A tirinha utiliza uma variedade linguística não padrão, caracterizada por marcas de oralidade e traços fonéticos regionais (como 'qui' no lugar de 'que', 'num' no lugar de 'não', 'vô' no lugar de 'vou'). Essa variação é legítima e representa uma variação regional.",
  "assunto": "Variação linguística"
},
{
  "enunciado": "Em 'flexibilizá-lo', o pronome faz referência à palavra:",
  "texto": "Doze anos depois da aprovação do Estatuto do Desarmamento, uma comissão especial da Câmara dos Deputados, dando mais uma lamentável demonstração de irresponsabilidade e ignorando os avanços conquistados pela sociedade brasileira, aprovou um projeto de lei que revoga o Estatuto do Desarmamento.\n\nDesde a aprovação do Estatuto, em 2003, dezenas de projetos de lei que buscavam flexibilizá-lo já foram formuladas, mas nenhum avançou. Agora, com o conservadorismo que se instalou no atual Congresso, isso pode mudar.",
  "imagem": None,
  "enunciado2": None,
  "alternativas": {
    "a": "Estatuto",
    "b": "Deputados",
    "c": "Conservadorismo",
    "d": "Mudar",
    "e": "Congresso"
  },
  "correta": "a",
  "resolucao": "O pronome oblíquo '-lo' em 'flexibilizá-lo' retoma o termo 'Estatuto do Desarmamento', mencionado anteriormente no texto. Essa referência é clara pelo contexto: os projetos de lei buscavam modificar (flexibilizar) as regras do Estatuto. As outras alternativas não mantêm coerência com o sentido da frase: não se flexibilizam deputados (b), conservadorismo (c), mudar (d) ou Congresso (e), mas sim uma lei/estatuto.",
  "assunto": "Referência pronominal/Coesão textual"
},
{
  "enunciado": "O verbo 'negar', no trecho abaixo, exigiu um complemento com preposição e outro sem ela. Marque a alternativa em que ocorre o mesmo fenômeno.",
  "texto": "A pena de morte por parte do Estado institucionaliza a pena de morte que já existe por parte dos bandidos. O Estado, quando decide matar, toma para si um direito que nega aos seus cidadãos. Logo, a pena de morte é uma contradição por parte do Estado.",
  "imagem": None,
  "enunciado2": None,
  "alternativas": {
    "a": "Obedeceu aos pais.",
    "b": "Assistiu a filmes diversos.",
    "c": "Foram morar juntos.",
    "d": "Casou-se com o melhor amigo.",
    "e": "Preferiu os amigos aos parentes."
  },
  "correta": "e",
  "resolucao": "O verbo 'negar' no texto apresenta dois complementos: um direto ('um direito') e outro indireto ('aos seus cidadãos'). Na alternativa E, o verbo 'preferir' também exige dois complementos: um direto sem preposição ('os amigos') e outro indireto com preposição ('aos parentes'), reproduzindo a mesma estrutura. As outras alternativas não apresentam essa dualidade: (a) e (b) têm apenas complemento indireto, (c) e (d) têm estruturas diferentes.",
  "assunto": "Regência verbal"
},
{
  "enunciado": "No fragmento abaixo, extraído de uma notícia, os travessões foram utilizados para:",
  "texto": "O Estado do Rio de Janeiro registrou neste ano, até 21 de outubro, 56.568 casos de dengue — mais de sete vezes o número registrado no mesmo período de 2014. Segundo a Secretaria Estadual de Saúde (7.819). Ocorreram 19 mortes — foram 10 em todo o ano passado. Atualmente, nenhum município fluminense enfrenta epidemia da doença, mas os números impressionam e deixam a população temerosa.",
  "imagem": None,
  "enunciado2": None,
  "alternativas": {
    "a": "separar frases explicativas",
    "b": "isolar uma pergunta",
    "c": "destacar uma citação que não pertence ao autor do texto",
    "d": "fazer perguntas",
    "e": "apresentar um pronunciamento de Alexandre Chieppe"
  },
  "correta": "a",
  "resolucao": "Os travessões no texto são usados para introduzir explicações ou informações adicionais, funcionando como uma forma de separar frases explicativas. Por exemplo, \"56.568 casos de dengue — mais de sete vezes...\" e \"19 mortes — foram 10...\" apresentam dados complementares que explicam ou detalham a informação principal. As outras alternativas não correspondem ao uso desses travessões no texto.",
  "assunto": "Pontuação"
},
{
  "enunciado": "No fragmento: \"Tenho certeza de que ele voltará\", a preposição \"de\" é necessária porque:",
  "texto": None,
  "imagem": None,
  "enunciado2": None,
  "alternativas": {
    "a": "O verbo \"ter\" a exige",
    "b": "A conjunção \"que\" a exige",
    "c": "O pronome \"ele\" a exige",
    "d": "A palavra \"certeza\" a exige",
    "e": "O verbo \"voltar\" a exige"
  },
  "correta": "d",
  "resolucao": "No trecho, a preposição \"de\" é exigida pela palavra \"certeza\", que rege complemento com preposição, estabelecendo a relação correta entre os termos. Nem o verbo \"ter\" nem a conjunção \"que\" exigem a preposição nesse contexto.",
  "assunto": "Classes gramaticais e termos da oração"
},
{
  "enunciado": "No seguinte trecho: \"Porém como a corrente do rio arrastou a carne verdadeira, com ela, foi também o seu reflexo e ficou o cão sem uma e sem outro.\" A expressão sublinhada faz referência, respectivamente:",
  "texto": "Um cão levava na boca um pedaço de carne, e, ao atravessar um rio, vendo a carne refletida na água, pareceu-lhe esta maior e soltou a que levava nos dentes para apanhar a que via dentro d'água. Porém como a corrente do rio arrastou a carne verdadeira, com ela foi também o seu reflexo e ficou o cão sem um e sem outro.",
  "imagem": None,
  "enunciado2": None,
  "alternativas": {
    "a": "Ao cão e a carne",
    "b": "Ao reflexo do rio e ao cão",
    "c": "Ao rio e ao reflexo do cão",
    "d": "A corrente do rio e a carne",
    "e": "A carne e ao reflexo da carne"
  },
  "correta": "e",
  "resolucao": "Na expressão sublinhada, 'ela' refere-se à carne verdadeira, e 'seu reflexo' refere-se ao reflexo da carne na água. Assim, a expressão indica que a corrente arrastou a carne e também seu reflexo, deixando o cão sem ambos.",
  "assunto": "Compreensão e interpretação de textos: Identificar as ideias principais e secundárias do texto"
},
{
  "enunciado": "No slogan da publicidade do desodorante AXE \"A primeira impressão é a que fica\", há:",
  "texto": None,
  "imagem": None,
  "enunciado2": None,
  "alternativas": {
    "a": "um período composto",
    "b": "uma oração com valor de substantivo",
    "c": "um período simples",
    "d": "apenas um verbo",
    "e": "mais de três verbos"
  },
  "correta": "a",
  "resolucao": "O slogan \"A primeira impressão é a que fica\" é um período composto porque contém duas orações: 'A primeira impressão é' e 'a que fica', ligadas pela oração subordinada adjetiva 'que fica'. Portanto, não é um período simples e contém mais de uma oração.",
  "assunto": "Analisar o uso dos gêneros textuais e das sequências discursivas"
},
{
  "enunciado": "A palavra \"sancionada\", no subtítulo da notícia abaixo, tem o mesmo sentido que:",
  "texto": "TSE aprova calendário eleitoral para as eleições municipais de 2016. Mudanças adaptam regras à minirreforma eleitoral sancionada neste ano.",
  "imagem": None,
  "enunciado2": None,
  "alternativas": {
    "a": "aprovação",
    "b": "consumismo",
    "c": "reprovação",
    "d": "interrupção",
    "e": "progressão"
  },
  "correta": "a",
  "resolucao": "No contexto da notícia, 'sancionada' significa que a minirreforma eleitoral foi aprovada oficialmente, ou seja, sancionada pelo poder competente. Portanto, o termo é sinônimo de 'aprovação' nesse caso.",
  "assunto": "Perceber o sentido contextual de palavras e expressões"
},
{
  "enunciado": "Do ponto de vista da constituição do gênero textual, observam-se, no texto abaixo, características de um(a):",
  "texto": "Brigadeiro\n\nIngredientes:\n* 1 Colher de sopa - Manteiga ou Margarina\n* 1 Lata - Leite Condensado\n* 4 Colheres de sopa - Chocolate em Pó\n* 1 Pacote - Chocolate Granulado\n\nModo de preparo:\n\n1. Aqueça a panela em fogo médio.\n\n2. Acrescente uma colher de sopa de manteiga.\n\n3. Logo após, utilize todo o Leite Condensado junto à manteiga\n\n4. Em seguida, acrescente 4 colheres de sopa de Chocolate em Pó e mexa sem parar até desgrudar da panela.\n\n5. Unte um recipiente onde a mistura será despejada e faça pequenas bolas com a mão passando a mistura no chocolate granulado.\n\n(Disponível em: http://www.comofazerbrigadeiro.com.br/)",
  "imagem": None,
  "enunciado2": None,
  "alternativas": {
    "a": "Notícia",
    "b": "Receita culinária",
    "c": "Artigo de opinião",
    "d": "Conto",
    "e": "Fábula"
  },
  "correta": "b",
  "resolucao": "O texto apresenta as características típicas de uma receita culinária: lista de ingredientes e modo de preparo em etapas numeradas. Isso o diferencia de outros gêneros textuais como notícia, conto ou artigo de opinião.",
  "assunto": "Analisar o uso dos gêneros textuais e das sequências discursivas"
},
{
  "enunciado": "O verbo \"ser\", no excerto abaixo, possui um sujeito:",
  "texto": "A ascensão das mulheres às altas esferas corporativas é rara. Elas ocupam menos de 20% dos cargos de responsabilidade nas quinhentas empresas mais importantes do mundo, segundo a lista elaborada pela Fortune.",
  "imagem": None,
  "enunciado2": None,
  "alternativas": {
    "a": "oculto",
    "b": "simples",
    "c": "implícito",
    "d": "composto",
    "e": "indeterminado"
  },
  "correta": "b",
  "resolucao": "No excerto, o sujeito do verbo \"ser\" é \"A ascensão das mulheres às altas esferas corporativas\", que é um sujeito simples (apenas um núcleo: \"ascensão\"). Portanto, o sujeito não é oculto, implícito, composto ou indeterminado.",
  "assunto": "Classes gramaticais e termos da oração"
},
{
  "enunciado": "Marque a alternativa em que há metáfora:",
  "texto": None,
  "imagem": None,
  "enunciado2": None,
  "alternativas": {
    "a": "Teus cabelos são luzes incandescentes.",
    "b": "Como chegou atrasado, não poderá realizar a prova.",
    "c": "Teus cabelos são como a luz do dia.",
    "d": "Prestamos-lhes nossos sinceros pêsames.",
    "e": "O mingau virou água."
  },
  "correta": "a",
  "resolucao": "Na alternativa (a), há metáfora, pois 'teus cabelos são luzes incandescentes' faz uma comparação implícita entre cabelos e luzes sem o uso de conectivos comparativos, caracterizando a metáfora. A alternativa (c) usa comparação explícita (como), e as demais não apresentam metáfora.",
  "assunto": "Recursos de estilo: conotação e denotação, figuras de linguagem"
},
{
  "enunciado": "No exemplo abaixo, o conectivo 'e' exprime uma ideia de:",
  "texto": "Imagem com o logo da Nescau e a frase: 'Energia que dá gosto. E barriga.'",
  "imagem": "static/imagens/nescau.jpeg",
  "enunciado2": None,
  "alternativas": {
    "a": "Conclusão",
    "b": "Finalidade",
    "c": "Adição",
    "d": "Condição",
    "e": "Alternância"
  },
  "correta": "c",
  "resolucao": "O conectivo 'e' une duas ideias: 'Energia que dá gosto' e 'Energia que dá barriga'. Como não há oposição nem consequência, o 'e' indica apenas soma de informações, ou seja, adição.",
  "assunto": "Coordenação e subordinação"
},
{
  "enunciado": "O sujeito do verbo 'calar', na tira abaixo, é:",
  "texto": None,
  "imagem": "static/imagens/tirinha5.gif",
  "enunciado2": None,
  "alternativas": {
    "a": "o verbo 'consentir'.",
    "b": "o vocábulo 'bonitinha'.",
    "c": "o pronome 'quem'.",
    "d": "a palavra 'espelho'.",
    "e": "o pronome 'alguém'."
  },
  "correta": "c",
  "resolucao": "Na tira, a personagem diz: 'Há alguém mais bonitinha do que eu?'. O espelho responde: 'Quem cala, consente!'. O sujeito do verbo 'calar' está oculto, mas pode ser identificado como o pronome interrogativo 'quem', que aparece na fala do espelho e é o responsável pela ação de 'calar'.",
  "assunto": "Classes gramaticais e termos da oração"
},
{
  "enunciado": "O verbo 'negar', no trecho abaixo, exigiu um complemento com preposição e outro sem ela. Marque a alternativa em que ocorre o mesmo fenômeno.",
  "texto": "A pena de morte por parte do Estado institucionaliza a pena de morte que já existe por parte dos bandidos. O Estado, quando decide matar, toma para si um direito que nega aos seus cidadãos. Logo, a pena de morte é uma contradição por parte do Estado.",
  "imagem": None,
  "enunciado2": "Disponível em: https://acidblacknerd.wordpress.com/2013/05/02/pe-de-morte-10-motivos-para-ser-contra-10-motivos-para-ser-a-favor/",
  "alternativas": {
    "a": "Obedeceu aos pais.",
    "b": "Assistiu a filmes diversos.",
    "c": "Foram morar juntos.",
    "d": "Casou-se com o melhor amigo.",
    "e": "Preferiu os amigos aos parentes."
  },
  "correta": "e",
  "resolucao": "No trecho, o verbo 'negar' exige dois complementos: um sem preposição ('um direito') e outro com preposição ('aos seus cidadãos'). A alternativa (e) repete esse fenômeno: o verbo 'preferir' exige um complemento direto ('os amigos') e outro indireto ('aos parentes').",
  "assunto": "Sintaxe de concordância e regência"
},
{
  "enunciado": "Marque a resposta correta. Na tirinha abaixo, observa-se que:",
  "texto": None,
  "imagem": "static/imagens/tirinha6.gif",
  "enunciado2": None,
  "alternativas": {
    "a": "Por infringir uma regra de concordância, Chico Bento, personagem de Mauricio de Sousa, tem sua variedade linguística respeitada e aceita pela professora.",
    "b": "Por infringir uma regra de concordância, Chico Bento, personagem de Mauricio de Sousa, é acolhido pela professora que, de pronto, reconhece a variedade linguística trazida pelo aluno.",
    "c": "Por infringir uma regra de concordância, Chico Bento, personagem de Mauricio de Sousa, é recriminado pela professora, mas ela reconhece e respeita a variedade linguística.",
    "d": "Por infringir uma regra de concordância, Chico Bento, personagem de Mauricio de Sousa, é repreendido pela professora que, de pronto, ignora a variedade linguística trazida pelo aluno.",
    "e": "Por infringir uma regra de concordância, Chico Bento, personagem de Mauricio de Sousa, é acolhido pela professora que, de pronto, reconhece e respeita a variedade linguística trazida pelo aluno."
  },
  "correta": "d",
  "resolucao": "Na tirinha, Chico Bento usa sua variedade linguística regional, mas é repreendido pela professora, que não reconhece nem respeita sua forma de falar. Isso revela uma atitude de negação da diversidade linguística por parte da educadora.",
  "assunto": "Norma padrão e variedades da língua"
},
{
  "enunciado": "Entre os dois períodos abaixo, existe uma relação semântica de:",
  "texto": "Só conhecem o pronome 'cujo' as pessoas que têm um longo histórico de escolarização e tiveram contato com ele por meio de textos escritos. Mas nem mesmo essas pessoas empregam corretamente esse pronome em sua fala diária ou mesmo em sua produção escrita habitual.",
  "imagem": None,
  "enunciado2": "BAGNO, M. Não é errado falar assim. São Paulo: Parábola Editorial, 2009, p. 123-124.",
  "alternativas": {
    "a": "oposição",
    "b": "tempo",
    "c": "causa",
    "d": "alternancia",
    "e": "finalidade"
  },
  "correta": "a",
  "resolucao": "A conjunção 'mas' introduz uma ideia que contrasta com a anterior: mesmo as pessoas que tiveram acesso ao pronome 'cujo' por meio da escolarização não o utilizam corretamente. Isso configura uma relação de oposição.",
  "assunto": "Coordenação e subordinação"
},
{
  "enunciado": "A palavra 'Planalto', presente nesse texto, é resultado de um processo de formação de palavras chamado de:",
  "texto": None,
  "imagem": "static/imagens/cartaz2.jpeg",
  "enunciado2": None,
  "alternativas": {
    "a": "composição por aglutinação",
    "b": "derivação parassintética",
    "c": "composição por justaposição",
    "d": "derivação regressiva",
    "e": "derivação imprópria"
  },
  "correta": "a",
  "resolucao": "A palavra 'Planalto' resulta da junção de 'plano' + 'alto', em que há alteração fonética (a vogal final de 'plano' desaparece). Isso caracteriza a composição por aglutinação, pois ocorre a união de dois radicais com perda de elementos sonoros.",
  "assunto": "Estrutura e formação das palavras"
},
{
  "enunciado": "No segundo quadrinho da tirinha, há a presença da seguinte figura de linguagem:",
  "texto": None,
  "imagem": "static/imagens/tirinha7.jpeg",
  "enunciado2": None,
  "alternativas": {
    "a": "metáfora",
    "b": "elipse",
    "c": "catacrese",
    "d": "polissindeto",
    "e": "prosopopéia"
  },
  "correta": "a",
  "resolucao": "No segundo quadrinho, a expressão 'Meu amor é uma caravana de rosas vagando num deserto inefável de paixão' é uma comparação implícita entre o amor e elementos simbólicos (caravana de rosas, deserto de paixão), sem o uso de conectivos comparativos. Isso caracteriza a figura de linguagem chamada metáfora.",
  "assunto": "Recursos de estilo: conotação e denotação, figuras de linguagem"
},
{
    "enunciado": "No período abaixo, o conectivo 'enquanto' possui valor semântico de:",
    "texto": "Os homicídios de mulheres negras aumentaram 54% em dez anos no Brasil passando de 1.964 em 2003, para 2.875, em 2013. Enquanto no mesmo período, o número de homicídios de mulheres brancas caiu 9,8%, saindo de 1.747 em 2003 para 1.576 em 2013. É o que aponta o Mapa da Violência 2015: Homicídio de Mulheres no Brasil, estudo elaborado pela Faculdade Latino-Americana de Ciências Sociais (Flacso), divulgado nesta segunda-feira (9).",
    "imagem": None,
    "alternativas": {
        "A": "Explicação",
        "B": "Causa",
        "C": "Tempo",
        "D": "Finalidade",
        "E": "Conclusão"
    },
    "correta": "C",
    "resolucao": "O conectivo 'enquanto' neste contexto estabelece uma relação de simultaneidade temporal entre os dois fatos apresentados: o aumento dos homicídios de mulheres negras e a diminuição dos homicídios de mulheres brancas ocorreram no mesmo período (dez anos). A expressão 'no mesmo período' reforça o valor temporal do conectivo, indicando que os eventos aconteceram ao mesmo tempo. Não expressa causa, explicação, finalidade ou conclusão, mas sim a coincidência temporal dos dois eventos contrastantes.",
    "assunto": "Valores semânticos de conectivos"
},
{
    "enunciado": "Qual das palavras abaixo é formada por prefixação e sufixação? Marque a alternativa correta.",
    "imagem": None,
    "alternativas": {
        "A": "cantando",
        "B": "entristecer",
        "C": "história",
        "D": "infelicidade",
        "E": "sobretudo"
    },
    "correta": "B",
    "resolucao": "A palavra 'entristecer' é formada pelo processo de derivação parassintética, que combina prefixação e sufixação simultaneamente. Analisando sua estrutura:\n\n- Prefixo: 'en-' (que indica ação de tornar)\n- Radical: 'trist-' (advindo de 'triste')\n- Sufixo: '-ecer' (que forma verbos)\n\nA formação ocorre de maneira simultânea, sendo necessários ambos os afixos para constituir a palavra. As outras alternativas não apresentam essa característica:\n\na) 'cantando' - forma verbal (gerúndio) do verbo cantar\nc) 'história' - palavra primitiva, não derivada\nd) 'infelicidade' - formada apenas por prefixação (in-) e sufixação (-dade)\ne) 'sobretudo' - composição por justaposição (sobre + tudo)",
    "assunto": "Processos de formação de palavras - derivação parassintética"
},



]

def questao_aleatoria():
    return random.choice(banco_questoes)

def questao_aleatoria_nao_repetida(respondidas=None):
    if respondidas is None:
        respondidas = []

    restantes = [q for q in banco_questoes if q['enunciado'] not in respondidas]

    if not restantes:
        return None

    return random.choice(restantes)
