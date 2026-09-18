# Modelagem Matemática e Inteligência Artificial
## Problemas revisitados, novas perguntas — repositório computacional

[![DOI](https://zenodo.org/badge/1376408108.svg)](https://doi.org/10.5281/zenodo.22837930)

Este repositório acompanha o livro **Modelagem Matemática e Inteligência Artificial: problemas revisitados, novas perguntas**, de **Rodney Carlos Bassanezi** e **João de Deus Mendes da Silva**.

A proposta do material computacional é trabalhar em três movimentos:

1. **Reproduzir** resultados apresentados no livro.
2. **Perturbar** parâmetros, configurações e hipóteses.
3. **Investigar** novas perguntas.

> Uma simulação implementa uma regra. Ela não decide, por si só, se essa regra representa adequadamente a realidade nem se um valor numérico constitui um ótimo provado.

## Repositório e versão arquivada

- GitHub: https://github.com/jdmsilva/modelagem-matematica-ia
- DOI da versão associada ao livro: https://doi.org/10.5281/zenodo.22837931
- DOI geral do software, válido para acompanhar versões futuras: https://doi.org/10.5281/zenodo.22837930

A versão arquivada correspondente à edição do livro deve ser citada pelo DOI específico:

**Bassanezi, Rodney Carlos; da Silva, João de Deus Mendes. _Modelagem Matemática e Inteligência Artificial — Repositório Computacional_. Versão 1.0.0. Zenodo, 2026. DOI: 10.5281/zenodo.22837931.**

## Instalação

```bash
python -m venv .venv
pip install -r requirements.txt
```

Defina `PYTHONPATH` apontando para `src/`.

Linux/macOS:

```bash
export PYTHONPATH="$PWD/src"
```

PowerShell:

```powershell
$env:PYTHONPATH="$PWD/src"
```

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

## Notebooks

A pasta `notebooks/` contém roteiros didáticos curtos para os capítulos:

- `cap01_macas.ipynb`
- `cap02_03_empacotamento.ipynb`
- `cap04_inversos.ipynb`

## Reprodutibilidade

Sempre registre:

- versão do código;
- parâmetros;
- semente aleatória, quando houver;
- origem dos dados;
- critério de parada;
- status do resultado.

Para os resultados computacionais, recomendamos distinguir explicitamente:

- `provado`
- `melhor_conhecido`
- `construcao`
- `experimento`

## Sobre `p = 0.290215`

Esse valor aparece no capítulo das maçãs como **valor de referência**. O módulo `modelagem_ia.fcc` inclui a função `calibrate_p`, que permite recalibrar `p` explicitamente a partir de um foco inicial, horizonte temporal e fração-alvo.

## Citação

Para citar a versão computacional associada ao livro:

```text
Bassanezi, Rodney Carlos; da Silva, João de Deus Mendes.
Modelagem Matemática e Inteligência Artificial — Repositório Computacional.
Versão 1.0.0. Zenodo, 2026.
DOI: 10.5281/zenodo.22837931
```

O arquivo `CITATION.cff` permite que o GitHub e outros serviços apresentem automaticamente a forma de citação.

## Licença

O código é distribuído sob licença MIT.
