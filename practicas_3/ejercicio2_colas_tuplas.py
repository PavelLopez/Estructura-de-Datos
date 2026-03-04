from collections import deque
def enque(q: deque, elemento) -> None:
    q.append(elemento)

def dequeue(q: deque):
    return q.popleft()

def peek(q: deque):
    return q[0]

def is_empty(q: deque)-> bool:
    return not q

def size(q: deque) -> int:
    return len(q)

def aplicar_retiro(saldos: deque[int], monto: int, historial: deque[int]| None = None)-> None:
    saldo_original = dequeue(saldos)
    if historial is not None:
        enque(historial, saldo_original)

    nuevo_saldo = saldo_original - monto
    enque(saldos, nuevo_saldo)


def aplicar_deposito(saldos: deque[int], monto: int, historial: deque[int]| None = None)-> None:
    saldos_original = dequeue(saldos)
    
    if historial is not None:
        enque(historial, saldos_original)
    nuevo_saldo = saldos_original + monto
    enque(saldos, nuevo_saldo)

#Corrida#
saldos = deque()
historial_saldos = deque()
#solucion para que el historial no permanesca 
#historial_saldos = deque(maxlen=5)
#colocar el "historial_saldos = deque()" antes del fos para depositar


print(is_empty(saldos))

for _ in range(5):
    enque(saldos, 1000)

monto_retiro = 500

for _ in range(5):
    aplicar_retiro(saldos, monto_retiro, historial_saldos)


print("Historial(saldos antes del retiro)", list(historial_saldos))
print("Saldos despues de retiro", list(saldos))

monto_deposito = 300

for _ in range(5):
    aplicar_deposito(saldos, monto_deposito, historial_saldos)

print("Historial(saldos antes del deposito)", list(historial_saldos))
print("Saldos finales", list(saldos))

