x = 0
y = 0

def setup():
    size(500, 500)  
    background(0)
    

def draw():
    global x
    global y
    
    stroke(255)
    strokeWeight(2)
    
    point(x, y)
    
    x = x + 5
    y = y + 5
    
    if x > 499:
        x = 0
        y = 0
        clear()
        
    
    
    
