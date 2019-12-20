puntos = []

def fuerza_bruta():
    global puntos
    
    if len(puntos) < 2:
        print('Son necesarios 2 o más puntos')
    else:
        # sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
        
        for origen in puntos:
            distancia_menor = 100000
            punto = (0, 0)
            for destino in puntos:
                if origen != destino:
                    x1 = origen[0]
                    y1 = origen[1]
                    
                    x2 = destino[0]
                    y2 = destino[1]
                    
                    distancia = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
                    
                    if distancia < distancia_menor:
                        distancia_menor = distancia
                        punto = destino
                        
            x1 = origen[0]
            y1 = origen[1]
                    
            x2 = punto[0]
            y2 = punto[1]
            
            stroke(255)
            strokeWeight(1)
            line(x1, y1, x2, y2)        
                    
def setup():
    size(500, 500)  
    background(0)
    
def draw():    
    global puntos
    
    if mousePressed:
        r = int(random(256))
        g = int(random(256))
        b = int(random(256))
        
        stroke(r, g, b)
        strokeWeight(8)
        
        x = int(random(500))
        y = int(random(500))
        
        point(x, y)
        punto = (x, y)
        puntos.append(punto)

        delay(100)
        
def keyReleased():
    global puntos

    if key == 'p':
        print(puntos)  
    elif key == 'c':
        clear() 
        del puntos[:]
    elif key == 'f':
        fuerza_bruta()
    
    
    
