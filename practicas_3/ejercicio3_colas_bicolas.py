#mete al final de la lista
#tiene comportamiento para la tail
def enqueTail(lista,elemento):
    lista.append(elemento)
#saca de la cola al primero en la lista
#tiene el comportamiento para el head
def dequeHead(lista,lista2):
    enqueHead(lista2,(lista[0]))
    lista.pop(0)
#funciona pero esta hardcodeado
def dequeTail(lista,lista2):
    enqueTail(lista2,lista[-1])
    lista.pop()

def enqueHead(lista,elemento):
  lista.insert(0,elemento)

def peek(lista):
    return lista[0]

def is_empty(lista):
    if lista == []:
        return True
    else:
        return False
    
def size(lista):
    return len(lista)

def retiro_en_head(lista,lista2):
    r = lista[0]-lista2[0]
    dequeHead(lista,lista2)
    print(peek(lista))
    enqueHead(lista,r)
    print(peek(lista))


def deposito(lista,lista2):
    s = lista[0] + lista2[0]
    dequeTail(lista,lista2)
    print(peek(lista))
    enqueTail(lista,s)
    print(peek(lista))





saldo=[]
retiros=[]
depositos=[]

print(is_empty(saldo))
enqueTail(saldo,1001)
enqueTail(saldo,1002)
enqueTail(saldo,1003)
enqueTail(saldo,1004)
enqueTail(saldo,1005)
print(saldo)

enqueTail(retiros,500)
print(retiros)
retiro_en_head(saldo,retiros)
retiro_en_head(saldo,retiros)
retiro_en_head(saldo,retiros)
retiro_en_head(saldo,retiros)
retiro_en_head(saldo,retiros)

print(saldo)

enqueTail(depositos,300)
print(depositos)
deposito(saldo,depositos)
deposito(saldo,depositos)
deposito(saldo,depositos)
deposito(saldo,depositos)
deposito(saldo,depositos)

print(saldo)
print(size(saldo))