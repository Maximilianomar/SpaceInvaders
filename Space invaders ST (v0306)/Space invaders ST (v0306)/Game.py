from MiniGameEngine import GameWorld
from SpaceShip import SpaceShip
from Alien import Alien
from Escudo import Escudo

import random

class Game(GameWorld):    
    def __init__(self, dificultad, nombres=None, num_jugadores=1):
        super().__init__(800, 600, title=f"Space Invaders", bgpic="Recursos/Fondo.png")
        # Condicionales y configuración según dificultad
       
        config_dificultad={
            "1": {"aliens": 5, "velocidad_base": 100, "incremento": 10},
            "2": {"aliens": 7, "velocidad_base": 150, "incremento": 20},
            "3": {"aliens": 10, "velocidad_base": 200, "incremento": 30}
        }
        config = config_dificultad.get(dificultad, config_dificultad["1"])
        
        cantidad_aliens = config["aliens"]
        velocidad_base = config["velocidad_base"]
        incremento = config["incremento"]
        
        self.nombres = nombres if nombres else ["Jugador 1", "Jugador 2"]
        self.num_jugadores = num_jugadores
        self.puntajes = [0, 0]
        self.labels_puntaje = []
        # Crear naves según el número de jugadores
        if num_jugadores == 2:
            self.nave1 = SpaceShip(500, 540, jugador=1)  # Jugador 1 a la derecha
            self.nave2 = SpaceShip(300, 540, jugador=2)  # Jugador 2 a la izquierda
        else:
            self.nave1 = SpaceShip(400, 540, jugador=1)
            self.nave2 = None
        # Labels de nombre y puntaje
        self.label_nombre1 = self._canvas.create_text(120, 20, text=f"{self.nombres[0]}: 0", fill="white", font=("Arial", 16, "bold"))
        if num_jugadores == 2:
            self.label_nombre2 = self._canvas.create_text(680, 20, text=f"{self.nombres[1]}: 0", fill="white", font=("Arial", 16, "bold"))
        
        # Crear aliens usando un bucle
        for i in range(cantidad_aliens):
            x = 100 + i * 70
            velocidad = velocidad_base + i * incremento
            Alien(x, 50, velocidad=velocidad)
 
 
        self.escudos = [
            Escudo(200, 400),
            Escudo(400, 400),
            Escudo(600, 400)
        ]



    def onUpdate(self, dt):
        fps = round(1 / dt, 1) 
        if self.isPressed("Escape"):
            self.exitGame()
        # Actualizar puntajes en pantalla
        p1 = self.nave1.get_puntuacion() if self.nave1 else 0
        self._canvas.itemconfig(self.label_nombre1, text=f"{self.nombres[0]}: {p1}")
        if self.num_jugadores == 2 and self.nave2:
            p2 = self.nave2.get_puntuacion()
            self._canvas.itemconfig(self.label_nombre2, text=f"{self.nombres[1]}: {p2}")

