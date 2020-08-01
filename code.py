
class Casilla:
    def __init__(self, posX, posY, simbolo):
        self.posicionX = posX
        self.posicionY = posY
        self.simbolo = simbolo


    #def casillaAdyacente(self, tablero)

        #if (tablero[self.posicionX-1][self.posicionY]):
            #self.casillaLeft = tablero[self.posicionX-1][self.posicionY]

        #if (tablero[self.posicionX+1][self.posicionY]):
            #self.casilleRight = tablero[self.posicionX+1][self.posicionY]

        
        


        #self.casillaUp
        #self.casillaDown
        #self.casillaLeft
        #self.casilleRight




class Negra(Casilla):
    def __init__(self, num, posX, posY):
        super().__init__(posX, posY, num) #uso del _init_ de la clase padre
        self.numero = num #indica el numero de la casilla negra, sino, es NULL u otro valor indicando que no tiene numero

    def printNegra(self):
        print('La casilla negra tiene el numero: ', self.numero, 'en la posición: ', self.posicionX,self.posicionY)

class Blanca(Casilla):
    def __init__(self, ilum, posX, posY):
        super().__init__(posX, posY, 'B') #uso del _init_ de la clase padre
        self.ilum = False #como es la creación inicial del objeto, no esta iluminado
        self.ampolleta = False



class Board:
    def __init__(self, n):
        self.size = n
        self.tablero = [[0 for x in range(n)] for y in range(n)] #iniciar 2D array
    
    def createBoard(self, casilla):
        self.tablero[int(casilla.posicionX)-1][int(casilla.posicionY)-1] = casilla





        #Aca va el codigo para armar el tablero, junto con un array de las posiciones de donde van las negras
        #y se rellena el resto con casillas blancas
        print(str(self.tablero))

    def fillBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                if (self.tablero[i][j] == 0):
                    self.tablero[i][j] = Blanca(False, i, j)

    def printBoard(self):
        print(self.tablero)

    def printRealBoard(self):

        for i in range(self.size): #aca tuve que cambiar i por j y viceversa para que se viera bien el trablero
            for j in range(self.size): #y no se porque funciona así, hermanito auidame
                if (isinstance(self.tablero[j][i], Blanca)):
                    if (self.tablero[j][i].ilum is True):
                        if (self.tablero[j][i].ampolleta is True):
                            print('[ A ]', end = '')
                        else:
                            print('[ E ]', end = '')
                    else: 
                        print('[   ]', end = '')  #el end = '' es para que no haga print con salto de linea
                if (isinstance(self.tablero[j][i], Negra)):
                    print('[', self.tablero[j][i].numero,']', end = '')
            
            print('\n')
    def printRealBoardn(self):

        for i in range(self.size):
            for j in range(self.size):
                print('[', i, '', j, ']', end = '')
            
            print('\n')


    def ilumBoard1(self):

        for i in range(self.size):
            for j in range(self.size):
                if (isinstance(self.tablero[i][j], Negra)):
                    print('Probando')
                    self.negraFirstStep(self.tablero[i][j])

    def printCasilla(self, posX, posY):

        casilla = self.tablero[posX][posY]
        if (isinstance(casilla, Blanca)):
            print('Es una casilla blanca')
        if (isinstance(casilla, Negra)):
            print('Es una casilla negra')
            print('Su simbolo es: ', casilla.numero)

    def ilumNegras(self, casilla):

        x = int(casilla.posicionX)-1
        y = int(casilla.posicionY)-1


        print('Debug: casilla ', casilla.posicionX, ' ', casilla.posicionY)
        

        x = x+1

        

        while x < self.size and int(casilla.posicionX)-1>0:

            print('Debug2: casilla ', x+1, ' ', casilla.posicionY)
            if (isinstance(self.tablero[x][y], Blanca)):
                if (x==int(casilla.posicionX)):
                    self.tablero[x][y].ampolleta = True
                self.tablero[x][y].ilum = True
            else:
                break
            x = x+1
            print('Debug3: x actual es: ', x)


        x = int(casilla.posicionX)-1

        x = x-1
        while x >= 0:



            if (isinstance(self.tablero[x][y], Blanca)):
                if (x==int(casilla.posicionX)-2):
                    self.tablero[x][y].ampolleta = True
                self.tablero[x][y].ilum = True
                print('Casilla ', x, '', y, ' ilumina3')
            else:
                break
            x = x-1

        x = int(casilla.posicionX)-1
        y = int(casilla.posicionY)-1

        y=y+1
        while y < self.size:
            if (isinstance(self.tablero[x][y], Blanca)):
                if (y==int(casilla.posicionY)):
                    self.tablero[x][y].ampolleta = True

                self.tablero[x][y].ilum = True
                print('Casilla ', x, '', y, ' ilumina3')
            else:
                break
            y = y+1
            
        y = int(casilla.posicionY)-1
        y=y-1
        while y >= 0:
            if (isinstance(self.tablero[x][y], Blanca)):
                if (y==int(casilla.posicionY)-2):
                    self.tablero[x][y].ampolleta = True
                self.tablero[x][y].ilum = True
                print('Casilla ', x, '', y, ' ilumina3')
            else:
                break
            y = y-1
        
    def negraFirstStep(self, casilla):

       

        if (isinstance(casilla, Negra)):
            if (casilla.numero == '4'):
                print('Debug del 4')
                self.ilumNegras(casilla)
            if (casilla.numero == '3'):
                print('Debug del 3')
                if (self.negra3):
                    self.ilumNegras(casilla)
            #if (casilla.numero == '2'):
                #print('Debug del 3')
                #if (self.negra2):
                    #self.ilumNegras(casilla)
            

    def negra3(self, casilla):

        x = casilla.posicionX-1
        y = casilla.posicionY-1

        if ((isinstance(self.tablero[x-1][y], Negra) or isinstance(self.tablero[x+1][y], Negra) or isinstance(self.tablero[x][y+1], Negra) or isinstance(self.tablero[x][y-1], Blanca)) or not (self.tablero[x-1][y] or not self.tablero[x+1][y] or not self.tablero[x][y-1] or not self.tablero[x][y+1])):
            return True
        else:
            return False

    def negra2(self, casilla):

        if ((casilla.posicionX==self.size and casilla.posicionY==self.size) or (casilla.posicionX==1 and casilla.posicionY==1) or (casilla.posicionX==1 and casilla.posicionY==self.size) or (casilla.posicionX==self.size and casilla.posicionY==1)):
            return True
        else:
            return False


        



 
import sys

print ('AAAAAAAAA')

print ('Argument List: ', sys.argv[0]) #sys.argv[0] es el nombre del archivo, los siguientes [1]... son los argumentos

print('Ingrese la cantidad de filas y columnas iguales')

num = int(input())



print('Ingrese la casillas tengras que tiene el tablero')

black = int(input())

array_pos = list()

tablero = Board(int(num))

i = 0
for i in range(black):
    print('Ingrese la posicion en X de la casilla numero: ', (i+1))
    posX = input()

    print('Ingrese la posicion en Y de la casilla numero: ', (i+1))
    posY = input()

    print('Ingrese el numero de la casilla negra ', (i+1))
    black = input()

    if (black == ''):
        black = '■'

    n = Negra(black, posX, posY)

    n.printNegra()
    print('DEBUG')
    tablero.createBoard(n)
tablero.fillBoard()
tablero.printBoard()
tablero.printRealBoard()
tablero.printRealBoardn()


print('Ingrese la posicion en X de la casilla')
posX = input()

print('Ingrese la posicion en Y de la casilla')
posY = input()

tablero.printCasilla(int(posX)-1, int(posY)-1)


print('A continuación, se iluminaran las casillas con el primer paso')

tablero.ilumBoard1()

tablero.printBoard()
tablero.printRealBoard()
