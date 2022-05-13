from Nodo import Nodo

class ListaEnlazada(): #Clase lista enlazada
    def __init__(self):  #Crearla, cabeza y cola vacias
        self.head = None
        self.tail = None

    def empty(self): #Si está vacío
        if self.head == None:
            return True
        else:
            return False

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
