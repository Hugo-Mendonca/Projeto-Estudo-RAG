## Relatório Final do Projeto Mineração de Dados Aplicada com CRISP-DM

Grupo:

## Resumo

O dataset Covertype, composto por sete classes de cobertura florestal, apresenta desafios significativos devido ao desbalanceamento severo das amostras. Este projeto propõe o desenvolvimento de modelos de aprendizado de máquina para a classificação automatizada desses tipos de cobertura, visando otimizar estratégias de preservação ambiental e planejamento turístico. Para mitigar o viés das classes majoritárias, a métrica F1-Score (Macro) foi adotada como critério principal de avaliação. Foram avaliadas diversas arquiteturas, comparando estratégias de balanceamento (Baseline, pipelines de reamostragem e pesos balanceados). O modelo LightGBM, configurado com o Pipeline 3, obteve o desempenho mais expressivo, alcançando 99% de F1Score no treinamento, 91% na validação e 93% no conjunto de teste. Estes resultados confirmam a alta capacidade discriminativa do modelo e sua robustez na generalização de padrões complexos.

## Sumário

| Fase 1: Business Understanding . . . . . . .                         | Fase 1: Business Understanding . . . . . . .                         |
|----------------------------------------------------------------------|----------------------------------------------------------------------|
| 0.1 Cliente e contexto . . .                                         | . . . . . . 3                                                        |
| 0.2 Problema de negócio . . . . . . . . .                            | . . . . . . 3                                                        |
| 0.3 Critério de Sucesso . . . . . . . .                              | . . . . . . 4                                                        |
| 0.4 Risco e impacto ético . . . . . . . .                            | . . . . . . 5                                                        |
| Fase 2: Data Understanding 5 . . . . . . . . . . . . . . . . . . . . | Fase 2: Data Understanding 5 . . . . . . . . . . . . . . . . . . . . |
| 0.5 Dataset escolhido                                                | . . . . . . 5 . . . . . .                                            |
| 0.6 Análise exploratória . . . . . . . .                             | 6                                                                    |
| 0.7 Implicações para a modelagem . . .                               | . . . . . . 8                                                        |
| Fase 3: Data Preparation . . . . . . . . . . .                       | Fase 3: Data Preparation . . . . . . . . . . .                       |
| 0.8 Partição treino, validação e teste .                             | . . . . . 9                                                          |

Hugo Mendonça, Danilo Regino Barrote, Bernardo

Siqueira Batista

Cliente:

US Forest Service (USFS)

IF1014 - 2026.1

| 0.9 Pipeline baseline . .                                                                                                                           | 0.9 Pipeline baseline . .                                                                                                                           | 0.9 Pipeline baseline . .                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 0.10 Variantes do conjunto de treino . . . . . . . . . . . . . . . . . 10                                                                           | 0.10 Variantes do conjunto de treino . . . . . . . . . . . . . . . . . 10                                                                           | 0.10 Variantes do conjunto de treino . . . . . . . . . . . . . . . . . 10                                                                           |
| Fase 4: Modeling 11 0.11 Espaços de busca utilizados . . . . . . . . . . . . . . . . . . . . 11                                                     | Fase 4: Modeling 11 0.11 Espaços de busca utilizados . . . . . . . . . . . . . . . . . . . . 11                                                     | Fase 4: Modeling 11 0.11 Espaços de busca utilizados . . . . . . . . . . . . . . . . . . . . 11                                                     |
| 0.12 Resultados por algoritmo . . . . . . . . . . . . . . . . . . . . . 12                                                                          | 0.12 Resultados por algoritmo . . . . . . . . . . . . . . . . . . . . . 12                                                                          | 0.12 Resultados por algoritmo . . . . . . . . . . . . . . . . . . . . . 12                                                                          |
| 0.0.1                                                                                                                                               | Análise do Algoritmo K-Nearest Neighbors(KNN) . . .                                                                                                 | 12                                                                                                                                                  |
| 0.0.2                                                                                                                                               | Análise do Algoritmo: Learning Vector Quantization (LVQ . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                     | 13                                                                                                                                                  |
| 0.0.3                                                                                                                                               | Análise do Algoritmo: Support Vector Machine (SVM)                                                                                                  | 14                                                                                                                                                  |
| 0.0.4                                                                                                                                               | Análise do Algoritmo: Decision Tree . . . . . . . . . .                                                                                             | 15                                                                                                                                                  |
| 0.0.5                                                                                                                                               | Análise do Algoritmo: Random Forest . . . . . . .                                                                                                   | 16                                                                                                                                                  |
| 0.0.6                                                                                                                                               | . . Análise do Algoritmo: Multi-Layer Perceptron (MLP) .                                                                                            | 17                                                                                                                                                  |
| 0.0.7                                                                                                                                               | Análise do Algoritmo: Bagging MLP . . . . . . . . . . . . .                                                                                         | 18                                                                                                                                                  |
| 0.0.8                                                                                                                                               | Análise do Algoritmo: XGBoost . . . . . . . . . .                                                                                                   | 19                                                                                                                                                  |
| 0.0.9                                                                                                                                               | Análise do Algoritmo: LightGBM . . . . . . . . . . .                                                                                                | 20                                                                                                                                                  |
| 0.0.10                                                                                                                                              | . Análise do Algoritmo: Stacking Heterogêneo . . . . . .                                                                                            | 21                                                                                                                                                  |
| 0.0.11                                                                                                                                              | Conclusão da Fase de Avaliação . . . . . . . . . . . . .                                                                                            | 22                                                                                                                                                  |
| Fase 5: Evaluation 23                                                                                                                               | Fase 5: Evaluation 23                                                                                                                               | Fase 5: Evaluation 23                                                                                                                               |
| 0.13 Baseline consolidado . . . . . . . . . . . . . . . . . . . . . . . . 23                                                                        | 0.13 Baseline consolidado . . . . . . . . . . . . . . . . . . . . . . . . 23                                                                        | 0.13 Baseline consolidado . . . . . . . . . . . . . . . . . . . . . . . . 23                                                                        |
| 0.14 Comparação baseline vs variantes . . . . . . . . . . . . . . . . 23                                                                            | 0.14 Comparação baseline vs variantes . . . . . . . . . . . . . . . . 23                                                                            | 0.14 Comparação baseline vs variantes . . . . . . . . . . . . . . . . 23                                                                            |
| 0.15 Seleção do melhor modelo . . . . . . . . . . . . . . . . . . . . . 25                                                                          | 0.15 Seleção do melhor modelo . . . . . . . . . . . . . . . . . . . . . 25                                                                          | 0.15 Seleção do melhor modelo . . . . . . . . . . . . . . . . . . . . . 25                                                                          |
| 0.16 Avaliação final no conjunto de teste . . . . . . . . . . . . . . . 26 6: Deployment 27                                                         | 0.16 Avaliação final no conjunto de teste . . . . . . . . . . . . . . . 26 6: Deployment 27                                                         | 0.16 Avaliação final no conjunto de teste . . . . . . . . . . . . . . . 26 6: Deployment 27                                                         |
| Fase                                                                                                                                                | Fase                                                                                                                                                | Fase                                                                                                                                                |
| 0.17 Como o modelo seria utilizado . . . . . . . . . . . . . . . . . . 27                                                                           | 0.17 Como o modelo seria utilizado . . . . . . . . . . . . . . . . . . 27                                                                           | 0.17 Como o modelo seria utilizado . . . . . . . . . . . . . . . . . . 27                                                                           |
| 0.18 Riscos e mitigações . . . . . . . . . . . . . . . . . . . . . . . . 28 0.19 Monitoramento e retreinamento . . . . . . . . . . . . . . . . . 28 | 0.18 Riscos e mitigações . . . . . . . . . . . . . . . . . . . . . . . . 28 0.19 Monitoramento e retreinamento . . . . . . . . . . . . . . . . . 28 | 0.18 Riscos e mitigações . . . . . . . . . . . . . . . . . . . . . . . . 28 0.19 Monitoramento e retreinamento . . . . . . . . . . . . . . . . . 28 |
| 1 Conclusão e trabalhos futuros 29                                                                                                                  | 1 Conclusão e trabalhos futuros 29                                                                                                                  | 1 Conclusão e trabalhos futuros 29                                                                                                                  |
| 2 Reprodutibilidade e ferramentas 29                                                                                                                | 2 Reprodutibilidade e ferramentas 29                                                                                                                | 2 Reprodutibilidade e ferramentas 29                                                                                                                |
| 0.1 Ambiente Computacional . . . . . . . . . . . . . . . . . . . . . 29                                                                             | 0.1 Ambiente Computacional . . . . . . . . . . . . . . . . . . . . . 29                                                                             | 0.1 Ambiente Computacional . . . . . . . . . . . . . . . . . . . . . 29                                                                             |
| 0.2 Tecnologias e Dependências . . . . . . . . . . . . . . . . . . . 30 Referências 30                                                              | 0.2 Tecnologias e Dependências . . . . . . . . . . . . . . . . . . . 30 Referências 30                                                              | 0.2 Tecnologias e Dependências . . . . . . . . . . . . . . . . . . . 30 Referências 30                                                              |

## Fase 1: Business Understanding

## 0.1 Cliente e contexto

A gestão sustentável de ecossistemas florestais de grande escala representa um dos maiores desafios contemporâneos para a preservação da biodiversidade global. Neste cenário, o US Forest Service (USFS), órgão vinculado ao Departamento de Agricultura dos Estados Unidos, desempenha um papel fundamental na administração de milhões de hectares de terras federais, onde a identificação precisa da tipologia florestal - a "cobertura vegetal"(Covertype) - é o pilar que sustenta ações estratégicas que variam desde o combate a incêndios e o manejo de pragas até a delimitação de zonas de conservação estrita. Atualmente, o monitoramento tradicional desses recursos depende amplamente de inventários de campo, um processo intrinsecamente custoso, moroso e limitado em sua capacidade de escala territorial.

Para endereçar essa falha, o presente trabalho propõe o desenvolvimento de um sistema de classificação automatizado baseado em uma arquitetura de Stacking Heterogêneo. Através de um pipeline que integra técnicas avançadas de balanceamento de classes e refinamento iterativo de hiperparâmetros, consolidamos a inteligência de diversos modelos, como LightGBM, XGBoost e Random Forest, sob a regência de um meta-aprendiz. Essa abordagem garante ao USFS uma ferramenta de suporte à decisão com alta sensibilidade para todas as tipologias florestais, transformando dados brutos em inteligência estratégica capaz de promover uma preservação mais eficiente e baseada em evidências.

A automação dessa análise, por meio da integração de dados geoespaciais e técnicas de aprendizado de máquina, surge como a alternativa mais viável para otimizar o monitoramento. Contudo, essa transição tecnológica enfrenta um obstáculo estatístico crítico: o desbalanceamento severo das classes. O dataset Covertype, que reflete a distribuição real de tipologias em áreas de alta altitude, é dominado por classes majoritárias, enquanto tipos de vegetação ecologicamente sensíveis - como certas espécies de coníferas ameaçadas pelas mudanças climáticas - figuram como classes minoritárias raras. Quando um modelo preditivo é treinado sem o devido rigor estatístico, ele tende a ignorar tais classes em prol da maximização da acurácia global, falhando justamente na proteção dos ecossistemas mais frágeis.

## 0.2 Problema de negócio

O problema de negócio central deste projeto reside na ineficiência operacional do US Forest Service (USFS) ao realizar inventários florestais em áreas vastas e de difícil acesso. O monitoramento manual é um processo moroso e dispendioso, que frequentemente deixa lacunas críticas na gestão ambiental. Mais grave ainda é o viés estatístico presente nos dados: como a maioria das tipologias florestais é composta por classes majoritárias, modelos de monitoramento convencionais tendem a ignorar as espécies mais raras e ecologicamente sensíveis, falhando justamente na proteção dos ecossistemas sob maior ameaça.

Para o USFS, essa imprecisão não é apenas um erro técnico, mas um risco estratégico, pois direciona recursos de conservação para áreas que não necessitam de intervenção urgente, negligenciando pontos críticos de biodiversidade. Portanto, o desafio de negócio consiste em superar o desbalanceamento dos dados, utilizando modelos de aprendizado de máquina para transformar variáveis geoespaciais em um mapa dinâmico de prioridades. Essa solução permite ao órgão alocar verbas e equipes de campo de forma prescritiva, garantindo que as decisões de preservação florestal sejam baseadas em evidências estatísticas robustas, capazes de identificar e proteger ecossistemas frágeis antes que a degradação se torne irreversível, além de otimizar a alocação de mão de obra e mitigar riscos ocupacionais ao reduzir a necessidade de inspeções presenciais em áreas remotas e inóspitas.

## 0.3 Critério de Sucesso

O sucesso deste projeto não é medido apenas pela performance algorítmica, mas pelo impacto direto na eficácia das operações de conservação florestal. O critério de sucesso está dividido em duas frentes complementares:

- 1. Critério Técnico (Performance do Modelo): O objetivo técnico é atingir um F1-Score Macro igual ou superior a 0.85 no conjunto de teste. A escolha desta métrica é mandatória pois, ao contrário da acurácia simples, o F1-Score penaliza severamente o modelo que ignora classes minoritárias. Portanto, um valor elevado neste indicador garante que o modelo possui alta sensibilidade para detectar todas as tipologias florestais, incluindo as espécies raras e ecologicamente sensíveis que são o foco da preservação.
- 2. Critério de Negócio (Impacto Operacional): Do ponto de vista es-

de levantamentos de campo em áreas onde a classificação do modelo apresenta alta confiança, permitindo que a mão de obra especializada

- tratégico, o sucesso é validado pela capacidade do modelo em: Redução da Incerteza: Diminuir em pelo menos 30% a necessidade

seja realocada para áreas de classificação incerta ou zonas de maior risco de degradação.

Sensibilidade Prescritiva: Garantir que 100% das classes minoritárias sejam corretamente identificadas em mais de 80% das instâncias, assegurando que o USFS não perca a visibilidade sobre nenhum ecossistema frágil.

Confiabilidade de Decisão: Fornecer ao órgão uma ferramenta que atue como suporte à decisão, validada por uma matriz de confusão que demonstre baixa taxa de erro de classificação entre tipologias distintas, evitando custos desnecessários com o envio de equipes para áreas que foram classificadas erroneamente.

## 0.4 Risco e impacto ético

A implementação desta solução introduz riscos técnicos e implicações éticas que devem ser gerenciados com rigor. Primeiramente, a magnitude do dataset Covertype impõe desafios significativos de custo computacional; a necessidade de elevado processamento para o treinamento de modelos robustos pode limitar a escalabilidade e a frequência de atualizações do sistema, caso não haja uma infraestrutura otimizada.

Do ponto de vista ético, o maior risco reside na propagação de vieses estatísticos inerentes ao desbalanceamento das classes. Caso o modelo privilegie excessivamente as tipologias majoritárias, ele pode classificar erroneamente ecossistemas raros - frequentemente aqueles com maior valor de biodiversidade ou sob maior risco de degradação. Essa falha de predição, se utilizada como base para políticas públicas do USFS, poderia resultar em uma alocação inadequada de verbas e pessoal, negligenciando áreas que demandam atenção urgente. Portanto, a ética no projeto impõe a transparência sobre as limitações do modelo e a adoção de métricas de avaliação, como o F1-Score, que garantam a equidade na identificação de todas as classes, mitigando o risco de omissões prejudiciais ao patrimônio ambiental.

## Fase 2: Data Understanding

## 0.5 Dataset escolhido

O dataset Covertype é uma base de dados clássica de sensoriamento remoto, amplamente utilizada em problemas de classificação multiclase. Ele descreve a cobertura florestal de quatro áreas de estudo na Floresta Nacional de Roosevelt, no Colorado (EUA), com o objetivo de prever o tipo de vegetação a partir de variáveis cartográficas.

## Características técnicas:

- Volume: 581.012 instâncias.

- Dimensionalidade: 54 colunas (features).

- Target: Variável Cover\_Type com 7 classes distintas.

## Composição das variáveis:

- Quantitativas (10): Incluem elevação, aspecto, declividade, distância hidrológica, distância para estradas e radiação solar.
- Binárias (44): Representam dados categóricos transformados via OneHot Encoding , sendo 4 para Wilderness Area e 40 para a classificação do tipo de solo.

Tipologias Florestais (Classes): Omodelo atua sobre 7 classes: Spruce/Fir , Lodgepole Pine , Ponderosa Pine , Cottonwood/Willow , Aspen , Douglas-fir e Krummholz . Odesafio técnico central reside no desbalanceamento severo : enquanto Lodgepole Pine domina a amostragem com centenas de milhares de registros, classes como Cottonwood/Willow são minoritárias e raras, exigindo técnicas de modelagem robustas para evitar o viés em favor das classes majoritárias.

## 0.6 Análise exploratória

A análise exploratória confirmou a alta integridade estrutural do dataset , que se encontra totalmente preenchido, eliminando a necessidade de técnicas de imputação e mitigando o risco de introduzir ruídos artificiais nos dados.

Identificamos um desbalanceamento severo na distribuição das classes, conforme mostra a Figura 1 . Este cenário valida nossa escolha pelo F1-Score Macro , visto que a acurácia global seria enviesada pelas classes majoritárias (1 e 2), negligenciando tipologias raras.

Figura 1: Distribuição das classes: o desbalanceamento motiva a métrica de avaliação.

<!-- image -->

Por fim, a análise da variável Elevation ( Figura 2 ) revela outliers que, embora presentes, são inerentes à heterogeneidade dos tipos de solo e condições ambientais de cada região. Optamos por mantê-los para preservar a variância real do fenômeno e a fidelidade ao ambiente mapeado.

## Altura por tipo florestal

Figura 2: Distribuição de altitude por cobertura florestal: presença de outliers naturais devido à heterogeneidade dos solos.

<!-- image -->

## 0.7 Implicações para a modelagem

Os achados da análise exploratória impõem diretrizes estritas para a arquitetura de modelagem, visando garantir robustez e equidade nas predições:

- Necessidade de Algoritmos Sensíveis à Escala: Como identificamos a necessidade de utilizar o StandardScaler para normalizar o intervalo das variáveis numéricas, o modelo escolhido deve ser compatível com dados escalonados. Algoritmos baseados em gradiente ou distâncias serão priorizados pela sua capacidade de extrair padrões de dados normalizados de forma eficiente.
- Abordagem Robusta ao Desbalanceamento: A disparidade volumétrica entre as classes minoritárias e majoritárias inviabiliza o uso de modelos simplistas. Implica-se, portanto, a obrigatoriedade de integrar ao pipeline de modelagem técnicas como class weights ou algoritmos de ensemble , que possuem mecanismos nativos de tratamento de distribuições assimétricas.
- Seleção de Métricas Orientada ao Negócio: Dado que a acurácia é uma métrica enviesada para este conjunto de dados, todas as etapas de busca de hiperparâmetros serão guiadas estritamente pelo F1-Score

Macro . Isso garante que o processo de otimização priorize o equilíbrio de sensibilidade entre todas as tipologias florestais, incluindo as raras.

- Validação Cruzada Estratificada: Adotaremos a Stratified K-Fold Cross-Validation para assegurar que cada subconjunto de treino e teste mantenha a proporção real de todas as 7 classes, garantindo que o modelo seja validado de forma estatisticamente justa mesmo para as classes com poucos representantes.

## Fase 3: Data Preparation

## 0.8 Partição treino, validação e teste

Para garantir a robustez na seleção do melhor algoritmo e evitar o overfitting durante o ajuste de hiperparâmetros, adotamos uma estratégia de partição de dados em três conjuntos distintos, totalizando 581.012 observações:

- Conjunto de Treino (50%): Utilizado para o treinamento dos modelos e para o aprendizado dos padrões básicos de cada algoritmo.
- Conjunto de Validação (25%): Dedicado exclusivamente à comparação de desempenho e ao ajuste fino de hiperparâmetros. Este conjunto atuou como um "filtro de qualidade", garantindo que os modelos fossem avaliados em dados não vistos durante o treinamento, permitindo a seleção da melhor configuração para cada variante.
- Conjunto de Teste (25%): Reservado para a etapa final de inferência, garantindo uma avaliação imparcial e realista da capacidade de generalização do modelo campeão.

Essa segregação foi fundamental, pois possibilitou a experimentação intensiva com diversos pipelines de pré-processamento, assegurando que a escolha do algoritmo final não estivesse viciada pela otimização excessiva em um único conjunto de validação.

## 0.9 Pipeline baseline

O pipeline baseline foi estruturado para estabelecer uma base comparativa sólida e reprodutível. Para garantir a convergência dos algoritmos, aplicamos o StandardScaler em todas as variáveis numéricas, mitigando o impacto das diferentes escalas de magnitude nas predições.

Conscientes do alto custo computacional imposto pelo volume total do dataset (aproximadamente 290 mil instâncias no treino), adotamos uma estratégia de amostragem por redução. Selecionamos aleatoriamente 20% do conjunto de treino (cerca de 58 mil instâncias), mantendo a distribuição original das classes. Esta decisão técnica, pautada na eficiência operacional, permitiu a experimentação célere com modelos de alta complexidade como SVM, KNN, LVQ e MLP - sem comprometer a representatividade estatística dos dados.

A escolha pela subamostragem foi fundamentada na priorização da capacidade de iteração e refinamento dos algoritmos, considerando que ganhos marginais de desempenho com a totalidade das instâncias não justificariam o custo temporal elevado no estágio atual de experimentação.

## 0.10 Variantes do conjunto de treino

Para a experimentação, estabelecemos um baseline inicial para validar a performance bruta dos modelos. Contudo, dado o desbalanceamento severo das classes - especialmente a Classe 4, que representa apenas 0,5% do dataset - observamos uma degradação significativa no desempenho e sinais de overfitting nas classes majoritárias.

Por fim, observando que os modelos baseados em árvores de decisão demonstravam superioridade sistemática, testamos uma variante final: a utilização dos dados originais do baseline combinada com o parâmetro class weight . Esta estratégia permitiu que os algoritmos realizassem o balanceamento de forma nativa, penalizando erros em classes minoritárias durante o treinamento sem a necessidade de manipular o espaço amostral original. A Tabela 1 detalha esta evolução experimental.

Em um primeiro movimento para mitigar esse viés, aplicamos a técnica de Undersampling . Entretanto, esta abordagem resultou em uma redução drástica da base de dados, sacrificando a capacidade de generalização e induzindo um desempenho insatisfatório. Para corrigir essa perda de informação, adotamos uma estratégia híbrida ( SMOTE + Undersampling ), padronizando cada classe com 7.000 instâncias. Esta técnica permitiu que diversos algoritmos recuperassem o desempenho e respondessem positivamente à diversidade dos dados.

Tabela 1: Evolução das estratégias de balanceamento e suas justificativas teóricas.

| Variante         | Técnica                 | Hipótese / Justificativa                                                                                                                            |
|------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| v1_balanceamento | Undersampling           | Redução das classes majoritárias para forçar o modelo a priorizar a identifica- ção de classes minoritárias.                                        |
| v2_balanceamento | SMOTE + Under- sampling | Abordagem híbrida para compensar a perda de informação do v1 atra- vés da geração de dados sintéticos e reamostragem.                               |
| v3_balanceamento | Class Weights           | Utilização de penalização assimétrica nos dados brutos, permitindo que o mo- delo aprenda padrões de classes raras sem distorcer o espaço amostral. |

## Fase 4: Modeling

## 0.11 Espaços de busca utilizados

A estratégia de otimização foi estruturada em duas etapas utilizando RandomizedSearchCV , priorizando a eficiência computacional frente à exaustividade do Grid Search .

- Exploração Global: Inicialmente, realizou-se uma busca ampla no espaço de hiperparâmetros para mapear regiões de convergência e identificar os candidatos mais promissores.
- Refinamento Local: Em uma segunda chamada, restringimos o espaço de busca em torno dos melhores resultados encontrados anteriormente. Nesta fase, alguns parâmetros foram fixados enquanto outros foram explorados em intervalos mais granulares, permitindo o fi ne-tuning das arquiteturas de maior performance, como o XGBoost e o LightGBM do Pipeline 3 .

Essa abordagem bifásica permitiu maximizar a capacidade preditiva dos modelos dentro de uma restrição de tempo de processamento, garantindo que as configurações finais não fossem apenas resultado de uma busca aleatória, mas sim de um processo iterativo de refinamento estatístico.

## 0.12 Resultados por algoritmo

## 0.0.1 Análise do Algoritmo K-Nearest Neighbors(KNN)

Figura 3: Comparação do F1-Score do KNN: Baseline vs Pipelines.

<!-- image -->

Pipeline

A Figura 3 evidencia o comportamento do KNN frente às diferentes estratégias de pipeline . Analisando a performance, destacamos dois pontos críticos que ilustram os desafios de modelagem enfrentados:

- Baseline e Overfitting Severo: O Baseline alcança a maior métrica de validação ( F 1 = 0 . 71 ), contudo, o gap de 0.15 em relação ao treino revela um cenário de overfitting severo. O modelo "decorou"as instâncias do conjunto de treinamento, o que compromete sua capacidade de generalização em cenários reais.
- Pipeline 1 e Underfitting Severo: O Pipeline 1 apresenta uma queda acentuada no desempenho, com valores de F 1 ≈ 0 . 55 . Neste caso, a técnica de reamostragem aplicada introduziu um underfitting severo, tornando o modelo incapaz de capturar a complexidade da fronteira de decisão das classes, resultando em um desempenho insatisfatório tanto no treino quanto na validação.
- Pipeline 2 (Confiabilidade): Embora apresente um desempenho absoluto inferior ao Baseline , o Pipeline 2 demonstra a maior estabilidade entre as etapas ( gap = 0 . 05 ). Sob uma ótica de engenharia, este modelo é o mais resiliente, priorizando a consistência das predições em detrimento de uma otimização agressiva que, como demonstrado, gera vulnerabilidades ao sobreajuste.

## 0.0.2 Análise do Algoritmo: Learning Vector Quantization (LVQ

Figura 4: Comparação do F1-Score do LVQ: Baseline vs Pipelines.

Comparação do F1-Score do LVQ: Baseline vs Pipelines

Pipeline

<!-- image -->

Aanálise do algoritmo LVQ (Figura 4) revela uma performance estagnada em todos os cenários testados, com valores de F1-Score situados entre 0.39 e 0.46. Diferente de modelos que demonstraram sensibilidade às técnicas de balanceamento, o LVQ apresentou um underfitting persistente em todas as configurações.

- Insuficiência da Hipótese Algorítmica: Os resultados indicam que o problema não reside na qualidade ou na representatividade dos dados, mas na incapacidade da arquitetura LVQ em modelar a complexidade das relações não lineares presentes no dataset de cobertura florestal.
- Estabilidade no Underfitting: A ausência de variação significativa entre os pipelines reforça que, para este algoritmo, a fronteira de decisão é muito rígida. O LVQ, ao depender de protótipos fixos, falha em capturar as sutilezas das classes minoritárias, independentemente de como os dados são balanceados.

Conclui-se, portanto, que a escolha desta arquitetura é inadequada para o problema em questão. A persistência do underfitting frente a diferentes abordagens de preparação de dados valida o descarte desta classe de algoritmos em favor de métodos baseados em árvores, que demonstraram flexibilidade superior para o mapeamento do espaço amostral.

Figura 5: Comparação do F1-Score do SVM: Baseline vs Pipelines.

Comparação do F1-Score do SVM: Baseline vs Pipelines

Pipeline

<!-- image -->

## 0.0.3 Análise do Algoritmo: Support Vector Machine (SVM)

Semelhante ao observado no LVQ, o algoritmo SVM demonstrou uma incapacidade crônica em adaptar-se à topologia dos dados. Como ilustrado na Figura 5, os resultados permaneceram estagnados em torno de F 1 ≈ 0 . 47 , independentemente da estratégia de pipeline ou técnica de balanceamento aplicada.

- Underfitting e Rigidez do Hiperplano: O desempenho consistente abaixo de 0.50, combinado com a ausência de gap entre treino e validação, configura um caso clássico de underfitting . O modelo não possui a flexibilidade necessária para mapear as fronteiras de decisão complexas entre as 7 classes de cobertura florestal.
- Limitação da Hipótese de Espaço de Margem: A falha do SVM reforça a conclusão de que este problema exige algoritmos capazes de realizar uma partição hierárquica e adaptativa do espaço amostral algo inerente a modelos baseados em árvores, mas que o SVM, mesmo com transformações de kernel, não logrou efetuar com sucesso para este volume de variáveis.

Desta forma, assim como o LVQ, o SVM foi incapaz de entender os dados, pois sua estrutura de otimização de margens mostrou-se insuficiente para a dimensionalidade e a complexidade estatística do projeto.

Figura 6: Comparação do F1-Score da Árvore de Decisão: Baseline vs Pipelines.

<!-- image -->

Comparação do F1-Score do Decision Tree: Baseline vs Pipelines

Pipeline

## 0.0.4 Análise do Algoritmo: Decision Tree

Diferente dos algoritmos lineares, a Árvore de Decisão demonstrou uma excelente capacidade de adaptação aos dados, consolidando-se como uma das arquiteturas mais eficazes para este problema. A Figura 6 ilustra o comportamento do modelo frente às estratégias de otimização.

- Baseline e o Risco do Overfitting: O Baseline alcança um desempenho expressivo ( F 1 = 0 . 75 ), contudo, o gap entre treino e validação (0.12) alerta para uma memorização excessiva das instâncias de treinamento, indicando que o modelo pode estar construindo ramificações profundas e desnecessárias.
- Estabilidade nos Pipelines 1 e 2: Estes cenários apresentaram resultados consistentes, com quase total convergência entre os conjuntos de treino e validação ( gap ≈ 0 . 03 ). Embora tenham entregado métricas ligeiramente inferiores, a confiabilidade operacional destes modelos é superior, sendo ideais para cenários onde a estabilidade da inferência é crítica.
- Otimização no Pipeline 3: O Pipeline 3 consolidou-se como a melhor configuração, atingindo F 1 = 0 . 77 . Observa-se, no entanto, um "pezinho"no overfitting , com um gap de 0.08. Este resultado sinaliza que, embora tenhamos maximizado o poder preditivo, atingimos o li-

mite de complexidade do modelo, sendo este o ponto de inflexão onde ganhos marginais de performance podem comprometer a generalização.

Esta análise valida que, para a Árvore de Decisão, o equilíbrio entre capacidade preditiva e generalização é extremamente sensível, exigindo o monitoramento contínuo da profundidade das árvores (pruning) para garantir que o desempenho do Pipeline 3 se mantenha sustentável em produção.

## 0.0.5 Análise do Algoritmo: Random Forest

Figura 7: Comparação do F1-Score do Random Forest: Baseline vs Pipelines.

<!-- image -->

O algoritmo Random Forest ratificou a eficácia da abordagem de ensemble , superando de forma consistente a Árvore de Decisão individual em todas as configurações.

- Eficiência do Ensemble: A combinação de múltiplas árvores permitiu que o modelo capturasse padrões de forma mais robusta, elevando o F1-Score do Pipeline 3 para 0.83, um salto notável em relação ao desempenho da árvore única.
- Generalização Superior: Observa-se que, no Pipeline 2 , o modelo atingiu uma estabilidade quase perfeita entre treino (0.78) e validação (0.76), demonstrando que a técnica de bagging é altamente eficaz para mitigar o overfitting inerente a estruturas de árvore.
- Otimização no Pipeline 3: Novamente, o Pipeline 3 destaca-se pela performance de elite. Embora o gap de generalização (0.08) seja similar

ao observado em modelos anteriores, a performance absoluta superior valida a estratégia de manter este pipeline como o caminho para a maximização dos resultados.

Esta análise conclui que o Random Forest é uma das arquiteturas mais sólidas para este dataset, visto que a diversidade de árvores compensa o ruído introduzido pelas técnicas de reamostragem, resultando em um modelo que combina alta acurácia com uma resiliência significativamente maior que os classificadores unitários.

## 0.0.6 Análise do Algoritmo: Multi-Layer Perceptron (MLP)

Figura 8: Comparação do F1-Score da MLP: Baseline vs Pipelines.

Comparação do F1-Score do MLP: Baseline vs Pipelines

Pipeline

<!-- image -->

A arquitetura de Multi-Layer Perceptron (MLP) exibiu um comportamento clássico de sensibilidade aos dados, onde o poder de aproximação não linear da rede foi, paradoxalmente, seu maior risco de instabilidade.

- Baseline e o Overfitting de Alta Complexidade: O Baseline alcança um desempenho elevado ( F 1 = 0 . 83 ), contudo, o gap de 0.13 entre treino e validação é expressivo. Em modelos de redes neurais, esse gap indica que a MLP aproveitou sua alta capacidade de modelagem para aprender ruídos e particularidades do treino, perdendo capacidade de predição em dados inéditos.
- A Escolha pelo Pipeline 2: O Pipeline 2 apresenta um resultado de F 1 = 0 . 78 com uma redução drástica no gap de generalização

( gap ≈ 0 . 03 ). Esta configuração demonstra que, ao fornecer dados melhor estruturados e balanceados, a rede neural convergiu para padrões mais latentes e representativos, em vez de memorizar instâncias específicas.

- Resiliência Operacional: A escolha pelo Pipeline 2 para a MLP é justificada pela confiabilidade operacional. Em sistemas de classificação florestal, um modelo que mantém consistência entre treino e validação é superior a um modelo com métricas "infladas"pelo overfitting , pois garante um comportamento previsível sob novas condições ambientais ou de sensor.

Desta forma, a MLP no Pipeline 2 se consolida como uma alternativa viável e segura para o nosso ecossistema de modelos.

## 0.0.7 Análise do Algoritmo: Bagging MLP

Figura 9: Comparação do F1-Score do Bagging MLP: Baseline vs Pipelines. Comparação do F1-Score do Bagging MLP: Baseline vs Pipelines 1.0

<!-- image -->

A aplicação de Bagging sobre o Multi-Layer Perceptron (MLP) resultou em uma performance inferior à observada na arquitetura MLP isolada. Diferente dos modelos de árvore, onde o ensemble via bagging é altamente eficaz, no caso da MLP, a estratégia não produziu os ganhos esperados.

- Efeito de Degradação por Amostragem: O bagging baseia-se na criação de subconjuntos de dados ( bootstrapping ). Para a MLP, que exige um volume robusto de dados para ajustar seus pesos, a redução

- do conjunto de treino por bootstrap limitou a capacidade da rede de convergir para um mínimo global satisfatório.
- Limitação da Variância: Enquanto árvores de decisão são modelos de alta variância que se beneficiam da redução desta pela média, a MLP apresenta uma dinâmica de erro diferente. A média das predições de várias redes neurais subtreinadas (devido aos subconjuntos menores) não conseguiu compensar a perda de acurácia individual de cada rede.

Esta queda de desempenho confirma que, para este dataset, o bagging não é a técnica de ensemble adequada para redes neurais. A evidência aponta que a arquitetura exige o conjunto completo de dados para a otimização de seus hiperplanos, validando a escolha de descontinuar esta estratégia em favor de modelos que operam melhor com as características intrínsecas da topologia florestal.

## 0.0.8 Análise do Algoritmo: XGBoost

Figura 10: Comparação do F1-Score do XGBoost: Baseline vs Pipelines.

Comparação do F1-Score do XGBoost: Baseline vs Pipelines

Pipeline

<!-- image -->

O XGBoost consolidou-se como uma das arquiteturas mais eficazes do projeto, demonstrando uma capacidade de aprendizado superior aos modelos de bagging e modelos lineares.

- Performance de Elite no Pipeline 3: O Pipeline 3 atingiu F 1 = 0 . 89 , consolidando-se como o ápice de performance do modelo. O diferencial do XGBoost aqui foi a otimização de gradiente, que permitiu ao

modelo focar progressivamente nas instâncias mais difíceis de classificar (as classes minoritárias), algo que modelos estáticos não conseguem realizar.

- Convergência e Generalização: Enquanto o Baseline apresenta um overfitting acentuado ( gap = 0 . 15 ), o Pipeline 2 exibe um equilíbrio exemplar entre treino (0.83) e validação (0.80). O Pipeline 3 , embora tenha um gap de 0.08, compensa este custo com um ganho de performance substancial, provando que o modelo possui "capacidade de modelagem"o suficiente para sustentar essa complexidade sem colapsar em ruído.
- Robustez ao Desbalanceamento: O XGBoost, ao aplicar regularização nativa (L1/L2) durante o treino das árvores, mostrou-se intrinsecamente mais resistente ao desbalanceamento do que as árvores isoladas ou o Random Forest , validando a escolha deste algoritmo como um dos pilares da nossa solução final.

Esta análise demonstra que o XGBoost não apenas performou bem em termos métricos, mas também apresentou um comportamento previsível durante a transição entre os pipelines , reafirmando a maturidade desta arquitetura para o desafio proposto.

## 0.0.9 Análise do Algoritmo: LightGBM

Figura 11: Comparação do F1-Score do LightGBM: Baseline vs Pipelines.

<!-- image -->

Pipeline O LightGBM demonstrou ser a arquitetura mais eficaz para o desafio, atingindo o maior F1-Score de todo o projeto ( F 1 = 0 . 91 no Pipeline 3 ).

- Eficiência e Precisão: O LightGBM não apenas superou os demais modelos em métrica bruta, mas também exibiu uma capacidade superior de gerenciar a complexidade das árvores. Seu método de crescimento leaf-wise permitiu um ajuste muito mais fino às fronteiras de decisão complexas, capturando padrões que modelos mais rígidos (como SVM ou MLP) ignoraram.
- Otimização do Pipeline 3: Enquanto o Baseline beira o overfitting total (treino de 0.99 vs validação de 0.85), o Pipeline 3 reduz esse gap de forma significativa (treino de 0.99 vs validação de 0.91). Este incremento na validação é a prova definitiva de que o pipeline de balanceamento, aliado à arquitetura correta, é a chave para o sucesso do modelo.
- Conclusão da Arquitetura: A estabilidade observada no Pipeline 2 ( F 1 = 0 . 81 , sem overfitting ) e a performance de elite no Pipeline 3 consolidam o LightGBM como a escolha técnica definitiva. Ele provou ser o modelo que melhor reconcilia a capacidade preditiva com a resiliência estatística exigida pelo inventário florestal.

Com estes resultados, validamos a hipótese de que algoritmos de gradient boosting de alto desempenho são a espinha dorsal para a classificação do nosso problema. Contudo, a análise detalhada revelou que cada modelo (LightGBM, XGBoost, Random Forest) possui vieses distintos na classificação das classes minoritárias.

## 0.0.10 Análise do Algoritmo: Stacking Heterogêneo

O Stacking Heterogêneo representou o ápice da estratégia de modelagem, alcançando um F 1 = 0 . 94 no Pipeline 3 . A eficácia desta arquitetura reside na exploração da complementaridade entre diferentes algoritmos.

- Meta-aprendizagem e Complementaridade: Ao utilizar o XGBoost como meta-modelo, a arquitetura foi capaz de "aprender a aprender", ponderando as previsões do LightGBM (que capturou nuances locais) com a robustez de modelos como Random Forest e MLP (que forneceram visões alternativas do espaço de características).
- Redução do Erro Residual: Enquanto modelos individuais podem ser "enganados"por ruídos específicos em certas classes, o Stacking

Figura 12: Comparação do F1-Score do Stacking Heterogêneo: Baseline vs Pipelines.

<!-- image -->

Pipeline

atuou como um filtro, onde os modelos base se auto-corrigem através do meta-aprendizado. Isso explica por que o Pipeline 3 superou o patamar de 0.91 obtido pelo melhor modelo individual.

- Generalização e Confiabilidade: Com um gap de apenas 0.05 entre treino e validação, o Stacking mostrou-se não apenas o modelo mais preciso, mas também um dos mais equilibrados. A inclusão da MLP neste cenário específico forneceu a não-linearidade adicional necessária para elevar a performance final, demonstrando que a heterogeneidade da arquitetura foi o diferencial para o sucesso.

Com estes resultados, concluímos que a estratégia de Stacking Heterogêneo é a solução ótima para o inventário florestal. Esta arquitetura entrega a maior performance absoluta atingida no projeto, mantendo um comportamento estável e validando a hipótese de que a combinação de diferentes "inteligências"algorítmicas supera a otimização isolada de qualquer modelo individual.

## 0.0.11 Conclusão da Fase de Avaliação

O processo de avaliação permitiu traçar uma trajetória clara sobre a eficácia das diferentes famílias de algoritmos para a classificação da cobertura florestal. A investigação sistemática, iniciada com o Baseline e evoluindo através de estratégias rigorosas de pipeline e ensemble , revelou padrões fun- damentais sobre a natureza dos dados e a capacidade de modelagem de cada arquitetura.

A análise confirmou que o Pipeline 3 apresenta-se como a arquitetura de maior potencial, otimizando o balanço entre capacidade preditiva e generalização. Entretanto, é imperativo notar que a eficácia destas configurações está condicionada à robustez de suas estruturas de ensemble .

Identificamos que modelos lineares e de baixa complexidade (KNN, SVM, LVQ) enfrentam limitações estruturais diante da complexidade multiespectral e do desbalanceamento do conjunto de dados, apresentando resultados de underfitting persistentes. Em contraste, arquiteturas baseadas em árvores de decisão - especialmente quando integradas em técnicas de boosting e stacking -demonstraram uma flexibilidade superior, sendo capazes de capturar fronteiras de decisão complexas com eficácia.

Nesta etapa, consolidamos o Stacking Heterogêneo e o LightGBM como os candidatos com maior poder discriminativo. A definição definitiva do modelo campeão, contudo, permanece reservada para a etapa de implantação e avaliação no conjunto de teste final, onde a métrica de generalização será o critério determinante para assegurar que a solução escolhida não apenas performa sob as condições do treinamento, mas mantém sua integridade operacional frente a dados inéditos.

## Fase 5: Evaluation

## 0.13 Baseline consolidado

A análise do baseline (Figura 13) revelou um comportamento propenso ao overfitting na maioria dos algoritmos testados, onde a disparidade na frequência das classes induziu os modelos a memorizarem as características das classes majoritárias.

Portanto, a aplicação das técnicas de balanceamento não visou apenas uma "limpeza"dos dados, mas sim a equalização da representatividade de cada classe no espaço de treinamento. Ao mitigar o viés em favor das classes dominantes, buscamos forçar os algoritmos a generalizarem os padrões das classes minoritárias, reduzindo assim o gap de desempenho entre treino e validação e conferindo maior robustez ao modelo final.

## 0.14 Comparação baseline vs variantes

A análise comparativa entre o Baseline e os diferentes Pipelines de balanceamento permite avaliar o impacto da reamostragem na performance global dos Comparação do F1 (Macro): Treino vs Validação no baseline modelos. A Tabela 2 sintetiza os resultados estatísticos desta comparação.

Figura 13: Comparação do F1-Score (Macro) entre conjuntos de Treino e Validação no baseline.

<!-- image -->

Tabela 2: Resumo Estatístico: Baseline vs. Pipelines

| Comparação             |   Estatística |   p-value | Significativo (5%)   |
|------------------------|---------------|-----------|----------------------|
| Baseline vs Pipeline 1 |           0.0 |  0.001953 | Sim                  |
| Baseline vs Pipeline 2 |           5.0 |  0.021484 | Sim                  |
| Baseline vs Pipeline 3 |           0.0 |  0.062500 | Não                  |

- Pipelines 1 e 2 (Visão Global): Ao comparar os pipelines universais contra o Baseline , observa-se uma diferença estatisticamente significativa ( p &lt; 0 . 05 ). Este resultado indica que a aplicação de técnicas de balanceamento em modelos heterogêneos (que incluem algoritmos lineares) introduz variações que afastam o desempenho dos modelos em relação ao Baseline original.
- Pipeline 3 (Foco em Árvores): Ao isolar o Pipeline 3 , que concentra arquiteturas mais resilientes, nota-se um resultado distinto: o teste estatístico resultou em um p &gt; 0 . 05 ( p = 0 . 0625 ). Esta ausência de significância estatística indica que o Pipeline 3 alcança um desempenho equivalente ao do Baseline , porém com a vantagem crítica de maior robustez e menor propensão ao overfitting , tornando-o a estratégia mais equilibrada dentre as testadas.

## 0.15 Seleção do melhor modelo

Após a análise exaustiva de todas as arquiteturas, o LightGBM foi selecionado como o modelo de referência para este projeto. Embora o Stacking Heterogêneo tenha apresentado resultados marginais superiores em termos de acurácia bruta, a escolha do LightGBM fundamenta-se em critérios de engenharia e robustez operacional:

- Generalização e Consistência: O LightGBM demonstrou uma performance superior na manutenção da estabilidade do F1-Score entre o conjunto de treino e o de validação, indicando uma menor propensão ao overfitting quando comparado à complexidade de um ensemble de várias camadas.
- Evidência Estatística (AUC-ROC): Conforme ilustrado na Figura 14, o LightGBM apresentou a maior área sob a curva (AUC = 0.997). Este valor, próximo à unidade, atesta uma capacidade de discriminação de classes quase perfeita e superior às demais arquiteturas testadas.
- Viabilidade Operacional: Em ambientes de produção, a simplicidade de uma arquitetura baseada em árvores de gradiente é preferível à complexidade inerente de um Stacking , que exige o gerenciamento de múltiplos modelos base e um meta-aprendiz. O LightGBM oferece o melhor equilíbrio entre alta acurácia, latência reduzida e facilidade de manutenção a longo prazo.

Multi-Class ROC Curves Comparison

Figura 14: Curvas ROC comparativas das arquiteturas de melhor performance (Pipeline 3).

<!-- image -->

Desta forma, o LightGBM consolida-se não apenas pelo seu desempenho estatístico demonstrado pela curva ROC, mas pela sua confiabilidade, sendo a escolha técnica mais adequada para a implementação e o monitoramento em cenários de inventário florestal real.

## 0.16 Avaliação final no conjunto de teste

A análise do desempenho no conjunto de teste (Figura 15) evidencia a superioridade das arquiteturas baseadas em árvores de decisão, que atingiram seu desempenho ótimo através do Pipeline 3 . Observa-se que, enquanto modelos lineares mantiveram métricas estagnadas e inferiores, a combinação de técnicas de balanceamento e otimização de hiperparâmetros nos modelos de ensemble resultou em um treinamento significativamente mais equânime.

Ao comparar o conjunto de treino com o de teste, constatamos uma redução drástica do overfitting em relação ao baseline (excluindo o SVM, LVQ e Bagging de Mlps), confirmando que os modelos agora possuem uma capacidade de generalização robusta. Em suma, a transição entre as estratégias de pipeline permitiu evoluir de modelos que apresentavam subajuste ou sobreajuste para arquiteturas capazes de reconhecer padrões complexos de forma estável, assegurando a confiabilidade necessária para a aplicação prática.

Figura 15: Comparação do F1-Score (Macro) entre Treino e Teste para a melhor configuração de cada modelo.

<!-- image -->

## Fase 6: Deployment

## 0.17 Como o modelo seria utilizado

Após a validação final, o LightGBM foi selecionado como modelo campeão. Ele será integrado ao ecossistema de TI do USFS para automatizar o mapeamento florestal. O modelo será serializado em formato ONNX e encapsulado em um contêiner Docker, garantindo reprodutibilidade. A API, desenvolvida com FastAPI, permitirá dois fluxos:

- Processamento em Lote (Batch): Para a atualização de mapas geográficos em larga escala, recebendo arquivos volumosos via GIS para processamento assíncrono.
- Consultas em Tempo Real (On-demand): Para agentes em campo, onde a API processa coordenadas topográficas e variáveis físicas, retornando o tipo de cobertura em milissegundos.

## 0.18 Riscos e mitigações

A operação envolve riscos que devem ser geridos para garantir a confiabilidade:

- Risco 1: Deslocamento Geográfico de Dados (Data Drift): O modelo pode falhar ao prever áreas fora da distribuição original. Mitigação: Implementação de uma camada de validação na API que bloqueia requisições com variáveis fora dos limites operacionais do conjunto de treino.
- Risco 2: Ambiguidade em Classes Minoritárias: A classe 4 (Cottonwood/Willow) apresenta uma taxa de erro de 6,1% , confundindose frequentemente com a Classe 3 (Ponderosa Pine) . Mitigação: Estratégia de Human-in-the-loop . Caso a probabilidade do predict\_proba seja inferior a um limiar de 80% , a predição será sinalizada como "Baixa Confiança", encaminhando o caso para revisão manual por um especialista florestal.

## 0.19 Monitoramento e retreinamento

Estruturamos uma esteira de MLOps para evitar o Model Decay :

Política de Retreinamento (Trigger-based): O retreinamento ocorrerá sob dois gatilhos independentes:

Monitoramento de Métricas: Utilizaremos ferramentas de observabilidade para identificar desvios estatísticos (Data Drift). O sistema emitirá alertas automáticos caso a distribuição de entrada em produção divirja do perfil de treino.

1. Monitoramento de Estabilidade (PSI): Definimos um limiar de alerta de 0.15 para o PSI, indicando uma mudança moderada na distribuição dos dados que exige investigação diagnóstica. Caso o PSI ultrapasse 0.20, o modelo é classificado como instável, disparando um gatilho automático de retreinamento.
2. Monitoramento de Performance ( Ground Truth ): Caso amostras reais de auditoria indiquem que o F1-Score Macro do modelo em produção caiu abaixo de 85%, o sistema iniciará um ciclo de reajuste de parâmetros e atualização do modelo.

Estratégia de Atualização ( Shadow Deployment ): Novos modelos serão validados em "modo sombra", processando requisições reais em paralelo sem afetar o usuário final. Após um período de 5 dias, o modelo superior substituirá o anterior de forma transparente.

## 1 Conclusão e trabalhos futuros

Ao término deste estudo, consolidamos a compreensão de que o dataset de inventário florestal apresenta uma natureza complexa, caracterizada por alta dimensionalidade, disparidade acentuada entre classes e uma topologia multiespectral que exige arquiteturas robustas para sua interpretação. A investigação sistemática conduzida demonstrou que modelos de baixa complexidade (KNN, SVM, LVQ) e estratégias de bagging sobre redes neurais são insuficientes para mapear as fronteiras de decisão deste problema, incorrendo invariavelmente em quadros de underfitting .

Para trabalhos futuros, o foco deve transitar da otimização laboratorial para a validação operacional. Propõe-se a implementação dos modelos em ambiente de produção para a realização de testes de inferência em tempo real com dados inéditos. Adicionalmente, sugere-se a exploração de técnicas de monitoramento de data drift para assegurar que a performance observada nestes testes seja mantida à medida que as condições ambientais ou as características dos sensores florestais venham a evoluir, garantindo a sustentabilidade da solução a longo prazo.

A evidência empírica apontou que modelos baseados em árvores de decisão, notadamente aqueles potencializados por técnicas de gradient boosting , constituem o estado da arte para este desafio. Dentre as arquiteturas avaliadas, o LightGBM destacou-se por atingir métricas de performance superiores a 90%, mantendo uma capacidade de generalização que supera a fragilidade de modelos mais simples. Paralelamente, o Stacking Heterogêneo provou ser um mecanismo eficaz de meta-aprendizado, capturando nuances que classificadores unitários, por vezes, negligenciam.

## 2 Reprodutibilidade e ferramentas

Para garantir a reprodutibilidade dos experimentos e a integridade da análise científica, a implementação deste projeto foi estruturada visando a transparência metodológica e a facilidade de acesso ao ambiente computacional.

## 0.1 Ambiente Computacional

Os experimentos foram executados no ambiente Google Colab , utilizando o kernel padrão de Python 3 . Esta escolha permitiu a padronização das biblio- tecas e o acesso a recursos de processamento necessários para o treinamento das arquiteturas de boosting e stacking . O código-fonte, o conjunto de dados e a documentação completa estão disponíveis no repositório oficial do projeto 1 .

## 0.2 Tecnologias e Dependências

O ecossistema tecnológico foi construído sobre bibliotecas consolidadas na comunidade de Ciência de Dados. A gestão de dependências foi centralizada em um arquivo de requisitos ( requirements.txt ), garantindo que a versão das bibliotecas seja consistente em qualquer instância de execução. As tecnologias centrais utilizadas incluem:

- Manipulação e Processamento: Pandas e NumPy para a estruturação e cálculo vetorial dos dados.
- Aprendizado de Máquina: Scikit-learn para os classificadores base, XGBoost e LightGBM para as arquiteturas de gradient boosting , e Imbalanced-learn para as técnicas de reamostragem (*pipelines* de balanceamento).
- Visualização: Matplotlib e Seaborn para a análise exploratória e a geração de curvas de desempenho (ROC e PR).

O fluxo de trabalho foi desenhado de forma modular, permitindo que cada etapa - da pré-processamento à inferência final - possa ser executada sequencialmente, assegurando a fidelidade dos resultados reportados neste documento.

## Referências

## Referências

- [1] PEDREGOSA, F. et al. Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research , v. 12, p. 2825-2830, 2011.
- [2] CHEN, T.; GUESTRIN, C. XGBoost: A Scalable Tree Boosting System. Proceedings of the 22nd ACM SIGKDD , p. 785-794, 2016.

[1 https://github.com/Hugo-Mendonca/Classification-covertype](https://github.com/Hugo-Mendonca/Classification-covertype)

- [3] KE, G. et al. LightGBM: A Highly Efficient Gradient Boosting Decision Tree. Advances in Neural Information Processing Systems , v. 30, 2017.
- [4] LEMAITRE, G.; NOGUEIRA, F.; ARJUNA, C. K. Imbalanced-learn: A Python Toolbox to Tackle the Curse of Imbalanced Datasets in Machine Learning. Journal of Machine Learning Research , v. 18, p. 1-5, 2017.
- [5] McKINNEY, W. Data Structures for Statistical Computing in Python. Proceedings of the 9th Python in Science Conference , p. 51-56, 2010.
- [6] DUA, D.; GRAFF, C. UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Sciences, 2017. Disponível em: &lt;http://archive.ics.uci.edu/ml&gt;. Acesso em: 10 jun. 2026.