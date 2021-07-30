class Partidos():
    nombre_partido = ''
    fecha_hora = ''
    fecha = ''
    hora = ''
    url_thumbnail = ''
    url = ''
    competencia = ''

    def __init__(self, nombre_partido,fecha_hora,fecha,hora, url_thumbnail, url, competencia):
        self.nombre_partido = nombre_partido
        self.fecha_hora = fecha_hora
        self.fecha = fecha
        self.hora = hora
        self.url_thumbnail = url_thumbnail
        self.url = url
        self.competencia = competencia

    def asdict(self):
        return {
            'partido': self.nombre_partido,
            'fecha_hora': self.fecha_hora,
            'fecha': self.fecha,
            'hora': self.hora,
            'url thumbnail': self.url_thumbnail,
            'url': self.url,
            'competencia': self.competencia
        }
