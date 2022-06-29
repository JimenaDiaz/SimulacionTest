from schemas.simulacion_dis import Dispositivo



class Producer():
    def __init__(self):
        pass
    def create_event(self):
        numero = 4
        fake_db = []
        i = 0 
        while numero > i:
            evento = Dispositivo()
            fake_db.append(evento.dict())
            print(fake_db)
            i += 1