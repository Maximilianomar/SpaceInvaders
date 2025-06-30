from MiniGameEngine import GameObject
import random
''''
Clase que representa el Alien del juego.
'''

class Alien(GameObject):
    aliens_destruidos = 0  # Contador global de aliens destruidos

    def __init__(self, x, y, velocidad):
        """
        Inicializa el alien.

        Args:
            x (int): Posición inicial en el eje X.
            y (int): Posición inicial en el eje Y.  
            velocidad: Velocidad de cada Aliens
            direccion: Direccion de los aliens 1 = derecha, -1 = izquierda
            bajada: Cantidad de Pixeles que baja 
            estado: activo/destruido        
        """
        super().__init__(x, y, "Recursos/Alien.png", "Alien")
        # Cada alien tiene una velocidad diferente
        self.velocidad_x = velocidad if velocidad is not None else random.uniform(80, 120) 
        self.direccion = 1  # 1 = derecha, -1 = izquierda
        self.bajada_y = 40  # Cantidad de píxeles que baja al llegar al borde
        self.x = x
        self.y = y
        self.estado = "Activo"

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

    def get_velocidad(self):
        return self.velocidad_x

    def set_velocidad(self, nueva_velocidad):
        self.velocidad_x = nueva_velocidad
    
    # ==========================
    # Lógica de juego (customer)
    # ==========================

    # Acción personalizada la destruccion
    def destruir(self):
        self.estado = "Destruido"
        
    # detecta las coliciones
    def onCollision(self, dt, gobj):
        if gobj.getTipo() == "Bullet" and self.estado != "Destruido":
            self.destruir()
            Alien.aliens_destruidos += 1  # Aumenta el contador
            print(f"💥 Alien destruido. Total: {Alien.aliens_destruidos} estado: {self.estado}")
            self.destroy()

        # Si choca con la nave, fin del juego
        if gobj.getTipo() == "SpaceShip":
            print("La nave ha sido alcanzada. ¡Los alienígenas invadieron la Tierra!")
            self.destroy()
            gobj.destroy()  # También destruye la nave
            # Detener el motor del juego        
            self._gw.exitGame()
      
    # actualiza la posicion del alien
    def onUpdate(self, dt):
        # Movimiento lateral
        self._x += self.velocidad_x * dt * self.direccion 

        # Condicional: si el alien es muy rápido
        # if self.velocidad_x > 100:
        #     print("⚡ Alien muy rápido!")

        # Si el alien llega al borde de la pantalla, invierte la dirección y baja una fila
        if self._x < 0 or self._x > self.getWorldWidth() - self.getWidth():
            self.direccion *= -1
            self._y += self.bajada_y
        
        # Actualiza la posición
        self.setPosition(self._x, self._y)        
        
        # Imprimir su posición actual
        print(self)

        # Fin del juego si llega al fondo
        if self._y + self.getHeight() >= self.getWorldHeight() - 80:
            print("⚠️ ¡Los alienígenas invadieron la Tierra!")
            self._gw.exitGame()
    
    # =====================
    # Método de impresión
    # =====================

    def __str__(self):
        return f"Alien → Posición: ({self._x}, {self._y}) | Estado: {self.estado} | Velocidad: {self.velocidad_x} | Estado: {self.estado}"