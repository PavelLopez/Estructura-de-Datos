class ColaCircular:
    def __init__(self,capacidad):
        self.capacidad = capacidad
        self.cola = [None]#capacidad
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
            x=1