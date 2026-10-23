import classe_porta
import msvcrt

while True:
    garagem = msvcrt.getch()
    porta = classe_porta.Porta_de_garagem(garagem)
    new_class = classe_porta.Salva_status()
    if garagem in (b'\x00', b'\xe0'):
        garagem = msvcrt.getch()
        if garagem == b'H':
            porta.estado = "ABERTO"
            porta.imprimir_status()
            new_class.salva_arquivo(porta)
            continue
        elif garagem == b'P':
            porta.estado = "FECHADO"
            porta.imprimir_status()
            new_class.salva_arquivo(porta)
            continue
        else:
            porta.estado = "ERRO!"
            porta.imprimir_status()
            new_class.salva_arquivo(porta)
            break
    break