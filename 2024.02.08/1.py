class Tetrahedron:
    def __init__(self, edge):
        self.edge = float(edge)
        
    def surface(self) -> float:
        return self.edge**2*3**(0.5)
        
    def volume(self) -> float:
        return self.edge**3*2**(0.5)/12

# >>> t1 = Tetrahedron(10)
# >>> t1.edge
# 10.0
# >>> t1.surface()
# 173.20508075688772
# >>> t1.volume()
# 117.85113019775793
# >>>
# >>> t1.edge = 50
# >>> t1.surface()
# 4330.127018922193
# >>> t1.volume()
# 14731.391274719741