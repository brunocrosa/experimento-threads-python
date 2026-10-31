import threading
import time

# 9 tarefas simuladas, com tempos diferentes de espera (E/S)
tarefas = [
    ("Consulta ao sensor", 1.0),
    ("Leitura do banco de dados", 2.0),
    ("Envio do relatório", 1.5),
    ("Consulta à API", 1.2),
    ("Leitura de arquivo", 0.8),
    ("Consulta de temperatura", 1.1),
    ("Gravação no banco de dados", 1.7),
    ("Envio de notificação", 0.9),
    ("Backup de dados", 1.4)
]

resultados = []
lock = threading.Lock()


def executar_tarefa(nome, duracao):
    print(f"[{threading.current_thread().name}] "
          f"Iniciou: {nome} ({duracao:.1f} s)")

    time.sleep(duracao)

    print(f"[{threading.current_thread().name}] "
          f"Finalizou: {nome}")

    with lock:
        resultados.append(f"{nome}: concluída")


# PRÁTICA 1: EXECUÇÃO SEQUENCIAL
print("\n=== EXECUÇÃO SEQUENCIAL ===")
resultados.clear()

inicio = time.perf_counter()

for nome, duracao in tarefas:
    executar_tarefa(nome, duracao)

tempo_sequencial = time.perf_counter() - inicio

print(f"Tempo sequencial: {tempo_sequencial:.2f} s")
print(f"Total de resultados: {len(resultados)}")


# PRÁTICA 2: EXECUÇÃO COM 9 THREADS
print("\n=== EXECUÇÃO COM 9 THREADS ===")
resultados.clear()
threads = []

inicio = time.perf_counter()

for nome, duracao in tarefas:
    thread = threading.Thread(
        target=executar_tarefa,
        args=(nome, duracao)
    )
    threads.append(thread)
    thread.start()

# Espera todas as threads terminarem
for thread in threads:
    thread.join()

tempo_threads = time.perf_counter() - inicio

print(f"Tempo com 9 threads: {tempo_threads:.2f} s")
print(f"Total de resultados: {len(resultados)}")

# Comparação de desempenho
if tempo_threads > 0:
    razao = tempo_sequencial / tempo_threads
    economia = (1 - tempo_threads / tempo_sequencial) * 100

    print(f"Razão de tempos: {razao:.2f}x")
    print(f"Redução do tempo: {economia:.1f}%")
