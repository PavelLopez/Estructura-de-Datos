#fila de banco
#presentar saldo, retiro, deposito. 5 personas retiro de 500 deposito de 300, todos tiene un saldo igual a 1000
#enque
#peek
#size
#deque
#is_empty

def enque(lista,elemento):
    lista.append(elemento)

def deque(lista,lista2):
    enque(lista2,(lista[0]))
    lista.pop(0)

def peek(lista):
    return lista[0]

def is_empty(lista):
    if lista == []:
        return True
    else:
        return False
    
def size(lista):
    return len(lista)

def retiro(lista,lista2):
    r = lista[0]-lista2[0]
    deque(lista,lista2)
    print(peek(lista))
    enque(lista,r)
    print(peek(lista))


def deposito(lista,lista2):
    s = lista[0] + lista2[0]
    deque(lista,lista2)
    print(peek(lista))
    enque(lista,s)
    print(peek(lista))


saldo=[]
retiros=[]
depositos=[]

print(is_empty(saldo))
enque(saldo,1001)
enque(saldo,1002)
enque(saldo,1003)
enque(saldo,1004)
enque(saldo,1005)
print(saldo)

enque(retiros,500)
print(retiros)
retiro(saldo,retiros)
retiro(saldo,retiros)
retiro(saldo,retiros)
retiro(saldo,retiros)
retiro(saldo,retiros)

print(saldo)

enque(depositos,300)
print(depositos)
deposito(saldo,depositos)
deposito(saldo,depositos)
deposito(saldo,depositos)
deposito(saldo,depositos)
deposito(saldo,depositos)

print(saldo)
print(size(saldo))