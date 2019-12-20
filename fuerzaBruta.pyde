def setup():
    size(500, 500)  
    background(0)
    
def draw():    
    if mousePressed:
        r = int(random(256))
        g = int(random(256))
        b = int(random(256))
        
        stroke(r, g, b)
        strokeWeight(4)
        
        x = int(random(500))
        y = int(random(500))
        
        point(x, y)

        delay(100)
        
        
    
    
    
