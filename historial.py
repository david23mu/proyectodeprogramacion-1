class Historial(Cita, Stack):
    def __init__(self):
        self.historial = []
        self.historial.append(Cita.__init__(nombre)) 
        self.historial.append(Cita.__init__(apellido))
        self.historial.append(Cita.__init__(edad))
        self.historial.append(Cita.__init__(fecha))
        self.historial.append(Cita.__init__(enfermedad))
        self.historial.append(Cita.__init__(receta))
        return self.historial
