from MiniGameEngine import GameObject


class Explotion(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, "Recursos/Explosion.gif", "Explosion")
        self._frame_count = 0
        self._max_frame_count = 20  # Número máximo de cuadros que la explosión será mostrada


    def onUpdate(self, dt):
        self._frame_count += 1
        if self._frame_count >= self._max_frame_count:
            self.destroy()