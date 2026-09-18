# Modelagem Matemática e Inteligência Artificial
## Problemas revisitados, novas perguntas — repositório computacional

Material suplementar ao livro de **Rodney Carlos Bassanezi** e **João de Deus Mendes da Silva**.

A organização segue três movimentos: **Reproduzir — Perturbar — Investigar**.

## Instalação
```bash
python -m venv .venv
pip install -r requirements.txt
```
Defina `PYTHONPATH` apontando para `src/`.

## Programas
- Cap. 1: `01` a `06` — logística, camadas, FCC, contágio, posição e robustez.
- Cap. 2: `07` — cinco primeiros empacotamentos no cubo.
- Cap. 3: `08` e `09` — busca heurística e grafo de contatos.
- Cap. 4: `10` a `14` — problema inverso, tetraedro, esfera, recipientes e areia.

## Reprodutibilidade
Registre versão, parâmetros, semente, origem dos dados, critério de parada e status do resultado (`provado`, `melhor_conhecido`, `construcao`, `experimento`).

## Observação sobre p=0.290215
É mantido como valor de referência do capítulo. O módulo `modelagem_ia.fcc` fornece `calibrate_p` para recalibração explícita.

## Publicação
Antes de publicar o livro: criar GitHub, release `v1.0.0`, arquivar no Zenodo e substituir os placeholders em `CITATION.cff`.
