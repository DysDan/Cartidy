from re import M
from StackEnlazado import StackEnlazado

class ListaEnlazadaFull(StackEnlazado):
    #Lo que hereda con StackEnlazado: empty(), push(x), pop(x), top()
    #Se le añade: encolar(x), desencolar(x), bot(), search()
    #Si es del git y no tiene el insertarMitad, ya lo estoy haciendo
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
        if self.tail.dato == text:
            return self.tail
        m = self.head
        while m.next != None:
            if m.dato == text:
                return m
            else:
                m = m.next
        return None

    def searchMayor(self,text):
        if text <= self.head.dato:
            return "head"
        if text >= self.tail.dato:
            return self.tail
        m = self.head
        while m.next != None:
            if m.dato >= text and text <= m.next.dato:
                return m
            else:
                m = m.next
        return None