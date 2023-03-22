class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)
    def listarTareas(self):
<<<<<<< HEAD
        for tarea in self.tareas:
            if tarea.estaLista():
                print(f"La tarea {tarea.obtenerNombre()} está lista")
            
=======
       for tarea in self.tareas:
           if tarea.estaLista():
               print(f"[X] {tarea.obtenerNombre()}" )
          
>>>>>>> d42145ec5bee934a69c4c68624f65b27cb960cda
        