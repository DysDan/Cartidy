from Nodo import Nodo
import Carta as Carta

class ListaEnlazada(): #Clase lista enlazada
    def __init__(self):  #Crearla, cabeza y cola vacias
        self.head = None
        self.tail = None

    def empty(self): #Si está vacío
        if self.head == None:
            return True
        else:
            return False

    def filter(self, search_id, search_by):
        head_c = self.head
        filtro = []
      
        if search_id == "Rareza": 
            for i in range(self.count):
                if Carta.getRareza() == search_by:
                    filtro.append(Carta)
                head_c = head_c.next
              
        if search_id == "Color":
            for i in range(self.count):
                if Carta.getColor() == search_by:
                      filtro.append(Carta)
                head_c = head_c.next
              
        if search_id == "Tipo":
              for i in range(self.count):
                  if Carta.getColor() == search_by:
                      filtro.append(Carta)
                  head_c = head_c.next
                
        return filtro

    def printLista(self):   #Print de lista
        if self.empty():    #Decir si está vacía
            print("La lista está vacía.")
        else:               #Si no, recorrerla toda
            temp = self.head    #Inicializar apuntador para recorrer
            lista = ""      #String donde se guarda lista
            while temp != None:
                lista += str(temp.dato) + " > "
                temp = temp.next
            print(lista)
