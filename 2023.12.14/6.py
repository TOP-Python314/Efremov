def orth_triangle(*, cathetus1: float = None, 
                     cathetus2: float = None, 
                     hypotenuse: float = None) -> float | None:
    
    if (cathetus1 != None != cathetus2 and 
        hypotenuse == None):
            return (cathetus1**2 + cathetus2**2)**0.5
        
    if (cathetus1 != None != hypotenuse and 
        cathetus1 < hypotenuse and 
        cathetus2 == None):
            return (hypotenuse**2 - cathetus1**2)**0.5
            
    if (cathetus2 != None != hypotenuse and 
        cathetus2 < hypotenuse and 
        cathetus1 == None):
            return (hypotenuse**2 - cathetus2**2)**0.5
    else:
        return None

# >>> orth_triangle(cathetus1 = 3, cathetus2 = 4)
# 5.0

# >>> orth_triangle(cathetus2 = 5, hypotenuse = 7)
# 4.898979485566356

# >>> print(orth_triangle(cathetus1 = 3, cathetus2 = 4, hypotenuse = 7))
# None

# >>> print(orth_triangle())
# None

# >>> print(orth_triangle(cathetus1 = 18, hypotenuse = 12))
# None