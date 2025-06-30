from MiniGameEngine import GameObject

class Escudo(GameObject):
    def __init__(self,  x, y):
        super().__init__(x, y, "Recursos/Escudo.png", "Escudo")
        self.x = x
        self.y = y
        self.estado = "Activo"

    def onCollision(self, dt, gobj):
        if gobj.getTipo() == "Alien" and self.estado != "destruido":
            self.destroy()