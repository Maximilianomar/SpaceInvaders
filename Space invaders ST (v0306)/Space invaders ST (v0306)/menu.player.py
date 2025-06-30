import tkinter as tk
from Game import Game
from tkinter import messagebox

def lanzar_menu():
    app = MenuJuego(dificultad="1")
    app.mainloop()
    
class MenuJuego(tk.Tk):
    def __init__(self, dificultad="1", nombre_jugador=None):  
        super().__init__()
        self.dificultad = dificultad
        self.nombre_jugador = nombre_jugador
        self.num_jugadores = 1 
        self.title("SpaceInvader - Menu Principal")
        self.geometry("400x600")
        self.resizable(False, False)
        self.configure(bg="black")

        # El resto de los widgets (sin fondo negro)
        tk.Label(self, text="Ingrese su nombre jugador 1", font=("Arial", 16),
                 fg="black", bg=None).pack(pady=20)
        
        self.nombre_entry = tk.Entry(self, font=("Arial", 16), width=15)
        self.nombre_entry.pack(pady=10)
        
        tk.Label(self, text="Cantidad de jugadores", font=("Arial", 18), fg="black", bg=None).pack(pady=5)
        frame_jugadores = tk.Frame(self, bg=None)
        frame_jugadores.pack(pady=5)
        btn_1j = tk.Button(frame_jugadores, text="1 Jugador", width=10, command=lambda: self.seleccionar_jugadores(1))
        btn_1j.grid(row=0, column=0, padx=5)
        
        btn_2j = tk.Button(frame_jugadores, text="2 Jugadores", width=10, command=lambda: self.seleccionar_jugadores(2))
        btn_2j.grid(row=0, column=1, padx=5)

        self.label_nombre2 = tk.Label(self, text="Nombre Jugador 2", font=("Arial", 18), fg="black", bg=None)
        self.nombre2_entry = tk.Entry(self, font=("Arial", 18))
        

        tk.Label(self, text="Seleccione Dificultad", font=("Arial", 18),
                 fg="black", bg=None).pack(pady=5)
        
        self.dificultades = [
            {"nombre": "Fácil", "nivel": "1"},
            {"nombre": "Media", "nivel": "2"},
            {"nombre": "Difícil", "nivel": "3"},
        ]
        for dato in self.dificultades:
            tk.Button(self, text=dato["nombre"], width=20,
                      command=lambda lvl=dato["nivel"]:
                          self.iniciar_juego(dificultad=lvl)).pack(pady=5)
        
        tk.Button(self, text="Instrucciones", width=20, command=self.mostrar_intruciones).pack(pady=5)
        tk.Button(self, text="Créditos", width=20, command=self.mostrar_credito).pack(pady=5)
        tk.Button(self, text="Salir", width=20,
                  command=self.quit).pack(pady=20)

    def seleccionar_jugadores(self, cantidad):
        self.num_jugadores = cantidad
        if cantidad == 2:
            self.label_nombre2.pack(pady=10)
            self.nombre2_entry.pack(pady=10)
        else:
            self.label_nombre2.pack_forget()
            self.nombre2_entry.pack_forget()

    def mostrar_intruciones(self):
        instrucciones = (
            "Controles del juego:\n"
            "- Flechas izquierda/derecha: mover la nave\n"
            "- ESPACIO: disparar\n"
            "- ESC: salir del juego \n\n"
            "Objetivo:\n"
            "Destruye todos los aliens antes de que lleguen a la parte inferior"
        )
        messagebox.showinfo("Instrucciones", instrucciones)
        
    def mostrar_credito(self):
        creditos = (
            "Space Invaders - Versión Python\n"
            "Desarrollado por: Maximiliano Muñoz\n"
            "Framework: Tkinter + MinigameEngine" 
        )
        messagebox.showinfo("Créditos", creditos)
    
    def iniciar_juego(self, dificultad):
        nombre = self.nombre_entry.get().strip() or "Jugador 1"
        nombre2 = self.nombre2_entry.get().strip() or "Jugador 2" if self.num_jugadores == 2 else None
        if not nombre:
            messagebox.showwarning("Advertencia", "Por favor, ingrese el nombre del Jugador 1")
            return
        if self.num_jugadores == 2 and not nombre2:
            messagebox.showwarning("Advertencia", "Por favor, ingrese el nombre del Jugador 2")
            return
        self.destroy()
        juego = Game(dificultad, [nombre, nombre2] if self.num_jugadores == 2 else [nombre], self.num_jugadores)
        juego.gameLoop(60)
                         

if __name__ == "__main__":
    lanzar_menu()