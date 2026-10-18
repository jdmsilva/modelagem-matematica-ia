# Modelagem Matemática e Inteligência Artificial

## Problemas revisitados, novas perguntas — repositório computacional

Este repositório acompanha o livro *Modelagem Matemática e Inteligência Artificial: problemas revisitados, novas perguntas*, de **Rodney Carlos Bassanezi** e **João de Deus Mendes da Silva**.

A proposta do material computacional é trabalhar em três movimentos:

1. **Reproduzir** resultados apresentados no livro.
2. **Perturbar** parâmetros, configurações e hipóteses.
3. **Investigar** novas perguntas.

Uma simulação implementa uma regra. Ela não decide, por si só, se essa regra representa adequadamente a realidade nem se um valor numérico constitui um ótimo provado.

---

## Repositório e versão arquivada

**GitHub:**  
https://github.com/jdmsilva/modelagem-matematica-ia

**DOI da versão associada ao livro — v1.1.0:**  
https://doi.org/10.5281/zenodo.23369973

**DOI geral do software:**  
https://doi.org/10.5281/zenodo.22837930

A versão arquivada correspondente à edição do livro deve ser citada pelo DOI específico:

> Bassanezi, Rodney Carlos; da Silva, João de Deus Mendes.  
> *Modelagem Matemática e Inteligência Artificial — Repositório Computacional*.  
> Versão 1.1.0. Zenodo, 2026.  
> DOI: 10.5281/zenodo.23369973.

A versão **1.1.0** incorpora o **Laboratório Interativo — Modelagem Matemática e IA**.

---

## Instalação

Os programas numéricos foram escritos em Python.

Crie um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
pip install -r requirements.txt
```

Defina `PYTHONPATH` apontando para `src/`.

### Linux/macOS

```bash
export PYTHONPATH="$PWD/src"
```

### PowerShell

```powershell
$env:PYTHONPATH="$PWD/src"
```

O Laboratório Interativo não depende dessa instalação. Ele pode ser executado diretamente em um navegador moderno.

---

## Estrutura

- `cap01_macas/` — logística, camadas, FCC, contágio, posição do foco e robustez.
- `cap02_bolas_cubo/` — cinco primeiros empacotamentos no cubo.
- `cap03_depois_de_cinco/` — otimização heurística e grafos de contato.
- `cap04_problemas_inversos/` — cubo inverso, pilha tetraédrica, recipiente esférico, comparação de recipientes e copo de areia.
- `notebooks/` — roteiros didáticos.
- `dados/` — arquivos de exemplo.
- `src/` — funções comuns usadas pelos programas.
- `docs/` — apêndice computacional e guia rápido.
- `tests/` — testes de consistência de resultados centrais.
- `laboratorio_interativo/` — aplicativo HTML autocontido que integra os problemas do livro em uma interface exploratória.

---

## Programas

### Capítulo 1 — Uma maçã apodrece

- `01_logistica_macas.py`
- `02_camadas_macas.py`
- `03_rede_fcc_macas.py`
- `04_contagio_fcc.py`
- `05_posicao_foco.py`
- `06_robustez_fcc.py`

### Capítulo 2 — Bolas em uma caixa cúbica

- `07_bolas_cubo_1a5.py`

### Capítulo 3 — E depois de cinco bolas?

- `08_otimizacao_cubo.py`
- `09_grafo_contatos.py`

### Capítulo 4 — O problema ao contrário

- `10_problema_inverso_cubo.py`
- `11_pilha_tetraedrica.py`
- `12_esferas_na_esfera.py`
- `13_comparar_recipientes.py`
- `14_copo_areia.py`

---

## Laboratório Interativo

A pasta `laboratorio_interativo/` contém o aplicativo:

**Laboratório Interativo — Modelagem Matemática e IA**

Para executar, abra diretamente:

```text
laboratorio_interativo/index.html
```

O aplicativo é autocontido e não exige instalação de Python nem conexão com a internet.

O laboratório integra, em uma única interface:

- propagação da contaminação entre maçãs em uma rede FCC;
- comparação entre diferentes posições iniciais da maçã contaminada;
- variação do número inicial de maçãs contaminadas;
- idealização da maçã como esfera;
- exploração de problemas de empacotamento em uma caixa cúbica;
- problema inverso e comparação de recipientes;
- retorno ao problema concreto de dimensionamento de recipientes para maçãs.

O laboratório tem finalidade exploratória. Uma configuração obtida computacionalmente constitui uma construção ou evidência numérica, mas não substitui uma prova de otimalidade.

---

## Notebooks

A pasta `notebooks/` contém roteiros didáticos curtos para os capítulos:

- `cap01_macas.ipynb`
- `cap02_03_empacotamento.ipynb`
- `cap04_inversos.ipynb`

---

## Reprodutibilidade

Sempre registre:

- versão do código ou do aplicativo;
- parâmetros utilizados;
- semente aleatória, quando houver;
- origem dos dados;
- critério de parada ou número de repetições;
- status epistemológico do resultado.

Para os resultados computacionais, recomendamos distinguir explicitamente:

- `provado`
- `melhor_conhecido`
- `construcao`
- `experimento`

Essas categorias não são intercambiáveis.

Uma configuração obtida computacionalmente constitui evidência ou construção, mas não substitui uma prova de otimalidade.

---

## Sobre `p = 0.290215`

Esse valor aparece no capítulo das maçãs como **valor de referência**.

O módulo `modelagem_ia.fcc` inclui a função `calibrate_p`, que permite recalibrar `p` explicitamente a partir de um foco inicial, horizonte temporal e fração-alvo.

Assim, `p = 0.290215` não deve ser interpretado automaticamente como uma estimativa empírica universal do processo de deterioração.

---

## Citação

Para citar a versão computacional associada ao livro:

> Bassanezi, Rodney Carlos; da Silva, João de Deus Mendes.  
> *Modelagem Matemática e Inteligência Artificial — Repositório Computacional*.  
> Versão 1.1.0. Zenodo, 2026.  
> DOI: 10.5281/zenodo.23369973.

**DOI específico da versão 1.1.0:**  
https://doi.org/10.5281/zenodo.23369973

**DOI geral do software:**  
https://doi.org/10.5281/zenodo.22837930

O arquivo `CITATION.cff` permite que o GitHub e outros serviços apresentem automaticamente a forma de citação.

---

## Licença

O código é distribuído sob licença MIT.
