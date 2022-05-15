class Carta:
    def __init__(self,nam,col,type,man,rar):
        self.nombre = nam
        self.color = col
        self.tipo = type
        self.mana = man
        self.rareza = rar

    def getCard(self):
        return self.nombre, self.color, self.tipo, self.mana, self.rareza
  
    def getName(self):
        return self.nombre

    def getColor(self):
        return self.color

    def getType(self):
        return self.tipo

    def getMana(self):
        return self.mana

    def getRarity(self):
        return self.rarity

    def setCard(self,nam,col,type,man,rar):
        self.nombre = nam
        self.color = col
        self.tipo = type
        self.mana = man
        self.rareza = rar
  
    def setName(self, nam):
        self.nombre = nam

    def setColor(self, col):
        self.color = col

    def setType(self, tipe):
        self.tipo = tipe

    def setMana(self, man):
        self.mana = man

    def setRarity(self, rar):
        self.rareza = rar