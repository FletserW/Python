times = ('Corinthians Santos Avaí América-MG Bragantino Atlético-MG São_Paulo Botafogo Internacional Coritiba '
         'Cuiabá Athletico-PR Palmeiras Flamengo Fluminense Goiás').split()
print('-=' * 25)
print(times)
print('-=' * 25)
print(f'{times[:5]}')
print('-=' * 25)
print(f'{times[-4:]}')
print('-=' * 25)
print(f'{sorted(times)}')
print('-=' * 25)
print(f"O Internacional está na {times.index('Internacional') + 1}° posição")

