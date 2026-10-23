import json
import os

class Porta_de_garagem:
    def __init__(self, estado):
        self.estado = estado
    def imprimir_status(self):
        print(f"Estatus da porta: {self.estado}\n")
class Salva_status:
    def salva_arquivo(self, param):
        dicionario = {"estatus": param.estado}
        lista = []
        lista.append(dicionario)
        with open("porta.json", "w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo, indent=4, ensure_ascii=False)