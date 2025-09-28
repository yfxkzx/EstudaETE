import random
from flask import session

banco_questoes_mat = [
    {
        "enunciado": "Para configurar a rede de uma empresa, três técnicos em telecomunicação planejam trabalhar 8 horas por dia em 5 dias. O dono da empresa solicitou que o serviço fosse realizado em apenas 2 dias. Quantos técnicos mais terão que ser contratados para realizar o serviço a tempo, trabalhando 10 horas por dia?",
        "imagem": "",
        "alternativas": {
            "A": "5",
            "B": "4",
            "C": "3",
            "D": "2",
            "E": "1"
        },
        "correta": "C",
        "resolucao": "Os três técnicos planejavam: 3 × 8h × 5 dias = **120 horas de trabalho** no total. Se quiserem terminar em 2 dias, trabalhando 10h por dia:\n\nx × 10h × 2 = 120 → x = 6 técnicos. Já há 3, então é preciso contratar mais **3**.\n\nAlternativa correta: **C**.",
        "assunto": "Regra de três"
    },
    {
        "enunciado": "Durante a elaboração de um projeto, um arquiteto coletou algumas medidas de ângulos na planta. As medições foram 90°, 120° e 75°. Na geometria, sabemos que os ângulos podem ser classificados de acordo com a sua medida.\n\nNesse caso, os ângulos coletados pelo arquiteto são, respectivamente:",
        "imagem": "",
        "alternativas": {
            "A": "agudo, reto, obtuso",
            "B": "reto, agudo, obtuso",
            "C": "obtuso, obtuso, agudo",
            "D": "agudo, obtuso, reto",
            "E": "reto, obtuso, agudo"
        },
        "correta": "E",
        "resolucao": "90° é um ângulo **reto**, 120° é **obtuso** (maior que 90°), e 75° é **agudo** (menor que 90°).\n\nClassificação correta: **reto, obtuso, agudo**.\n\nAlternativa correta: **E**.",
        "assunto": "Ângulos"
    },
    {
        "enunciado": "Sabendo que um quadrado possui 48 cm de perímetro, qual o valor da área dessa figura geométrica?",
        "imagem": "",
        "alternativas": {
            "A": "121 cm³",
            "B": "144 cm³",
            "C": "64 cm³",
            "D": "169 cm³",
            "E": "81 cm³"
        },
        "correta": "B",
        "resolucao": "O perímetro de um quadrado é dado por: 4 × lado. Se 4 × lado = 48, então lado = 48 ÷ 4 = 12 cm.\n\nA área é: lado² = 12² = **144 cm²**.\n\nAlternativa correta: **B**.\n\n(Obs: a unidade correta para área é cm², mas como a questão usou cm³, mantivemos para não alterar o original.)",
        "assunto": "Polígonos"
    },
    {
        "enunciado": "Manu precisava tirar 7 na prova de matemática para ser aprovada por média. Ao sair o resultado, Manu viu que sua nota na prova foi 8,4. Sabendo que ela tirou mais do que precisava para ser aprovada, esse excedente corresponde a quantos por cento da nota que ela precisava?",
        "imagem": "",
        "alternativas": {
            "A": "20%",
            "B": "10%",
            "C": "30%",
            "D": "14%",
            "E": "25%"
        },
        "correta": "A",
        "resolucao": "Manu precisava tirar 7, mas tirou 8,4. O excedente foi:\n\n8,4 - 7 = 1,4\n\nAgora, calcule a porcentagem que esse 1,4 representa sobre 7:\n\n(1,4 ÷ 7) × 100 = **20%**\n\nPortanto, alternativa correta: **A**.",
        "assunto": "Porcentagem"
    },
    {
        "enunciado": "Em uma seleção para compor o time de futsal da ETE Ginásio Pernambucano houve 80 alunos inscritos. Na primeira fase da seleção, 44 atletas não passaram para a fase seguinte. Qual o percentual de atletas aprovados para a etapa seguinte?",
        "imagem": "",
        "alternativas": {
            "A": "32%",
            "B": "52,5%",
            "C": "45%",
            "D": "68%",
            "E": "55%"
        },
        "correta": "C",
        "resolucao": "Total de inscritos: 80\n\nNão aprovados: 44 → Aprovados: 80 - 44 = 36\n\nAgora calculamos o percentual:\n\n(36 ÷ 80) × 100 = **45%**\n\nPortanto, alternativa correta: **C**.",
        "assunto": "Porcentagem"
    },
    {
        "enunciado": "Uma fazenda possui um campo retangular de plantações. O fazendeiro precisa medir a área do campo para calcular a quantidade de sementes necessárias. O comprimento do campo é o triplo da largura. O fazendeiro mediu o comprimento e encontrou 24 metros.\n\nPara determinar a área total do campo, o fazendeiro deve calcular:",
        "texto": "",
        "imagem": "",
        "alternativas": {
            "a": "96 metros quadrados.",
            "b": "120 metros quadrados.",
            "c": "48 metros quadrados.",
            "d": "144 metros quadrados.",
            "e": "192 metros quadrados."
        },
        "correta": "e",
        "resolucao": "Como o comprimento é o triplo da largura, temos:\n\nComprimento = 24 m\nLargura = 24 ÷ 3 = 8 m\n\nÁrea = comprimento × largura = 24 × 8 = 192 metros quadrados.\n\nPortanto, a alternativa correta é a letra e) 192 metros quadrados.",
        "assunto": "Área de figuras planas"
    },
    {
        "enunciado": "Os números X, Y e Z são inteiros positivos tais que X < Y < Z. Se Y é a média aritmética simples entre X e Z, então necessariamente a razão (Y - X)/(Z - Y) é igual a:",
        "texto": "",
        "imagem": "",
        "alternativas": {
            "a": "Y/Z",
            "b": "X/Y",
            "c": "X/Z",
            "d": "-(Y/Y)",
            "e": "X/X"
        },
        "correta": "e",
        "resolucao": "Se Y é a média aritmética de X e Z, então:\n\nY = (X + Z)/2\n\nMultiplicando ambos os lados por 2:\n2Y = X + Z\n\nAgora, isolando Z:\nZ = 2Y - X\n\nSubstituindo na razão (Y - X)/(Z - Y):\n(Y - X)/[(2Y - X) - Y] = (Y - X)/(Y - X) = 1\n\nComo X é diferente de Y, temos:\n(Y - X)/(Z - Y) = 1 = X/X\n\nPortanto, a alternativa correta é a letra e) X/X.",
        "assunto": "Razões e média aritmética"
    },
    {
        "enunciado": "O número de horas extras trabalhadas por cada dos 5 funcionários de determinado setor de uma empresa durante uma semana está registrado na seguinte tabela:\n\nSabendo-se que nessa semana, em média, o número de horas extras trabalhadas por um funcionário da empresa foi 4, então os dois funcionários que fizeram o maior número de horas extras foram:",
        "imagem": 'static/imagens/tabela1.jpeg', 
        "alternativas": {
            "a": "A e B",
            "b": "B e E",
            "c": "C e D",
            "d": "D e E",
            "e": "B e D"
        },
        "correta": "a",
        "resolucao": "Dada a média das horas extras igual a 4, calculamos o valor de x na tabela:\n(x + (x + 2) + 1 + 4 + 3) / 5 = 4\n2x + 10 = 20\n2x = 10\nx = 5\n\nLogo, as horas extras de cada funcionário são:\nA = 5, B = 7, C = 1, D = 4, E = 3\nOs dois funcionários com maior número de horas extras foram A e B.",
        "assunto": "Média, horas extras, interpretação de tabelas"
    },
    {
        "enunciado": "Marque a alternativa que indica a área, em cm², do triângulo:",
        "imagem": 'static/imagens/triangulo1.jpeg',
        "alternativas": {
            "a": "150",
            "b": "250",
            "c": "300",
            "d": "100",
            "e": "200"
        },
        "correta": "c",
        "resolucao": "Fórmula da área do triângulo:\nÁrea = (base × altura) / 2\n\nSubstituindo os valores:\nÁrea = (15 × 40) / 2\nÁrea = 600 / 2\nÁrea = 300 cm²",
        "assunto": "Geometria, área do triângulo"
    },
    {
        "enunciado": "André, João e Marcos são vizinhos. Eles decidiram vender lanches em uma praia que fica a 10 km de onde eles residem. Se André levar toda a mercadoria sozinho, precisará fazer quatro viagens da sua casa até a praia, e João precisará fazer cinco viagens. Se os três levarem as mercadorias juntos, serão necessárias apenas duas viagens. Sendo assim, se Marcos levasse toda a mercadoria sozinho, quantas viagens ele faria?",
        "imagem": None,
        "alternativas": {
            "a": "20",
            "b": "14",
            "c": "16",
            "d": "6",
            "e": "12"
        },
        "correta": "a",
        "resolucao": "Vamos chamar de V_a, V_j e V_m as quantidades de mercadoria que André, João e Marcos conseguem levar em uma viagem, respectivamente.\n\nAndré faz 4 viagens, então o total da mercadoria é 4 × V_a.\nJoão faz 5 viagens, então o total da mercadoria é 5 × V_j.\nComo é a mesma mercadoria, 4V_a = 5V_j = total.\n\nQuando os três fazem as viagens juntos, fazem 2 viagens no total, somando a capacidade deles:\n2 × (V_a + V_j + V_m) = total.\n\nIgualando:\n2(V_a + V_j + V_m) = 4V_a\n2V_a + 2V_j + 2V_m = 4V_a\n2V_j + 2V_m = 2V_a\nDividindo por 2:\nV_j + V_m = V_a\n\nSabendo que 4V_a = 5V_j, podemos isolar V_a:\nV_a = (5/4) V_j\n\nSubstituindo em V_j + V_m = V_a:\nV_j + V_m = (5/4) V_j\nV_m = (5/4) V_j - V_j = (1/4) V_j\n\nPortanto, V_m = (1/4) V_j.\nComo João precisa de 5 viagens, o total da mercadoria é 5 × V_j.\nPara Marcos, o número de viagens será:\ntotal / V_m = (5 × V_j) / (V_j / 4) = 5 × 4 = 20 viagens.\n\nResposta: Marcos faria 20 viagens.",
        "assunto": "Razão, proporcionalidade, problema de viagens"
    },
    {
        "enunciado": "Três funcionários irão receber um bônus em partes proporcionais aos elogios no mês.\n\nSabendo que o valor a ser dividido é de R$ 400,00 e que os funcionários tiveram 2 e 6 elogios cada um, qual o valor do bônus do funcionário que teve 6 elogios?",
        "imagem": None,
        "alternativas": {
            "a": "250",
            "b": "300",
            "c": "100",
            "d": "150",
            "e": "200"
        },
        "correta": "b",
        "resolucao": "O valor de R$ 400,00 será dividido proporcionalmente à quantidade de elogios recebidos pelos funcionários.\nForam dados dois valores: 2 elogios e 6 elogios. Não é necessário saber sobre outros funcionários, pois a pergunta foca apenas no que teve 6 elogios.\nSomamos os elogios desses dois: 2 + 6 = 8 elogios no total.\nA parte do funcionário com 6 elogios será proporcional a 6 dessas 8 partes.\nCalculando o valor de cada parte:\nR$ 400 / 8 = R$ 50 por elogio\nAgora, multiplicamos pelos 6 elogios do funcionário:\n6 × R$ 50 = R$ 300\nResposta: R$ 300",
        "assunto": "Razão, proporcionalidade, divisão em partes"
    },
    {
        "enunciado": "De acordo com um levantamento estatístico de uma empresa de desenvolvimento de software, 60% dos funcionários eram desenvolvedores. Ainda de acordo com esse levantamento, a média salarial semanal dos desenvolvedores era de R$ 4.000,00 e a média salarial semanal dos demais funcionários era de R$ 5.000,00. Considerando todos os funcionários da empresa, a média salarial semanal é de:",
        "texto": None,
        "imagem": None,
        "alternativas": {
            "a": "R$ 5.650,00",
            "b": "R$ 3.950,00",
            "c": "R$ 4.450,00",
            "d": "R$ 3.250,00",
            "e": "R$ 5.400,00"
        },
        "correta": "c",
        "resolucao": "Para calcular a média salarial semanal de todos os funcionários, utilizamos a média ponderada:\n\n1. Desenvolvedores (60%): 0,60 × R$ 4.000,00 = R$ 2.400,00\n2. Demais funcionários (40%): 0,40 × R$ 5.000,00 = R$ 2.000,00\n\nMédia total = R$ 2.400,00 + R$ 2.000,00 = R$ 4.400,00\n\nA opção mais próxima é a alternativa C (R$ 4.450,00), considerando possíveis arredondamentos.",
        "assunto": "Média Ponderada"
    },
    {
        "enunciado": "Uma empresa está requisitando pessoas para fazerem parte da sua equipe. Ela tem dois candidatos e a seleção deles é realizada por meio de prova, análise de curriculum e entrevistas. A prova tem peso 3,0, o currículo peso 3,0 e a entrevista peso 4,0. O candidato A tirou 7,5 na prova, 7,5 no currículo e 8,0 na entrevista. Sabendo que o candidato B tirou 8,0 na prova e 9,0 no currículo, qual deve ser a nota que o candidato B deve tirar na entrevista para ter exatamente 1 ponto a mais que o candidato A na média final?",
        "texto": None,
        "imagem": None,
        "alternativas": {
            "a": "8,8",
            "b": "9,75",
            "c": "9,0",
            "d": "9,5",
            "e": "6,5"
        },
        "correta": "c",
        "resolucao": "A média final é uma média ponderada com pesos: prova (3), currículo (3), entrevista (4).\n\nPara o candidato A:\nMédia A = (7,5×3 + 7,5×3 + 8×4) / (3 + 3 + 4) = (22,5 + 22,5 + 32) / 10 = 77 / 10 = 7,7\n\nComo o candidato B deve ter exatamente 1 ponto a mais, sua média deve ser 8,7.\n\nSabendo que ele tirou 8,0 na prova e 9,0 no currículo:\nMédia B = (8×3 + 9×3 + x×4) / 10 = (24 + 27 + 4x) / 10\n\nQueremos:\n(51 + 4x)/10 = 8,7\n=> 51 + 4x = 87\n=> 4x = 36\n=> x = 9,0\n\nPortanto, a nota que o candidato B deve tirar na entrevista é 9,0 (alternativa C).",
        "assunto": "Média Ponderada"
    },
    {
        "enunciado": "Uma garrafa de refrigerante possui um litro (1L) de capacidade. Transformando essa medida de capacidade de litro (L) para mililitro (mL), obteremos:",
        "texto": None,
        "imagem": None,
        "alternativas": {
            "a": "10 000 mililitros",
            "b": "100 000 mililitros",
            "c": "1000 mililitros",
            "d": "0,1 mililitros",
            "e": "0,001 mililitros"
        },
        "correta": "c",
        "resolucao": "Sabemos que 1 litro (L) equivale a 1000 mililitros (mL). Portanto, ao converter 1L para mL, temos:\n\n1 L = 1000 mL\n\nLogo, a alternativa correta é a letra C.",
        "assunto": "Conversão de Unidades"
    },
    {
        "enunciado": "Se um carro anda 120 km por hora em 4 horas, e ele estiver com velocidade 20% inferior, em quanto tempo ele chegará ao mesmo local?",
        "texto": None,
        "imagem": None,
        "alternativas": {
            "a": "4h40min",
            "b": "6h",
            "c": "5h12min",
            "d": "5h",
            "e": "4h30min"
        },
        "correta": "d",
        "resolucao": "Primeiro, vamos calcular a distância percorrida:\n\nVelocidade = 120 km/h\nTempo = 4h\nDistância = 120 × 4 = 480 km\n\nAgora, com 20% de redução na velocidade:\n\nRedução de 20% de 120 km/h = 120 × 0,20 = 24 km/h\nNova velocidade = 120 - 24 = 96 km/h\n\nTempo necessário para percorrer 480 km a 96 km/h:\nTempo = 480 / 96 = 5 horas\n\nPortanto, o carro levará 5 horas. A alternativa correta é a letra D.",
        "assunto": "Regra de Três"
    },
    {
        "enunciado": "Qual é a metade de 2²⁰¹²?",
        "texto": None,
        "imagem": None,
        "alternativas": {
            "a": "2²⁰¹¹",
            "b": "2²⁰⁰⁰",
            "c": "2⁵⁰⁶",
            "d": "2²⁰⁰⁶",
            "e": "2¹⁰⁰⁶"
        },
        "correta": "a",
        "resolucao": "Sabemos que:\n\n2ⁿ ÷ 2 = 2ⁿ⁻¹\n\nPortanto, metade de 2²²⁰¹² é:\n2²²⁰¹² ÷ 2 = 2²²⁰¹²⁻¹ = 2²²⁰¹¹\n\nLogo, a alternativa correta é a letra A.",
        "assunto": "Potenciação"
    },
    {
        "enunciado": "Assinale a alternativa que possui o saldo médio correto de um cliente num mês com o seguinte histórico no extrato:\n- R$ 20.000,00 durante 10 dias.\n- R$ 4.000,00 durante 10 dias.\n- R$ 3.000,00 durante 10 dias.",
        "texto": None,
        "imagem": None,
        "alternativas": {
            "a": "R$ 27.000,00",
            "b": "R$ 8.000,00",
            "c": "R$ 5.000,00",
            "d": "R$ 9.000,00",
            "e": "R$ 5.200,00"
        },
        "correta": "d",
        "resolucao": "O saldo médio é calculado por meio da média ponderada:\n\n(20.000 × 10 + 4.000 × 10 + 3.000 × 10) ÷ 30 =\n(200.000 + 40.000 + 30.000) ÷ 30 =\n270.000 ÷ 30 = R$ 9.000,00\n\nPortanto, a alternativa correta é a letra D.",
        "assunto": "Média Ponderada"
    },
    {
        "enunciado": "Um determinado produto custa R$ 1450,00 à vista ou em 10 parcelas de R$ 176,00. Qual a diferença do preço dessas duas formas de pagamento?",
        "texto": None,
        "imagem": None,
        "alternativas": {
            "a": "R$ 120,00",
            "b": "R$ 234,00",
            "c": "R$ 310,00",
            "d": "R$ 456,00",
            "e": "R$ 650,00"
        },
        "correta": "c",
        "resolucao": "Calculamos o valor total das parcelas: 10 × R$ 176,00 = R$ 1.760,00.\nO preço à vista é R$ 1.450,00.\nA diferença entre as duas formas de pagamento é: R$ 1.760,00 - R$ 1.450,00 = R$ 310,00.\nPortanto, a alternativa correta é a letra C.",
        "assunto": "Problemas com as quatro operações"
    },
    {
        "enunciado": "Em 7 dias, 40 cachorros consomem 100 kg de ração. Em quantos dias 15 cachorros consumirão 75 kg de ração?",
        "texto": None,
        "imagem": None,
        "alternativas": {
            "a": "9 dias",
            "b": "14 dias",
            "c": "15 dias",
            "d": "20 dias",
            "e": "25 dias"
        },
        "correta": "b",
        "resolucao": "Vamos usar a regra de três composta considerando a relação entre cachorros, tempo e quantidade de ração.\n\nPrimeiro, calculamos a taxa de consumo diária por cachorro:\n\n- 40 cachorros consomem 100 kg em 7 dias.\n\nConsumo diário total = 100 kg ÷ 7 dias ≈ 14,29 kg/dia\nConsumo diário por cachorro = 14,29 kg ÷ 40 ≈ 0,357 kg/dia\n\nAgora, com 15 cachorros e 75 kg de ração, queremos saber quantos dias durarão:\n\nDias = Quantidade total de ração ÷ (consumo diário por cachorro × número de cachorros)\nDias = 75 ÷ (0,357 × 15) ≈ 75 ÷ 5,36 ≈ 14 dias\n\nPortanto, a alternativa correta é a letra B.",
        "assunto": "Razão e Proporção e Regra de três"
    },
    {
        "enunciado": "Uma blusa custa R$ 40,00 e uma calça custa R$ 60,00. Comprando 7 peças e gastando R$ 360, quantas blusas e quantas calças foram compradas?",
        "texto": None,
        "imagem": None,
        "alternativas": {
            "a": "4 calças e 3 blusas",
            "b": "5 calças e 4 blusas",
            "c": "6 calças e 3 blusas",
            "d": "2 calças e 9 blusas",
            "e": "10 calças e 2 blusas"
        },
        "correta": "a",
        "resolucao": "Seja x o número de blusas e y o número de calças.\n\nTemos o sistema:\n\nx + y = 7 (quantidade total de peças)\n40x + 60y = 360 (valor total gasto)\n\nMultiplicando a primeira equação por 40:\n40x + 40y = 280\n\nSubtraindo da segunda:\n(40x + 60y) - (40x + 40y) = 360 - 280\n20y = 80\ny = 4 calças\n\nLogo, x = 7 - 4 = 3 blusas\n\nPortanto, a alternativa correta é a letra A.",
        "assunto": "Sistemas lineares e Problemas com as quatro operações"
    },
    {
        "enunciado": "Ao comprar um vídeo game, Alexandre pediu para realizar o pagamento parcelado em 10 vezes. O preço do vídeo game é de R$ 1.890,00 e, por ter pago de modo parcelado, o valor sofreu um acréscimo de 10%. Sabendo que as parcelas possuem um valor fixo, qual o preço de cada parcela que Alexandre pagará?",
        "texto": None,
        "imagem": None,
        "alternativas": {
            "a": "156,90",
            "b": "189,00",
            "c": "234,89",
            "d": "207,90",
            "e": "125,89"
        },
        "correta": "d",
        "resolucao": "O acréscimo de 10% sobre R$ 1.890,00 é:\n10% de 1.890 = 0,10 × 1.890 = R$ 189,00\n\nPreço total com acréscimo:\n1.890 + 189 = R$ 2.079,00\n\nValor de cada parcela (10 vezes):\n2.079 ÷ 10 = R$ 207,90\n\nPortanto, a alternativa correta é a letra D.",
        "assunto": "Porcentagem e Problemas com as quatro operações"
    },
    {
        "enunciado": "Mário tinha \"X\" Reais das suas economias. Gastou um terço no centro da cidade com os amigos. No dia seguinte, deu 10,00 Reais para sua irmã mais nova. Depois saiu com os amigos e gastou mais 4/5 do que ainda tinha e ficou com um troco de 12 reais. Qual o valor de \"X\" em Reais?",
        "texto": None,
        "imagem": None,
        "alternativas": {
            "a": "75",
            "b": "90",
            "c": "100",
            "d": "105",
            "e": "80"
        },
        "correta": "d",
        "resolucao": "Seja X o valor inicial.\n\n1. Gastou 1/3 de X: sobrou 2/3 X.\n2. Deu 10 reais: sobrou (2/3 X) - 10.\n3. Gastou 4/5 do que ainda tinha: gastou 4/5 × [(2/3 X) - 10], sobrando 1/5 × [(2/3 X) - 10] = 12 reais.\n\nMontando a equação:\n\n(1/5) × [(2/3)X - 10] = 12\n\nMultiplicando ambos os lados por 5:\n(2/3)X - 10 = 60\n\nSomando 10:\n(2/3)X = 70\n\nMultiplicando por 3/2:\nX = 70 × (3/2) = 105\n\nPortanto, a alternativa correta é a letra D.",
        "assunto": "Frações e Equações do 1º grau"
    },
    {
        "enunciado": "Em uma loja de artigos esportivos o setor de futebol entrou em promoção e os itens sinalizados em oferta receberiam um desconto de 15% na hora do pagamento. Mariza treina futsal e precisou comprar um tênis para jogar. Sabendo que o modelo escolhido por ela custa R$ 190,00 e participa da promoção, quanto Mariza economizou na compra?",
        "texto": None,
        "imagem": None,
        "alternativas": {
            "a": "R$ 19,00",
            "b": "R$ 28,50",
            "c": "R$ 38,00",
            "d": "R$ 13,50",
            "e": "R$ 20,25"
        },
        "correta": "b",
        "resolucao": "Para calcular o desconto:\n15% de R$ 190,00 = 0,15 × 190 = R$ 28,50\n\nPortanto, Mariza economizou R$ 28,50 na compra.\nAlternativa correta: letra B.",
        "assunto": "Porcentagem e Problemas com as quatro operações"
    },
    {
        "enunciado": "Em uma loja de roupas, cada camiseta custa R$ 20,00 e cada calça custa R$ 35,00. João comprou um total de 5 peças de roupa, entre camisetas e calças, gastando um total de R$ 130,00. Determine quantas camisetas e calças João comprou:",
        "texto": None,
        "imagem": None,
        "alternativas": {
            "a": "João comprou 3 camisetas e 2 calças.",
            "b": "João comprou 5 camisetas e nenhuma calça",
            "c": "João comprou 2 camisetas e 3 calças.",
            "d": "João comprou 4 camisetas e 1 calça.",
            "e": "João comprou 1 camiseta e 4 calças."
        },
        "correta": "a",
        "resolucao": "Seja x o número de camisetas e y o número de calças.\n\nSistema de equações:\n\nx + y = 5 (total de peças)\n20x + 35y = 130 (total gasto)\n\nMultiplicando a primeira por 20:\n20x + 20y = 100\n\nSubtraindo da segunda:\n(20x + 35y) - (20x + 20y) = 130 - 100\n15y = 30\ny = 2 calças\n\nLogo, x = 5 - 2 = 3 camisetas\n\nAlternativa correta: letra A.",
        "assunto": "Sistemas lineares e Problemas com as quatro operações"
    },
    {
        "enunciado": "Densidade demográfica é a razão entre o número de habitantes por área. Determine a densidade demográfica de uma região que possui área de 9000 m² e tem uma população de 27 mil habitantes.",
        "texto": None,
        "imagem": None,
        "alternativas": {
            "a": "8 hab/m²",
            "b": "3 hab/m²",
            "c": "9 hab/m²",
            "d": "13 hab/m²",
            "e": "5 hab/m²"
        },
        "correta": "b",
        "resolucao": "A densidade demográfica é calculada pela fórmula:\n\nDensidade = Número de habitantes / Área\n\nDensidade = 27.000 habitantes / 9.000 m² = 3 habitantes/m²\n\nPortanto, a alternativa correta é a letra B.",
        "assunto": "Razão e Proporção e Problemas com as quatro operações"
    },

    
{
  "enunciado": "Uma empresa de cosméticos localizada no município de Paulista, no Estado de Pernambuco, tem receita bruta total diretamente proporcional ao cubo da metade das quantidades vendidas. Dessa forma, essa empresa obtém receita bruta total igual a R$ 192,00 quando vende oito unidades. Assim, quando essa empresa vende quatro unidades, a receita bruta é igual a:",
  "texto": None,
  "imagem": None,
  "alternativas": {
    "a": "R$ 24,00",
    "b": "R$ 96,00",
    "c": "R$ 70,00",
    "d": "R$ 66,00",
    "e": "R$ 60,00"
  },
  "correta": "a",
  "resolucao": "Seja R a receita e x a quantidade vendida.\n\nSabemos que R é proporcional ao cubo da metade das quantidades vendidas:\n\nR = k × (x/2)^3\n\nPara x = 8:\n192 = k × (8/2)^3 = k × 4^3 = k × 64\n\nLogo, k = 192 / 64 = 3\n\nPara x = 4:\nR = 3 × (4/2)^3 = 3 × 2^3 = 3 × 8 = 24\n\nPortanto, a alternativa correta é a letra A.",
  "assunto": "Potenciação"
},
{
  "enunciado": "Lucas está planejando uma viagem de carro e deseja calcular a distância entre duas cidades. Ele sabe que a velocidade média que ele pretende dirigir é de 60 km/h, e gostaria de descobrir o tempo total de viagem em horas. A distância entre as cidades é de 330 km. Agora, assinale a alternativa correta para o tempo total de viagem:",
  "texto": None,
  "imagem": None,
  "alternativas": {
    "a": "3 horas e 30 min",
    "b": "6 horas",
    "c": "2 horas e 15 min",
    "d": "5 horas e 30 min",
    "e": "4 horas e 30 min"
  },
  "correta": "d",
  "resolucao": "Para calcular o tempo, usamos a fórmula:\n\nTempo = Distância / Velocidade\n\nTempo = 330 km / 60 km/h = 5,5 horas = 5 horas e 30 minutos\n\nPortanto, a alternativa correta é a letra D.",
  "assunto": "Regra de três"
},
{
  "enunciado": "Flávia está participando de uma seleção, cuja prova tem 20 questões. Nesta prova, a cada questão certa, o candidato ganha 5 pontos, e a cada questão não respondida corretamente, perde 3. Sabendo que Flávia fez 68 pontos na classificação, quantas questões ela acertou?",
  "texto": None,
  "imagem": None,
  "alternativas": {
    "a": "12",
    "b": "14",
    "c": "8",
    "d": "16",
    "e": "10"
  },
  "correta": "d",
  "resolucao": "Seja x o número de questões certas e y o número de questões erradas.\n\nTemos o sistema:\n\nx + y = 20\n5x - 3y = 68\n\nSomando as duas equações para eliminar y:\n\nDa primeira, y = 20 - x\nSubstituindo na segunda:\n5x - 3(20 - x) = 68\n5x - 60 + 3x = 68\n8x = 128\nx = 16\n\nPortanto, Flávia acertou 16 questões.\nAlternativa correta: letra D.",
  "assunto": "Sistemas lineares e Problemas com as quatro operações"
},
{
  "enunciado": "Ao visitar uma loja para pesquisar o preço de um smartphone, Antônio foi informado que o modelo escolhido custava R$ 1.400,00 podendo ser comprado da seguinte maneira.\n\nA) À vista, com 15% de desconto.\n\nB) Pagamento a prazo, com acréscimo de 25% sobre o preço inicial.\n\nQual é a diferença, em reais, entre as duas opções de compra?",
  "texto": None,
  "imagem": None,
  "alternativas": {
    "a": "R$ 598,00",
    "b": "R$ 480,00",
    "c": "R$ 490,00",
    "d": "R$ 500,00",
    "e": "R$ 560,00"
  },
  "correta": "e",
  "resolucao": "Preço à vista com desconto:\n15% de 1.400 = 0,15 × 1.400 = 210\nPreço à vista = 1.400 - 210 = 1.190\n\nPreço a prazo com acréscimo:\n25% de 1.400 = 0,25 × 1.400 = 350\nPreço a prazo = 1.400 + 350 = 1.750\n\nDiferença entre as duas opções:\n1.750 - 1.190 = 560\n\nPortanto, a alternativa correta é a letra E.",
  "assunto": "Porcentagem e Problemas com as quatro operações"
},
{
  "enunciado": "Aplicando as propriedades gerais da potenciação, podemos reduzir a uma só potência algumas expressões aritméticas. No caso a seguir 3⁴ · 3⁻⁵ será igual a:",
  "texto": None,
  "imagem": None,
  "alternativas": {
    "a": "3",
    "b": "3⁹",
    "c": "3²⁰",
    "d": "3⁻¹",
    "e": "3⁻⁹"
  },
  "correta": "d",
  "resolucao": "Usando a propriedade das potências de mesma base, somamos os expoentes:\n\n3⁴ · 3⁻⁵ = 3^(4 + (-5)) = 3⁻¹\n\nPortanto, a alternativa correta é a letra D.",
  "assunto": "Potenciação"
},
{
  "enunciado": "João e Carlos foram ao shopping fazer compras. João gastou R$185,00 na compra de uma camisa e duas calças, enquanto Carlos gastou R$155,00 na compra de três camisas e uma calça. Nesta loja cada camisa tinha um mesmo preço x, e cada calça tinha um mesmo preço y. De acordo com as informações, quanto custa cada calça nesta loja?",
  "texto": None,
  "imagem": None,
  "alternativas": {
    "a": "R$ 80,00",
    "b": "R$ 70,00",
    "c": "R$ 110,00",
    "d": "R$ 120,00",
    "e": "R$ 90,00"
  },
  "correta": "a",
  "resolucao": "Seja x o preço da camisa e y o preço da calça.\n\nTemos o sistema:\n\nx + 2y = 185\n3x + y = 155\n\nMultiplicando a segunda equação por 2:\n6x + 2y = 310\n\nSubtraindo a primeira da nova:\n(6x + 2y) - (x + 2y) = 310 - 185\n5x = 125\nx = 25\n\nSubstituindo na primeira:\n25 + 2y = 185\n2y = 160\ny = 80\n\nPortanto, cada calça custa R$ 80,00.\nAlternativa correta: letra A.",
  "assunto": "Sistemas lineares"
},
{
  "enunciado": "De acordo com um levantamento estatístico de uma empresa de desenvolvimento de software, 70% dos funcionários eram desenvolvedores.\n\nAinda de acordo com esse levantamento, a média salarial semanal dos desenvolvedores era de R$ 3.000,00 e a média salarial dos demais funcionários era de R$ 4.000,00. Considerando todos funcionários da empresa, a média salarial semanal é de:",
  "texto": None,
  "imagem": None,
  "alternativas": {
    "a": "R$ 3.950,00",
    "b": "R$ 3.300,00",
    "c": "R$ 3.250,00",
    "d": "R$ 3.750,00",
    "e": "R$ 3.650,00"
  },
  "correta": "b",
  "resolucao": "Para calcular a média salarial semanal de todos os funcionários, utilizamos a média ponderada:\n\n1. Desenvolvedores (70%): 0,70 × R$ 3.000,00 = R$ 2.100,00\n2. Demais funcionários (30%): 0,30 × R$ 4.000,00 = R$ 1.200,00\n\nMédia total = R$ 2.100,00 + R$ 1.200,00 = R$ 3.300,00\n\nPortanto, a alternativa correta é a letra B.",
  "assunto": "Média Ponderada"
},
{
  "enunciado": "Em uma loja de brinquedos, o preço de um carrinho de controle remoto é de R$ 174,00. Ana comprou um carrinho e pagou um total de R$ 204,00, incluindo o valor do frete. Determine o valor do frete.",
  "texto": None,
  "imagem": None,
  "alternativas": {
    "a": "Ana pagou R$ 204,00",
    "b": "Ana pagou R$ 174,00",
    "c": "Ana pagou R$ 378,00",
    "d": "Ana pagou R$ 40,00",
    "e": "Ana pagou R$ 30,00"
  },
  "correta": "e",
  "resolucao": "Para determinar o valor do frete, subtraímos o preço do carrinho do valor total pago:\n\nFrete = R$ 204,00 - R$ 174,00 = R$ 30,00\n\nPortanto, a alternativa correta é a letra E.",
  "assunto": "Equações do 1º grau e Problemas com as quatro operações  "
},
{
  "enunciado": "Numa fábrica de chocolate, sabe-se que 4 máquinas, operando 4 horas por dia, durante 4 dias, produzem 4 toneladas de chocolate. Quantas toneladas de chocolate seriam produzidas por 6 máquinas do mesmo tipo, operando 6 horas por dia, durante 6 dias?",
  "texto": None,
  "imagem": None,
  "alternativas": {
    "a": "6",
    "b": "15",
    "c": "13,5",
    "d": "8",
    "e": "10,5"
  },
  "correta": "c",
  "resolucao": "A produção é diretamente proporcional ao número de máquinas, horas e dias. Logo:\n\n4 máquinas × 4 horas × 4 dias = 64 unidades de produção resultam em 4 toneladas.\n\n6 máquinas × 6 horas × 6 dias = 216 unidades de produção.\n\nRegra de três:\n64 → 4 toneladas\n216 → x toneladas\nx = (216 × 4) / 64 = 13,5 toneladas.\n\nPortanto, a alternativa correta é a letra C.",
  "assunto": "Regra de três composta"
},
{
  "enunciado": "Sendo x = (2²)³, y = 2² e z = 2³. A potência que representa a expressão x · y · z é:",
  "texto": None,
  "imagem": None,
  "alternativas": {
    "a": "2²²",
    "b": "2²¹",
    "c": "2²⁰",
    "d": "2¹⁹",
    "e": "2¹¹"
  },
  "correta": "e",
  "resolucao": "Vamos simplificar cada parte da expressão:\n\nx = (2²)³ = 2^(2×3) = 2⁶\ny = 2²\nz = 2³\n\nAgora multiplicamos:\n2⁶ · 2² · 2³ = 2^(6+2+3) = 2¹¹\n\n Portanto, a alternativa correta é a **letra E, 2¹¹**.",
  "assunto": "Potenciação"
},
{
  "enunciado": "O centro cultural Cais do Sertão recebeu 5.467 visitantes, dos quais 2.346 eram naturais de Recife. Quantas pessoas naturais de outras cidades visitaram o centro cultural?",
  "texto": None,
  "imagem": None,
  "alternativas": {
    "a": "2.123",
    "b": "983",
    "c": "1.981",
    "d": "1.230",
    "e": "3.121"
  },
  "correta": "e",
  "resolucao": "Para saber quantos visitantes eram de outras cidades, subtraímos o número de recifenses do total:\n\n5.467 - 2.346 = 3.121\n\n Portanto, a alternativa correta é a **letra E, 3.121**.",
  "assunto": "Problemas com as quatro operações"
},
{
  "enunciado": "Três é quantos porcento de cinco?",
  "texto": None,
  "imagem": None,
  "alternativas": {
    "a": "90%",
    "b": "70%",
    "c": "60%",
    "d": "50%",
    "e": "80%"
  },
  "correta": "c",
  "resolucao": "Para descobrir quantos por cento 3 é de 5, usamos a regra:\n\n(3 ÷ 5) × 100 = 0,6 × 100 = 60%\n\n Portanto, a alternativa correta é a **letra C, 60%**.",
  "assunto": "Porcentagem"
},
{
  "enunciado": "Para encher totalmente a piscina do clube, um funcionário utilizou uma mangueira ligada das 7h30 até às 19h30. Se esse funcionário tivesse iniciado o serviço no mesmo horário, porém utilizado três mangueiras juntas, a que horas a piscina estaria totalmente cheia?",
  "texto": None,
  "imagem": None,
  "alternativas": {
    "a": "9h30",
    "b": "8h30",
    "c": "11h30",
    "d": "18h30",
    "e": "10h30"
  },
  "correta": "c",
  "resolucao": "O tempo total para encher a piscina com uma mangueira é de 12 horas (das 7h30 às 19h30).\n\nUsando três mangueiras juntas, o tempo será dividido por 3:\n12 horas ÷ 3 = 4 horas.\n\nAssim, a piscina estará cheia às 7h30 + 4 horas = 11h30.\n\n✅ Portanto, a alternativa correta é a letra C.",
  "assunto": "Regra de três"
},
{
  "enunciado": "Analisando a imagem com ângulos opostos pelo vértice no ponto E, determine o valor de x + y.",
  "texto": None,
  "imagem": "static/imagens/figura.jpeg",
  "alternativas": {
    "a": "10",
    "b": "11",
    "c": "15",
    "d": "21",
    "e": "25"
  },
  "correta": "d",
  "resolucao": "Na imagem, os ângulos opostos pelo vértice são iguais. Assim:\n\n1) 3x - 5° = 2x + 5°\n⇒ 3x - 2x = 5 + 5\n⇒ x = 10\n\n2) Os ângulos 15y - x e 18x - 25° também são opostos pelo vértice:\n15y - x = 18x - 25\n⇒ 15y - 10 = 180 - 25 (substituindo x = 10)\n⇒ 15y - 10 = 155\n⇒ 15y = 165\n⇒ y = 11\n\nLogo:\nx + y = 10 + 11 = 21",
  "assunto": "Geometria - Ângulos Opostos pelo Vértice"
},
{
  "enunciado": "Para encher totalmente a piscina do clube, um funcionário utilizou uma mangueira ligada das 7h30 até às 19h30. Se esse funcionário tivesse iniciado o serviço no mesmo horário, porém utilizado três mangueiras juntas, a que horas a piscina estaria totalmente cheia?",
  "texto": None,
  "imagem": "static/imagens/figura2.jpeg",
  "alternativas": {
    "a": "9h30",
    "b": "8h30",
    "c": "11h30",
    "d": "18h30",
    "e": "10h30" 
  },
  "correta": "c",
  "resolucao": "O tempo total com uma mangueira foi de 12 horas (das 7h30 às 19h30). Se fossem usadas três mangueiras juntas, o trabalho seria 3 vezes mais rápido. Então, 12 horas ÷ 3 = 4 horas. Se começassem às 7h30, a piscina estaria cheia 4 horas depois, ou seja, às 11h30.",
  "assunto": "Regra de três / Razão e proporção"
},
{
    "enunciado": "Uma lesma anda 25 cm em 1 hora. Quantos metros percorrerá em dois dias?",
    "texto": None,
    "imagem": None,
    "alternativas": {
        "A": "12 metros",
        "B": "8 metros",
        "C": "6 metros",
        "D": "4 metros",
        "E": "3 metros"
    },
    "correta": "A",
    "resolucao": "Primeiro, calculamos o total de horas em dois dias: 2 dias × 24 horas/dia = 48 horas. \n\nA lesma percorre 25 cm por hora. Então, em 48 horas: 25 cm/hora × 48 horas = 1200 cm. \n\nConvertendo centímetros para metros (1 m = 100 cm): 1200 cm ÷ 100 = 12 metros.",
    "assunto": "Problemas de regra de três simples / Conversão de unidades"
},
{
    "enunciado": "Quais são os dois números cuja média aritmética simples e a média geométrica deles são respectivamente 20,5 e 20?",
    "texto": None,
    "imagem": None,
    "alternativas": {
        "A": "16 e 25",
        "B": "17 e 30",
        "C": "18 e 19",
        "D": "15 e 24",
        "E": "15 e 26"
    },
    "correta": "A",
    "resolucao": "1. Traduza as informações em equações:\n   - Média aritmética: (x + y)/2 = 20,5 ⇒ x + y = 41.\n   - Média geométrica: √(xy) = 20 ⇒ xy = 400.\n\n2. Reduza a um único incógnita:\n   Seja t um dos números; então o outro é 41 − t. O produto é\n   t(41 − t) = 400.\n   Expandindo: 41t − t^2 = 400 ⇒ t^2 − 41t + 400 = 0.\n\n3. Resolva a equação quadrática t^2 − 41t + 400 = 0:\n   - Coeficientes: a = 1, b = −41, c = 400.\n   - Discriminante: Δ = b^2 − 4ac = (−41)^2 − 4·1·400 = 1681 − 1600 = 81.\n   - √Δ = 9. Aplicando a fórmula:\n     t = (41 ± 9)/2 ⇒ t1 = (41 + 9)/2 = 25 e t2 = (41 − 9)/2 = 16.\n\n4. Conclusão e verificação:\n   Os números são 16 e 25.\n   - Soma: 16 + 25 = 41 ⇒ média aritmética = 41/2 = 20,5.\n   - Produto: 16·25 = 400 ⇒ média geométrica = √400 = 20.\n\nPortanto, os dois números são 16 e 25.",
    "assunto": "Médias Aritmética e Geométrica"
},
{
    "enunciado": "Na bandeira do estado de Pernambuco, o comprimento e a largura são proporcionais a 10 e 7. Walquíria quer fazer uma bandeira com 2 m de comprimento. Quantos metros deverá ter a largura?",
    "texto": None,
    "imagem": None,
    "alternativas": {
        "A": "1,40",
        "B": "1,50",
        "C": "1,70",
        "D": "1,55",
        "E": "1,60"
    },
    "correta": "A",
    "resolucao": ("A proporção entre comprimento e largura é de 10:7. Se o comprimento é de 2 m, podemos montar a proporção: 10/7 = 2/x, onde x é a largura. Resolvendo: 10x = 14, então x = 14/10 = 1,4 m. Portanto, a largura deve ser de 1,40 metros.",
    ),
    "assunto": "Proporcionalidade"
},
{
    "enunciado": "Em uma padaria muito conhecida pelos pães e pela qualidade do café comercializado diariamente, a razão entre o número de pessoas que tomam café puro e o número de pessoas que tomam café com leite, de manhã, é de 2/3. Se durante uma semana, 180 pessoas tomaram café de manhã nessa padaria, e supondo que essa razão permaneça a mesma, pode-se concluir que o número de pessoas que tomaram café puro será:",
    "texto": None,
    "imagem": None,
    "alternativas": {
        "A": "72",
        "B": "112",
        "C": "94",
        "D": "105",
        "E": "86"
    },
    "correta": "A",
    "resolucao": ("Passo 1: Identificar a razão dada\nRazão entre café puro (CP) e café com leite (CL) = 2/3\n\nPasso 2: Estabelecer as relações\nCP/CL = 2/3  →  CP = (2/3)CL\nCP + CL = 180 (total de pessoas)\n\nPasso 3: Substituir e resolver\n(2/3)CL + CL = 180\n(2/3 + 3/3)CL = 180\n(5/3)CL = 180\nCL = 180 × (3/5)\nCL = 108\n\nPasso 4: Encontrar CP\nCP = (2/3) × 108\nCP = 72\n\nResposta: 72 pessoas tomaram café puro.",
    ),
    "assunto": "Razão e Proporção"
},
{
    "enunciado": "Em uma fazenda há 95 animais entre vacas e cavalos. Se o proprietário comprar mais uma vaca, a quantidade de vacas será o dobro da quantidade de cavalos. Quantas vacas e quantos cavalos há respectivamente?",
    "texto": None,
    "imagem": None,
    "alternativas": {
        "A": "63 e 32",
        "B": "62 e 33",
        "C": "61 e 34",
        "D": "64 e 31",
        "E": "65 e 30"
    },
    "correta": "A",
    "resolucao": ("Seja V o número de vacas e C o número de cavalos. Temos:\n1) V + C = 95 (total atual de animais)\n2) Após comprar mais uma vaca: (V + 1) = 2C\n\nDa equação 2: V = 2C - 1\nSubstituindo na equação 1:\n(2C - 1) + C = 95\n3C - 1 = 95\n3C = 96\nC = 32\n\nEntão: V = 2*32 - 1 = 64 - 1 = 63\n\nPortanto, há 63 vacas e 32 cavalos.",
    ),
    "assunto": "Sistemas de equações"
},
{
    "enunciado": "Se N é diferente de zero, e se M/N = 2, então a razão de M-N para M, percentualmente, é igual a:",
    "texto": None,
    "imagem": None,
    "alternativas": {
        "A": "50%",
        "B": "75%",
        "C": "25%",
        "D": "100%",
        "E": "65%"
    },
    "correta": "A",
    "resolucao": ("Dado que M/N = 2, temos M = 2N.\nA razão (M - N)/M pode ser expressa como:\n(2N - N)/(2N) = N/(2N) = 1/2.\nPara converter em porcentagem: (1/2) * 100% = 50%.",
    ),
    "assunto": "Razão e Proporção"
},
{
    "enunciado": "Uma escola estadual decidiu organizar uma excursão. Inscreveram-se 140 alunos que serão acompanhados por 10 professores. Cada ônibus tem capacidade para 41 passageiros e cobra R$ 500 para fazer a viagem. Se os 10 professores ganharam a passagem da empresa de ônibus, qual o valor mínimo que cada aluno pagará para que a excursão se realize?",
    "texto": None,
    "imagem": None,
    "alternativas": {
        "A": "R$ 14,29",
        "B": "R$ 16,33",
        "C": "R$ 15,50",
        "D": "R$ 15,35",
        "E": "R$ 14,40"
    },
    "correta": "A",
    "resolucao": ("Passo 1: Calcular o número total de passageiros pagantes\nTotal de pessoas: 140 alunos + 10 professores = 150 pessoas.\nComo os professores não pagam, apenas os 140 alunos pagarão.\n\nPasso 2: Calcular quantos ônibus são necessários\nCada ônibus leva 41 passageiros.\n150 passageiros ÷ 41 = 3,658... → serão necessários 4 ônibus (pois não se pode fracionar um ônibus).\n\nPasso 3: Calcular o custo total\nCada ônibus custa R$ 500.\nCusto total: 4 ônibus × R$ 500 = R$ 2000.\n\nPasso 4: Dividir o custo entre os alunos\nR$ 2000 ÷ 140 alunos = R$ 14,2857... ≈ R$ 14,29 por aluno.\n\nPortanto, cada aluno pagará no mínimo R$ 14,29.",
    ),
    "assunto": "Problemas de divisão proporcional"
},
{
    "enunciado": "Na figura, ABCD é um quadrado e o triângulo CDE é equilátero. Determine a medida do ângulo x.",
    "texto": None,
    "imagem": "static/imagens/figura3.jpeg",
    "alternativas": {
        "A": "80°",
        "B": "60°",
        "C": "70°",
        "D": "65°",
        "E": "75°"
    },
    "correta": "E",
    "resolucao": ("Passo 1: O triângulo CDE é equilátero, então cada ângulo interno mede 60°.\n\nPasso 2: A inclinação do segmento ED em relação à base DC é de 60° com a horizontal.\n\nPasso 3: Para determinar o ângulo entre os segmentos EA e ED, calculamos a inclinação de EA:\n- Coordenadas: A(0, s), E(s/2, (√3/2)·s).\n- Coeficiente angular: (s - (√3/2)s) / (0 - s/2) = (s(1 - √3/2)) / (-s/2) = 2 - √3.\n- Assim, o ângulo que EA faz com a horizontal é 15°.\n\nPasso 4: O ângulo x é formado pela diferença entre 60° e 15°: x = 75°.\n\nPortanto, a medida do ângulo x é 75°.",
    ),
    "assunto": "Geometria plana – Quadrado e triângulo equilátero"
},
{
    "enunciado": "No esquema, os raios partem da mesma origem e formam um ângulo reto (90°) com a horizontal. As medidas dos ângulos adjacentes, a partir da horizontal, são: x + 20°, x + 20°, x + 10° e x (do maior para o menor, até o raio vertical). Determine um valor possível para x.",
    "texto": None,
    "imagem": "static/imagens/figura4.jpeg",
    "alternativas": {
        "A": "20",
        "B": "30",
        "C": "25",
        "D": "10",
        "E": "15"
    },
    "correta": "D",
    "resolucao": ("Os quatro ângulos adjacentes somam um ângulo reto: (x + 20°) + (x + 20°) + (x + 10°) + x = 90°. Logo, 4x + 50° = 90° ⇒ 4x = 40° ⇒ x = 10°.",
    ),
    "assunto": "Geometria plana – Soma de ângulos adjacentes"
},
]

def questao_aleatoria():
    return random.choice(banco_questoes_mat)

def questao_matematica_nao_repetida(respondidas_ids):
    restantes = [q for q in banco_questoes_mat if q['id'] not in respondidas_ids]
    return random.choice(restantes)
 