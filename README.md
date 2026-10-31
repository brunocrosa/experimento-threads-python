# Experimento: Execução Sequencial e Concorrente com Threads em Python

## Sobre o projeto

Este projeto apresenta um experimento desenvolvido em Python com o objetivo de comparar o desempenho da execução sequencial de tarefas com a execução concorrente utilizando threads.

Foram simuladas nove tarefas independentes, representando operações comuns em sistemas computacionais, como consultas a sensores, leitura e gravação em bancos de dados, consultas a APIs, leitura de arquivos, envio de notificações e backups.

## Objetivo

Demonstrar como a utilização de múltiplas threads pode reduzir o tempo total de execução de tarefas que envolvem operações de entrada e saída (E/S), permitindo que diferentes períodos de espera ocorram simultaneamente.

## Tecnologias utilizadas

- **Python 3.13.14**
- **threading:** criação e gerenciamento de threads.
- **time:** simulação de tempos de espera e medição do tempo de execução.
- **Visual Studio Code:** ambiente utilizado para desenvolvimento e execução do programa.

## Como funciona

O programa realiza duas etapas:

1. **Execução sequencial:** as nove tarefas são executadas individualmente, uma após a outra.
2. **Execução concorrente:** são criadas nove threads, uma para cada tarefa, permitindo que sejam executadas concorrentemente.

Ao final, o programa compara os tempos obtidos e apresenta a razão entre eles e a redução percentual do tempo de execução.

## Como executar

1. Instale o Python em seu computador.
2. Baixe ou clone este repositório.
3. Abra a pasta do projeto no Visual Studio Code ou em outro ambiente compatível.
4. Execute o seguinte comando no terminal:

```bash
python teste_threads.py
```

## Resultados obtidos

Na execução realizada, foram obtidos os seguintes resultados:

| Indicador | Resultado |
|---|---:|
| Quantidade de tarefas | 9 |
| Tempo sequencial | 11,61 segundos |
| Tempo com 9 threads | 2,00 segundos |
| Razão de tempos | 5,80 vezes |
| Redução do tempo | 82,7% |
| Tarefas concluídas | 9 em ambas as execuções |

## Conclusão

O experimento demonstrou que a utilização de threads pode proporcionar uma redução significativa no tempo de execução de tarefas que envolvem espera por operações de entrada e saída.

Neste cenário, a execução concorrente apresentou uma redução de aproximadamente 82,7% em comparação à execução sequencial.

É importante destacar que os tempos de espera foram simulados com a função `time.sleep()`. Portanto, o experimento demonstra os benefícios da concorrência em tarefas limitadas por operações de E/S, não necessariamente em atividades que exigem processamento intensivo da CPU.

---

**Projeto desenvolvido para fins acadêmicos e de estudo sobre concorrência e programação com threads em Python.**
