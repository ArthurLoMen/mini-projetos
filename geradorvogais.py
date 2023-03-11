while True:
    nomes = (input('Digite seu nome: '))

    for letras in nomes:
        for vogais in letras:
            if vogais in 'qwertyuiopasdfghjklçzxcvbnm':
                print(vogais)
            