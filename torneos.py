class Torneos():
    id_torneo_filtro = 0
    nombre_torneo = ''


    def __init__(self, id_torneo_filtro,nombre_torneo):
        self.id_torneo_filtro = id_torneo_filtro
        self.nombre_torneo = nombre_torneo

    def asdicts(self):
        return {
            'id_torneo': self.id_torneo_filtro,
            'nombre_torneo': self.nombre_torneo,
        }
