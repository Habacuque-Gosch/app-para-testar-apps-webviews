#COLETA DE CORDENADAS DE COLETA PARA O MAPA
class Colet:
    def __init__(self, coleta):
        self.coleta = coleta

#COLETA DE CORDENADAS DE ENTREGA PARA O MAPA
class Entreg:
    def __init__(self, entrega):
        self.entrega = entrega

class InfoColeta_entrega:
     def __init__(self, cep_entrega, rua_entrega, bairro_entrega, cidade_entrega, estado_entrega, casa_entrega, cep_coleta, rua_coleta, bairro_coleta, cidade_coleta, estado_coleta, casa_coleta, itens, veiculo, distancia, total):
        self.cep_entrega = cep_entrega
        self.rua_entrega = rua_entrega
        self.bairro_entrega = bairro_entrega
        self.cidade_entrega = cidade_entrega
        self.estado_entrega = estado_entrega
        self.casa_entrega = casa_entrega
        self.cep_coleta = cep_coleta
        self.rua_coleta = rua_coleta
        self.bairro_coleta = bairro_coleta
        self.cidade_coleta = cidade_coleta
        self.estado_coleta = estado_coleta
        self.casa_coleta = casa_coleta
        self.veiculo = veiculo
        self.distancia = distancia
        self.total = total
        self.itens = itens