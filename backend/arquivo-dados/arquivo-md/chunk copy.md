--- CHUNK 1 ---
## Relatório Final do Projeto Mineração de Dados Aplicada com CRISP-DM

Grupo:Hugo Mendonça, Danilo Regino Barrote, Bernardo Siqueira Batista

Cliente: US Forest Service (USFS)

IF1014 - 2026.1


## Resumo

--- CHUNK 2 ---
O dataset Covertype, composto por sete classes de cobertura florestal, apresenta desafios significativos devido ao desbalanceamento severo das amostras. Este projeto propõe o desenvolvimento de modelos de aprendizado de máquina para a classificação automatizada desses tipos de cobertura, visando otimizar estratégias de preservação ambiental e planejamento turístico. Para mitigar o viés das classes majoritárias, a métrica F1-Score (Macro) foi adotada como critério principal de avaliação

--- CHUNK 3 ---
. Foram avaliadas diversas arquiteturas, comparando estratégias de balanceamento (Baseline, pipelines de reamostragem e pesos balanceados). O modelo LightGBM, configurado com o Pipeline 3, obteve o desempenho mais expressivo, alcançando 99% de F1Score no treinamento, 91% na validação e 93% no conjunto de teste. Estes resultados confirmam a alta capacidade discriminativa do modelo e sua robustez na generalização de padrões complexos.

--- CHUNK 4 ---
## Sumário

--- CHUNK 5 ---
| Fase 1: Business Understanding . . . . . . .                         | Fase 1: Business Understanding . . . . . . .                         |

| 0.1 Cliente e contexto . . .                                         | . . . . . . 3                                                        |

--- CHUNK 6 ---
| 0.2 Problema de negócio . . . . . . . . .                            | . . . . . . 3                                                        |
| 0.3 Critério de Sucesso . . . . . . . .                              | . . . . . . 4                                                        |
| 0.4 Risco e impacto ético . . . . . . . .                            | . . . . . . 5                                                        |

--- CHUNK 7 ---
| Fase 2: Data Understanding 5 . . . . . . . . . . . . . . . . . . . . | Fase 2: Data Understanding 5 . . . . . . . . . . . . . . . . . . . . |
| 0.5 Dataset escolhido                                                | . . . . . . 5 . . . . . .                                            |
| 0.6 Análise exploratória . . . . . . . .                             | 6                                                                    |

--- CHUNK 8 ---
| 0.7 Implicações para a modelagem . . .                               | . . . . . . 8                                                        |
| Fase 3: Data Preparation . . . . . . . . . . .                       | Fase 3: Data Preparation . . . . . . . . . . .                       |
| 0.8 Partição treino, validação e teste .                             | . . . . . 9                                                          |

--- CHUNK 9 ---
| 0.9 Pipeline baseline . .                                                                                                                           | 0.9 Pipeline baseline . .                                                                                                                           | 0.9 Pipeline baseline . .                                                                                                                           |

--- CHUNK 10 ---

--- CHUNK 11 ---
| 0.10 Variantes do conjunto de treino . . . . . . . . . . . . . . . . . 10                                                                           | 0.10 Variantes do conjunto de treino . . . . . . . . . . . . . . . . . 10                                                                           | 0.10 Variantes do conjunto de treino . . . . . . . . . . . . . . . . . 10                                                                           |

--- CHUNK 12 ---
| Fase 4: Modeling 11 0.11 Espaços de busca utilizados . . . . . . . . . . . . . . . . . . . . 11                                                     | Fase 4: Modeling 11 0.11 Espaços de busca utilizados . . . . . . . . . . . . . . . . . . . . 11                                                     | Fase 4: Modeling 11 0.11 Espaços de busca utilizados . . . . . . . . . . . . . . . . . . . . 11                                                     |

--- CHUNK 13 ---
| 0.12 Resultados por algoritmo . . . . . . . . . . . . . . . . . . . . . 12                                                                          | 0.12 Resultados por algoritmo . . . . . . . . . . . . . . . . . . . . . 12                                                                          | 0.12 Resultados por algoritmo . . . . . . . . . . . . . . . . . . . . . 12                                                                          |

--- CHUNK 14 ---
| 0.0.1                                                                                                                                               | Análise do Algoritmo K-Nearest Neighbors(KNN) . . .                                                                                                 | 12                                                                                                                                                  |

--- CHUNK 15 ---
| 0.0.2                                                                                                                                               | Análise do Algoritmo: Learning Vector Quantization (LVQ . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                     | 13                                                                                                                                                  |

--- CHUNK 16 ---
| 0.0.3                                                                                                                                               | Análise do Algoritmo: Support Vector Machine (SVM)                                                                                                  | 14                                                                                                                                                  |

--- CHUNK 17 ---
| 0.0.4                                                                                                                                               | Análise do Algoritmo: Decision Tree . . . . . . . . . .                                                                                             | 15                                                                                                                                                  |

--- CHUNK 18 ---
| 0.0.5                                                                                                                                               | Análise do Algoritmo: Random Forest . . . . . . .                                                                                                   | 16                                                                                                                                                  |

--- CHUNK 19 ---
| 0.0.6                                                                                                                                               | . . Análise do Algoritmo: Multi-Layer Perceptron (MLP) .                                                                                            | 17                                                                                                                                                  |

--- CHUNK 20 ---
| 0.0.7                                                                                                                                               | Análise do Algoritmo: Bagging MLP . . . . . . . . . . . . .                                                                                         | 18                                                                                                                                                  |

--- CHUNK 21 ---
| 0.0.8                                                                                                                                               | Análise do Algoritmo: XGBoost . . . . . . . . . .                                                                                                   | 19                                                                                                                                                  |

--- CHUNK 22 ---
| 0.0.9                                                                                                                                               | Análise do Algoritmo: LightGBM . . . . . . . . . . .                                                                                                | 20                                                                                                                                                  |

--- CHUNK 23 ---
| 0.0.10                                                                                                                                              | . Análise do Algoritmo: Stacking Heterogêneo . . . . . .                                                                                            | 21                                                                                                                                                  |

--- CHUNK 24 ---
| 0.0.11                                                                                                                                              | Conclusão da Fase de Avaliação . . . . . . . . . . . . .                                                                                            | 22                                                                                                                                                  |

--- CHUNK 25 ---
| Fase 5: Evaluation 23                                                                                                                               | Fase 5: Evaluation 23                                                                                                                               | Fase 5: Evaluation 23                                                                                                                               |

--- CHUNK 26 ---
| 0.13 Baseline consolidado . . . . . . . . . . . . . . . . . . . . . . . . 23                                                                        | 0.13 Baseline consolidado . . . . . . . . . . . . . . . . . . . . . . . . 23                                                                        | 0.13 Baseline consolidado . . . . . . . . . . . . . . . . . . . . . . . . 23                                                                        |

--- CHUNK 27 ---
| 0.14 Comparação baseline vs variantes . . . . . . . . . . . . . . . . 23                                                                            | 0.14 Comparação baseline vs variantes . . . . . . . . . . . . . . . . 23                                                                            | 0.14 Comparação baseline vs variantes . . . . . . . . . . . . . . . . 23                                                                            |

--- CHUNK 28 ---
| 0.15 Seleção do melhor modelo . . . . . . . . . . . . . . . . . . . . . 25                                                                          | 0.15 Seleção do melhor modelo . . . . . . . . . . . . . . . . . . . . . 25                                                                          | 0.15 Seleção do melhor modelo . . . . . . . . . . . . . . . . . . . . . 25                                                                          |

--- CHUNK 29 ---
| 0.16 Avaliação final no conjunto de teste . . . . . . . . . . . . . . . 26 6: Deployment 27                                                         | 0.16 Avaliação final no conjunto de teste . . . . . . . . . . . . . . . 26 6: Deployment 27                                                         | 0.16 Avaliação final no conjunto de teste . . . . . . . . . . . . . . . 26 6: Deployment 27                                                         |

--- CHUNK 30 ---
| Fase                                                                                                                                                | Fase                                                                                                                                                | Fase                                                                                                                                                |

--- CHUNK 31 ---
| 0.17 Como o modelo seria utilizado . . . . . . . . . . . . . . . . . . 27                                                                           | 0.17 Como o modelo seria utilizado . . . . . . . . . . . . . . . . . . 27                                                                           | 0.17 Como o modelo seria utilizado . . . . . . . . . . . . . . . . . . 27                                                                           |

--- CHUNK 32 ---
| 0.18 Riscos e mitigações . . . . . . . . . . . . . . . . . . . . . . . . 28 0.19 Monitoramento e retreinamento . . . . . . . . . . . . . . . . . 28 | 0.18 Riscos e mitigações . . . . . . . . . . . . . . . . . . . . . . . . 28 0.19 Monitoramento e retreinamento . . . . . . . . . . . . . . . . . 28 | 0.18 Riscos e mitigações . . . . . . . . . . . . . . . . . . . . . . . . 28 0.19 Monitoramento e retreinamento . . . . . . . . . . . . . . . . . 28 |

--- CHUNK 33 ---
| 1 Conclusão e trabalhos futuros 29                                                                                                                  | 1 Conclusão e trabalhos futuros 29                                                                                                                  | 1 Conclusão e trabalhos futuros 29                                                                                                                  |

--- CHUNK 34 ---
| 2 Reprodutibilidade e ferramentas 29                                                                                                                | 2 Reprodutibilidade e ferramentas 29                                                                                                                | 2 Reprodutibilidade e ferramentas 29                                                                                                                |

--- CHUNK 35 ---
| 0.1 Ambiente Computacional . . . . . . . . . . . . . . . . . . . . . 29                                                                             | 0.1 Ambiente Computacional . . . . . . . . . . . . . . . . . . . . . 29                                                                             | 0.1 Ambiente Computacional . . . . . . . . . . . . . . . . . . . . . 29                                                                             |

--- CHUNK 36 ---
| 0.2 Tecnologias e Dependências . . . . . . . . . . . . . . . . . . . 30 Referências 30                                                              | 0.2 Tecnologias e Dependências . . . . . . . . . . . . . . . . . . . 30 Referências 30                                                              | 0.2 Tecnologias e Dependências . . . . . . . . . . . . . . . . . . . 30 Referências 30                                                              |

--- CHUNK 37 ---
## Fase 1: Business Understanding

### 0.1 Cliente e contexto

--- CHUNK 38 ---
A gestão sustentável de ecossistemas florestais de grande escala representa um dos maiores desafios contemporâneos para a preservação da biodiversidade global

--- CHUNK 39 ---
. Neste cenário, o US Forest Service (USFS), órgão vinculado ao Departamento de Agricultura dos Estados Unidos, desempenha um papel fundamental na administração de milhões de hectares de terras federais, onde a identificação precisa da tipologia florestal - a "cobertura vegetal"(Covertype) - é o pilar que sustenta ações estratégicas que variam desde o combate a incêndios e o manejo de pragas até a delimitação de zonas de conservação estrita

--- CHUNK 40 ---
. Atualmente, o monitoramento tradicional desses recursos depende amplamente de inventários de campo, um processo intrinsecamente custoso, moroso e limitado em sua capacidade de escala territorial.

--- CHUNK 41 ---
Para endereçar essa falha, o presente trabalho propõe o desenvolvimento de um sistema de classificação automatizado baseado em uma arquitetura de Stacking Heterogêneo. Através de um pipeline que integra técnicas avançadas de balanceamento de classes e refinamento iterativo de hiperparâmetros, consolidamos a inteligência de diversos modelos, como LightGBM, XGBoost e Random Forest, sob a regência de um meta-aprendiz

--- CHUNK 42 ---
. Essa abordagem garante ao USFS uma ferramenta de suporte à decisão com alta sensibilidade para todas as tipologias florestais, transformando dados brutos em inteligência estratégica capaz de promover uma preservação mais eficiente e baseada em evidências.

--- CHUNK 43 ---
A automação dessa análise, por meio da integração de dados geoespaciais e técnicas de aprendizado de máquina, surge como a alternativa mais viável para otimizar o monitoramento. Contudo, essa transição tecnológica enfrenta um obstáculo estatístico crítico: o desbalanceamento severo das classes

--- CHUNK 44 ---
. O dataset Covertype, que reflete a distribuição real de tipologias em áreas de alta altitude, é dominado por classes majoritárias, enquanto tipos de vegetação ecologicamente sensíveis - como certas espécies de coníferas ameaçadas pelas mudanças climáticas - figuram como classes minoritárias raras. Quando um modelo preditivo é treinado sem o devido rigor estatístico, ele tende a ignorar tais classes em prol da maximização da acurácia global, falhando justamente na proteção dos ecossistemas mais frágeis.

--- CHUNK 45 ---
### 0.2 Problema de negócio

--- CHUNK 46 ---
O problema de negócio central deste projeto reside na ineficiência operacional do US Forest Service (USFS) ao realizar inventários florestais em áreas vastas e de difícil acesso. O monitoramento manual é um processo moroso e dispendioso, que frequentemente deixa lacunas críticas na gestão ambiental

--- CHUNK 47 ---
. Mais grave ainda é o viés estatístico presente nos dados: como a maioria das tipologias florestais é composta por classes majoritárias, modelos de monitoramento convencionais tendem a ignorar as espécies mais raras e ecologicamente sensíveis, falhando justamente na proteção dos ecossistemas sob maior ameaça.

--- CHUNK 48 ---
Para o USFS, essa imprecisão não é apenas um erro técnico, mas um risco estratégico, pois direciona recursos de conservação para áreas que não necessitam de intervenção urgente, negligenciando pontos críticos de biodiversidade. Portanto, o desafio de negócio consiste em superar o desbalanceamento dos dados, utilizando modelos de aprendizado de máquina para transformar variáveis geoespaciais em um mapa dinâmico de prioridades

--- CHUNK 49 ---
. Essa solução permite ao órgão alocar verbas e equipes de campo de forma prescritiva, garantindo que as decisões de preservação florestal sejam baseadas em evidências estatísticas robustas, capazes de identificar e proteger ecossistemas frágeis antes que a degradação se torne irreversível, além de otimizar a alocação de mão de obra e mitigar riscos ocupacionais ao reduzir a necessidade de inspeções presenciais em áreas remotas e inóspitas.

--- CHUNK 50 ---
### 0.3 Critério de Sucesso

O sucesso deste projeto não é medido apenas pela performance algorítmica, mas pelo impacto direto na eficácia das operações de conservação florestal. O critério de sucesso está dividido em duas frentes complementares:

--- CHUNK 51 ---
- 1. Critério Técnico (Performance do Modelo): O objetivo técnico é atingir um F1-Score Macro igual ou superior a 0.85 no conjunto de teste. A escolha desta métrica é mandatória pois, ao contrário da acurácia simples, o F1-Score penaliza severamente o modelo que ignora classes minoritárias

--- CHUNK 52 ---
. Portanto, um valor elevado neste indicador garante que o modelo possui alta sensibilidade para detectar todas as tipologias florestais, incluindo as espécies raras e ecologicamente sensíveis que são o foco da preservação.

--- CHUNK 53 ---
- 2. Critério de Negócio (Impacto Operacional): Do ponto de vista es-

--- CHUNK 54 ---
de levantamentos de campo em áreas onde a classificação do modelo apresenta alta confiança, permitindo que a mão de obra especializada

- tratégico, o sucesso é validado pela capacidade do modelo em: Redução da Incerteza: Diminuir em pelo menos 30% a necessidade

seja realocada para áreas de classificação incerta ou zonas de maior risco de degradação.

--- CHUNK 55 ---
Sensibilidade Prescritiva: Garantir que 100% das classes minoritárias sejam corretamente identificadas em mais de 80% das instâncias, assegurando que o USFS não perca a visibilidade sobre nenhum ecossistema frágil.

--- CHUNK 56 ---
Confiabilidade de Decisão: Fornecer ao órgão uma ferramenta que atue como suporte à decisão, validada por uma matriz de confusão que demonstre baixa taxa de erro de classificação entre tipologias distintas, evitando custos desnecessários com o envio de equipes para áreas que foram classificadas erroneamente.

### 0.4 Risco e impacto ético

--- CHUNK 57 ---
### 0.4 Risco e impacto ético

A implementação desta solução introduz riscos técnicos e implicações éticas que devem ser gerenciados com rigor. Primeiramente, a magnitude do dataset Covertype impõe desafios significativos de custo computacional; a necessidade de elevado processamento para o treinamento de modelos robustos pode limitar a escalabilidade e a frequência de atualizações do sistema, caso não haja uma infraestrutura otimizada.

--- CHUNK 58 ---
Do ponto de vista ético, o maior risco reside na propagação de vieses estatísticos inerentes ao desbalanceamento das classes. Caso o modelo privilegie excessivamente as tipologias majoritárias, ele pode classificar erroneamente ecossistemas raros - frequentemente aqueles com maior valor de biodiversidade ou sob maior risco de degradação

--- CHUNK 59 ---
. Essa falha de predição, se utilizada como base para políticas públicas do USFS, poderia resultar em uma alocação inadequada de verbas e pessoal, negligenciando áreas que demandam atenção urgente. Portanto, a ética no projeto impõe a transparência sobre as limitações do modelo e a adoção de métricas de avaliação, como o F1-Score, que garantam a equidade na identificação de todas as classes, mitigando o risco de omissões prejudiciais ao patrimônio ambiental.

--- CHUNK 60 ---
## Fase 2: Data Understanding

### 0.5 Dataset escolhido

O dataset Covertype é uma base de dados clássica de sensoriamento remoto, amplamente utilizada em problemas de classificação multiclase. Ele descreve a cobertura florestal de quatro áreas de estudo na Floresta Nacional de Roosevelt, no Colorado (EUA), com o objetivo de prever o tipo de vegetação a partir de variáveis cartográficas.

## Características técnicas:

- Volume: 581.012 instâncias.

- Dimensionalidade: 54 colunas (features).

--- CHUNK 61 ---
- Dimensionalidade: 54 colunas (features).

- Target: Variável Cover\_Type com 7 classes distintas.

## Composição das variáveis:

- Quantitativas (10): Incluem elevação, aspecto, declividade, distância hidrológica, distância para estradas e radiação solar.
- Binárias (44): Representam dados categóricos transformados via OneHot Encoding , sendo 4 para Wilderness Area e 40 para a classificação do tipo de solo.

--- CHUNK 62 ---
Tipologias Florestais (Classes): Omodelo atua sobre 7 classes: Spruce/Fir , Lodgepole Pine , Ponderosa Pine , Cottonwood/Willow , Aspen , Douglas-fir e Krummholz . Odesafio técnico central reside no desbalanceamento severo : enquanto Lodgepole Pine domina a amostragem com centenas de milhares de registros, classes como Cottonwood/Willow são minoritárias e raras, exigindo técnicas de modelagem robustas para evitar o viés em favor das classes majoritárias.

### 0.6 Análise exploratória

--- CHUNK 63 ---
### 0.6 Análise exploratória

A análise exploratória confirmou a alta integridade estrutural do dataset , que se encontra totalmente preenchido, eliminando a necessidade de técnicas de imputação e mitigando o risco de introduzir ruídos artificiais nos dados.

--- CHUNK 64 ---
Identificamos um desbalanceamento severo na distribuição das classes, conforme mostra a Figura 1 . Este cenário valida nossa escolha pelo F1-Score Macro , visto que a acurácia global seria enviesada pelas classes majoritárias (1 e 2), negligenciando tipologias raras.

Figura 1: Distribuição das classes: o desbalanceamento motiva a métrica de avaliação.

<!-- image -->

--- CHUNK 65 ---
<!-- image -->

Por fim, a análise da variável Elevation ( Figura 2 ) revela outliers que, embora presentes, são inerentes à heterogeneidade dos tipos de solo e condições ambientais de cada região. Optamos por mantê-los para preservar a variância real do fenômeno e a fidelidade ao ambiente mapeado.

## Altura por tipo florestal

Figura 2: Distribuição de altitude por cobertura florestal: presença de outliers naturais devido à heterogeneidade dos solos.

<!-- image -->

### 0.7 Implicações para a modelagem

--- CHUNK 66 ---
<!-- image -->

### 0.7 Implicações para a modelagem

Os achados da análise exploratória impõem diretrizes estritas para a arquitetura de modelagem, visando garantir robustez e equidade nas predições:

--- CHUNK 67 ---
- Necessidade de Algoritmos Sensíveis à Escala: Como identificamos a necessidade de utilizar o StandardScaler para normalizar o intervalo das variáveis numéricas, o modelo escolhido deve ser compatível com dados escalonados. Algoritmos baseados em gradiente ou distâncias serão priorizados pela sua capacidade de extrair padrões de dados normalizados de forma eficiente.

--- CHUNK 68 ---
- Abordagem Robusta ao Desbalanceamento: A disparidade volumétrica entre as classes minoritárias e majoritárias inviabiliza o uso de modelos simplistas. Implica-se, portanto, a obrigatoriedade de integrar ao pipeline de modelagem técnicas como class weights ou algoritmos de ensemble , que possuem mecanismos nativos de tratamento de distribuições assimétricas.

--- CHUNK 69 ---
- Seleção de Métricas Orientada ao Negócio: Dado que a acurácia é uma métrica enviesada para este conjunto de dados, todas as etapas de busca de hiperparâmetros serão guiadas estritamente pelo F1-Score

--- CHUNK 70 ---
Macro . Isso garante que o processo de otimização priorize o equilíbrio de sensibilidade entre todas as tipologias florestais, incluindo as raras.

- Validação Cruzada Estratificada: Adotaremos a Stratified K-Fold Cross-Validation para assegurar que cada subconjunto de treino e teste mantenha a proporção real de todas as 7 classes, garantindo que o modelo seja validado de forma estatisticamente justa mesmo para as classes com poucos representantes.

## Fase 3: Data Preparation

--- CHUNK 71 ---
## Fase 3: Data Preparation

### 0.8 Partição treino, validação e teste

Para garantir a robustez na seleção do melhor algoritmo e evitar o overfitting durante o ajuste de hiperparâmetros, adotamos uma estratégia de partição de dados em três conjuntos distintos, totalizando 581.012 observações:

--- CHUNK 72 ---
- Conjunto de Treino (50%): Utilizado para o treinamento dos modelos e para o aprendizado dos padrões básicos de cada algoritmo.
- Conjunto de Validação (25%): Dedicado exclusivamente à comparação de desempenho e ao ajuste fino de hiperparâmetros. Este conjunto atuou como um "filtro de qualidade", garantindo que os modelos fossem avaliados em dados não vistos durante o treinamento, permitindo a seleção da melhor configuração para cada variante.

--- CHUNK 73 ---
- Conjunto de Teste (25%): Reservado para a etapa final de inferência, garantindo uma avaliação imparcial e realista da capacidade de generalização do modelo campeão.

--- CHUNK 74 ---
Essa segregação foi fundamental, pois possibilitou a experimentação intensiva com diversos pipelines de pré-processamento, assegurando que a escolha do algoritmo final não estivesse viciada pela otimização excessiva em um único conjunto de validação.

### 0.9 Pipeline baseline

--- CHUNK 75 ---
### 0.9 Pipeline baseline

O pipeline baseline foi estruturado para estabelecer uma base comparativa sólida e reprodutível. Para garantir a convergência dos algoritmos, aplicamos o StandardScaler em todas as variáveis numéricas, mitigando o impacto das diferentes escalas de magnitude nas predições.

--- CHUNK 76 ---
Conscientes do alto custo computacional imposto pelo volume total do dataset (aproximadamente 290 mil instâncias no treino), adotamos uma estratégia de amostragem por redução. Selecionamos aleatoriamente 20% do conjunto de treino (cerca de 58 mil instâncias), mantendo a distribuição original das classes

--- CHUNK 77 ---
. Esta decisão técnica, pautada na eficiência operacional, permitiu a experimentação célere com modelos de alta complexidade como SVM, KNN, LVQ e MLP - sem comprometer a representatividade estatística dos dados.

--- CHUNK 78 ---
A escolha pela subamostragem foi fundamentada na priorização da capacidade de iteração e refinamento dos algoritmos, considerando que ganhos marginais de desempenho com a totalidade das instâncias não justificariam o custo temporal elevado no estágio atual de experimentação.

### 0.10 Variantes do conjunto de treino

--- CHUNK 79 ---
### 0.10 Variantes do conjunto de treino

Para a experimentação, estabelecemos um baseline inicial para validar a performance bruta dos modelos. Contudo, dado o desbalanceamento severo das classes - especialmente a Classe 4, que representa apenas 0,5% do dataset - observamos uma degradação significativa no desempenho e sinais de overfitting nas classes majoritárias.

--- CHUNK 80 ---
Por fim, observando que os modelos baseados em árvores de decisão demonstravam superioridade sistemática, testamos uma variante final: a utilização dos dados originais do baseline combinada com o parâmetro class weight . Esta estratégia permitiu que os algoritmos realizassem o balanceamento de forma nativa, penalizando erros em classes minoritárias durante o treinamento sem a necessidade de manipular o espaço amostral original. A Tabela 1 detalha esta evolução experimental.

--- CHUNK 81 ---
Em um primeiro movimento para mitigar esse viés, aplicamos a técnica de Undersampling . Entretanto, esta abordagem resultou em uma redução drástica da base de dados, sacrificando a capacidade de generalização e induzindo um desempenho insatisfatório. Para corrigir essa perda de informação, adotamos uma estratégia híbrida ( SMOTE + Undersampling ), padronizando cada classe com 7.000 instâncias

--- CHUNK 82 ---
. Esta técnica permitiu que diversos algoritmos recuperassem o desempenho e respondessem positivamente à diversidade dos dados.

--- CHUNK 83 ---
Tabela 1: Evolução das estratégias de balanceamento e suas justificativas teóricas.

--- CHUNK 84 ---
| Variante         | Técnica                 | Hipótese / Justificativa                                                                                                                            |
|------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|

--- CHUNK 85 ---
| v1_balanceamento | Undersampling           | Redução das classes majoritárias para forçar o modelo a priorizar a identifica- ção de classes minoritárias.                                        |
| v2_balanceamento | SMOTE + Under- sampling | Abordagem híbrida para compensar a perda de informação do v1 atra- vés da geração de dados sintéticos e reamostragem.                               |

--- CHUNK 86 ---
| v3_balanceamento | Class Weights           | Utilização de penalização assimétrica nos dados brutos, permitindo que o mo- delo aprenda padrões de classes raras sem distorcer o espaço amostral. |

--- CHUNK 87 ---
## Fase 4: Modeling

### 0.11 Espaços de busca utilizados

A estratégia de otimização foi estruturada em duas etapas utilizando RandomizedSearchCV , priorizando a eficiência computacional frente à exaustividade do Grid Search .

--- CHUNK 88 ---
- Exploração Global: Inicialmente, realizou-se uma busca ampla no espaço de hiperparâmetros para mapear regiões de convergência e identificar os candidatos mais promissores.

--- CHUNK 89 ---
- Refinamento Local: Em uma segunda chamada, restringimos o espaço de busca em torno dos melhores resultados encontrados anteriormente. Nesta fase, alguns parâmetros foram fixados enquanto outros foram explorados em intervalos mais granulares, permitindo o fi ne-tuning das arquiteturas de maior performance, como o XGBoost e o LightGBM do Pipeline 3 .

--- CHUNK 90 ---
Essa abordagem bifásica permitiu maximizar a capacidade preditiva dos modelos dentro de uma restrição de tempo de processamento, garantindo que as configurações finais não fossem apenas resultado de uma busca aleatória, mas sim de um processo iterativo de refinamento estatístico.

### 0.12 Resultados por algoritmo

### 0.0.1 Análise do Algoritmo K-Nearest Neighbors(KNN)

Figura 3: Comparação do F1-Score do KNN: Baseline vs Pipelines.

Comparação do F1-Score do KNN: Baseline vs Pipelines

Pipeline

--- CHUNK 91 ---
Comparação do F1-Score do KNN: Baseline vs Pipelines

Pipeline

<!-- image -->

A Figura 3 evidencia o comportamento do KNN frente às diferentes estratégias de pipeline . Analisando a performance, destacamos dois pontos críticos que ilustram os desafios de modelagem enfrentados:

--- CHUNK 92 ---
- Baseline e Overfitting Severo: O Baseline alcança a maior métrica de validação ( F 1 = 0 . 71 ), contudo, o gap de 0.15 em relação ao treino revela um cenário de overfitting severo. O modelo "decorou"as instâncias do conjunto de treinamento, o que compromete sua capacidade de generalização em cenários reais.

--- CHUNK 93 ---
- Pipeline 1 e Underfitting Severo: O Pipeline 1 apresenta uma queda acentuada no desempenho, com valores de F 1 ≈ 0 . 55 . Neste caso, a técnica de reamostragem aplicada introduziu um underfitting severo, tornando o modelo incapaz de capturar a complexidade da fronteira de decisão das classes, resultando em um desempenho insatisfatório tanto no treino quanto na validação.

--- CHUNK 94 ---
- Pipeline 2 (Confiabilidade): Embora apresente um desempenho absoluto inferior ao Baseline , o Pipeline 2 demonstra a maior estabilidade entre as etapas ( gap = 0 . 05 ). Sob uma ótica de engenharia, este modelo é o mais resiliente, priorizando a consistência das predições em detrimento de uma otimização agressiva que, como demonstrado, gera vulnerabilidades ao sobreajuste.

--- CHUNK 95 ---
### 0.0.2 Análise do Algoritmo: Learning Vector Quantization (LVQ

Figura 4: Comparação do F1-Score do LVQ: Baseline vs Pipelines.

Comparação do F1-Score do LVQ: Baseline vs Pipelines

Pipeline

<!-- image -->

--- CHUNK 96 ---
Pipeline

<!-- image -->

Aanálise do algoritmo LVQ (Figura 4) revela uma performance estagnada em todos os cenários testados, com valores de F1-Score situados entre 0.39 e 0.46. Diferente de modelos que demonstraram sensibilidade às técnicas de balanceamento, o LVQ apresentou um underfitting persistente em todas as configurações.

--- CHUNK 97 ---
- Insuficiência da Hipótese Algorítmica: Os resultados indicam que o problema não reside na qualidade ou na representatividade dos dados, mas na incapacidade da arquitetura LVQ em modelar a complexidade das relações não lineares presentes no dataset de cobertura florestal.

--- CHUNK 98 ---
- Estabilidade no Underfitting: A ausência de variação significativa entre os pipelines reforça que, para este algoritmo, a fronteira de decisão é muito rígida. O LVQ, ao depender de protótipos fixos, falha em capturar as sutilezas das classes minoritárias, independentemente de como os dados são balanceados.

--- CHUNK 99 ---
Conclui-se, portanto, que a escolha desta arquitetura é inadequada para o problema em questão. A persistência do underfitting frente a diferentes abordagens de preparação de dados valida o descarte desta classe de algoritmos em favor de métodos baseados em árvores, que demonstraram flexibilidade superior para o mapeamento do espaço amostral.

Figura 5: Comparação do F1-Score do SVM: Baseline vs Pipelines.

Comparação do F1-Score do SVM: Baseline vs Pipelines

Pipeline

<!-- image -->

--- CHUNK 100 ---
Pipeline

<!-- image -->

### 0.0.3 Análise do Algoritmo: Support Vector Machine (SVM)

Semelhante ao observado no LVQ, o algoritmo SVM demonstrou uma incapacidade crônica em adaptar-se à topologia dos dados. Como ilustrado na Figura 5, os resultados permaneceram estagnados em torno de F 1 ≈ 0 . 47 , independentemente da estratégia de pipeline ou técnica de balanceamento aplicada.

--- CHUNK 101 ---
- Underfitting e Rigidez do Hiperplano: O desempenho consistente abaixo de 0.50, combinado com a ausência de gap entre treino e validação, configura um caso clássico de underfitting . O modelo não possui a flexibilidade necessária para mapear as fronteiras de decisão complexas entre as 7 classes de cobertura florestal.

--- CHUNK 102 ---
- Limitação da Hipótese de Espaço de Margem: A falha do SVM reforça a conclusão de que este problema exige algoritmos capazes de realizar uma partição hierárquica e adaptativa do espaço amostral algo inerente a modelos baseados em árvores, mas que o SVM, mesmo com transformações de kernel, não logrou efetuar com sucesso para este volume de variáveis.

--- CHUNK 103 ---
Desta forma, assim como o LVQ, o SVM foi incapaz de entender os dados, pois sua estrutura de otimização de margens mostrou-se insuficiente para a dimensionalidade e a complexidade estatística do projeto.

