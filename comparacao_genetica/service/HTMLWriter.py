import logging as log

def printHTML(count, arquivoSaidaLocation, colorHEX) :
    arquivoSaida = open(arquivoSaidaLocation,"w")
    log.debug("Inicio de output de informação para o arquivo : {} \nCom as informações : {}".format(arquivoSaidaLocation, count))
    arquivoSaida.write("<div>")
    __formatCount(count, arquivoSaida,colorHEX)
    arquivoSaida.close()
    log.debug("Finalizado de output de informação para o arquivo : {}".format(arquivoSaidaLocation))

def __formatCount(count, arquivoSaida, colorHEX) :
    i = 1
    for k in count:
        log.debug("Adicionando informações do count : {}".format(count[k]))
        transparencia = count[k]/max(count.values())
        arquivoSaida.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba("+colorHEX+", "+str(transparencia)+"')>"+k+"</div>")
        if i%4 == 0:
            arquivoSaida.write("<div style='clear:both'></div>")
        i+=1