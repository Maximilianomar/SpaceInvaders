import time
from MiniGameEngine import GameObject
from Bullet import Bullet
import random


"""
    Clase que representa la Nave Espacial del juego.
"""
class SpaceShip(GameObject):
    def __init__(self, x, y, jugador=1):
        """
        Inicializa la Nave Espacial.

        Args:
            x (int): Posición inicial en el eje X.
            y (int): Posición inicial en el eje Y.
            jugador (int): Número de jugador (1 o 2)
        """
        super().__init__(x, y, "Recursos/SpaceShip.png", "SpaceShip")
        self._x = x
        self._y = y
        self._estado = "activo"
        self.lastBullet = time.time()
        self._puntuacion = 0  # Nueva propiedad: puntuación
        self.aparicion_x = random.uniform(10, 750)
        self.aparicion_y = random.uniform(10, 300)
        self.jugador = jugador  # Nuevo: número de jugador

    # =====================
    # Getters y Setters
    # =====================

    def get_x(self):
        return self._x

    def set_x(self, valor):
        self._x = valor

    def get_y(self):
        return self._y

    def set_y(self, valor):
        self._y = valor

    def get_estado(self):
        return self._estado

    def set_estado(self, estado):
        self._estado = estado

    def get_puntuacion(self):
        return self._puntuacion

    def set_puntuacion(self, valor):
        self._puntuacion = valor

    # ==========================
    # Lógica de juego (Customer)
    # ==========================

    def aumentar_puntuacion(self, valor):
        self._puntuacion += valor    

    def onUpdate(self, dt):
        """ Actualiza la nave espacial en cada fotograma """
        ww = self.getWorldWidth()
        w = self.getWidth()
        x = self.getX()
        y = self.getY()

        # Movimiento lateral según jugador
        if self.jugador == 1:
            if self.isPressed("Left"):
                x = max(w / 2, x - 4)
            elif self.isPressed("Right"):
                x = min(ww - w / 2, x + 4)
        elif self.jugador == 2:
            if self.isPressed("a"):
                x = max(w / 2, x - 4)
            elif self.isPressed("d"):
                x = min(ww - w / 2, x + 4)

        self.setPosition(x, y)
        self.set_x(x)
        self.set_y(y)

        # Acción personalizada de disparo
        self.disparar_laser(x, y)

    def onCollision(self, dt, gobj):
        if gobj.getTipo() == "PowerUp":
            gobj.activar_efecto(self) 
        
    # =====================
    # Método personalizado
    # =====================
    def disparar_laser(self, x, y):
        """ Dispara un láser hacia arriba si ha pasado el tiempo de recarga """
        if (self.jugador == 1 and self.isPressed("Up")) or (self.jugador == 2 and self.isPressed("w")):
            if time.time() - self.lastBullet > 0.3:
                Bullet(x, y - 30)
                self.lastBullet = time.time()
                self.aumentar_puntuacion(10)  # Se suma puntuación al disparar
                print(self)
        
    # =====================
    # Método de impresión
    # =====================
    def __str__(self):
        return (
            f"Nave espacial en posición ({self._x}, {self._y}) "
            f"con estado '{self._estado}' y puntuación {self._puntuacion}"
        )
