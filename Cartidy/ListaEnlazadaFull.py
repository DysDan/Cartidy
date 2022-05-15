from StackEnlazado import StackEnlazado

class ListaEnlazadaFull(StackEnlazado):
    #Lo que hereda con StackEnlazado: empty(), push(x), pop(x), top()
    #Se le añade: encolar(x), desencolar(x), bot(), search()
    def encolar(self,item):
        self.longitud += 1
        if self.empty():
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def desencolar(self):
        if self.empty():
            print("No se puede desencolar. Está vacía.")
        else:
            self.longitud -= 1
            valor = self.head.dato
            self.head = self.head.next
            return valor
    
    def bot(self):
        return self.tail.dato

    def search(self,text):
        m = self.head
        while m.next != None:
            if m.dato == text:
                return m
            else:
                m = m.next
        return None