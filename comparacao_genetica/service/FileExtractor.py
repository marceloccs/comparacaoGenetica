import logging as log

def extract (fileFastaLocation) :
    entrada = open(fileFastaLocation).read()
    count = {}

    for i in ['A','T','C','G'] :
        for j in ['A','T','C','G'] :
            count[i+j] = 0

    entrada = entrada.replace("\n","")

    for k in range(len(entrada)-1):
        count[entrada[k]+entrada[k+1]] += 1

    log.debug("Extraido informação do arquivo : {} \nResultado da coleta : {}".format(fileFastaLocation, count))
    return count