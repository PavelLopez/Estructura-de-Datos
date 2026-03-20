#Desarrollio de un programa en python quesimule una cola de 
# tamannio 5 para gestionar turnos de atención.

class ColaCircular:
    def __init__(self,capacidad):
        self.capacidad = capacidad
        self.cola = [None]*capacidad
        self.frente = -1
        self.final = -1

    def is_empty(self):
        return self.frente == -1
    
    def is_full(self):
        return (self.final + 1)%self.capacidad == self.frente
    
    def in_que(self,dato):
        if self.is_empty():
            self.frente = 0
            self.final = 0
        else:
            self.final = (self.final+1)%self.capacidad

        self.cola[self.final]=dato

    def de_que(self):
        if self.is_empty():
            print("La cola esta vacia")
            return None
        
        dato = self.cola[self.frente]

        if self.frente == self.final:
            self.frente = -1
            self.final = -1
        else:
            self.frente = (self.frente + 1)%self.capacidad
        
        return dato
    
    def see_front(self):
        if self.is_empty():
            return None
        return self.cola[self.frente]
    
    def see(self):
        if self.is_empty:
            print("cola vacia")
            return
        
        elementos = []
        i= self.frente

        while True:
            elementos.append(self.cola(i))
            if i == self.final:
                break
            i=(i+1)%self.capacidad
        print("Cola",elementos)


laCola = ColaCircular(5)
laCola.in_que(1)

laCola.see_front
