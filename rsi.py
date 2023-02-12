import pandas as pd
import numpy as np 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                      ############################################################                                                          #
#                                                                             INDICADOR RSI                                                                                  #
#               INDICADOR TECNICO RSI DE TRADING ALGORITMICO, CREADO POR FRANCISCO ALAS, PARA BOT DE TRADING ALGORITMICO BOTGUS   WWW.BOTGUS.COM                             #
#       RSI es un indicador técnico de análisis técnico que mide la fuerza relativa de los precios de cierre de un activo. Se usa para determinar si un activo está          #
#       sobrecomprado o sobrevendido y para identificar oportunidades de compra o venta.                                                                                     #
#                                                      ############################################################                                                          #
#                                                                   1.PARAMETROS DE INDICADOR RSI                                                                            #
#                                                      ############################################################                                                          #
#                       PARAMETROS: datos,venta_rsi,compra_rsi,rsi_periodo,ema_rsi,ema_mediamovil,ema_longitud,cruce_ma_anterior,habilita_cruce                              #
#   datos (dataframe) = datos historicos de las velas en formato: 'open', 'high', 'low', 'close','volume', estos datos tienen que venir de un dataframe.                     #
#   venta_rsi (int) = valor de banda de arriba de RSI, bandas en las que se mueve el RSI por defecto 30-70, siendo 30 banda de abajo y 70 banda de arriba.                   #
#   compra_rsi (int) = Valor de la banda de abajo de RSI, bandas en las que se mueve el precio por defecto 30-70, siendo 30 banda de abajo y 70 banda de arriba.             #
#   rsi_periodo (int) = Número de períodos para calcular el RSI.                                                                                                             #
#   ema_rsi (str) = media movil para RSI, esta puede ser ema o sma, media movil exponencial o media móvil simple                                                             #
#   ema_mediamovil (str) = MA de media movil, esta puede ser 'ema' o 'sma'.  media movil exponencial o media móvil simple  .                                                 #
#   ema_longitud (int) = Numero de períodos para calcular la media movil exponencial o la media movil simple.                                                                #
#   cruce_ma_anterior (str) = si queremos que compruebe si anteriormente se dio un cruce entre RSI Y MA en la direccion opuesta,                                             #
#   antes de dar el cruce final esperado entre RSI Y MA. esto llamado tambien doble cruce. los valores soportados 'si' o  'no'.                                              #
#   habilita_cruce (str) = Indica si vamos a usar el cruce  de RSI con la media movil, esto puede ser usado para evitar señales falsas. los valores soportados 'si' o  'no'. #
#                                                      ############################################################                                                          #
#                                                             2.RETORNO DE RESULTADOS DE LA FUNCION                                                                          #
#                                                      ############################################################                                                          #
#                                    EL INDICADOR RSI RETORNA LOS SIGUIENTES DATOS: rsi_valor, ma_valor, cruce, donde_sedio_elcruce                                          #
# rsi_valor = Valor de RSI.        RECOMENDACION MANEJARLO COMO FLOAT float(rsi_valor)                                                                                       #
# ma_valor = valor de media movil de RSI        RECOMENDACION MANEJARLO COMO FLOAT float(rsi_valor)                                                                          #
# cruce = determina si se dio el cruce o no   : devuelve cuatro valores : 'cruce_hacia_arriba', 'cruce_hacia_abajo', 'no_hay_cruce', 'no']                                   #
#     - 'cruce_hacia_arriba' = El valor de RSI es mayor al valor de la media movil.                                                                                          #
#     - 'cruce_hacia_abajo' = El valor de RSI es menor al valor de la media movil.                                                                                           #
#     - 'no_hay_cruce' = No se ha dado el cruce de RSI Y MA.                                                                                                                 #
#     - 'no' = valor que es devuelto cuando no se selecciono el cruce por medio de media movil.                                                                              #
# donde_sedio_elcruce = determina donde se dio el cruce de RSI con MA  : devuelve tres valores : 'fuera', 'dentro', 'no'                                                     #
#     - 'fuera' = el cruce se dio fuera de las bandas.                                                                                                                       #
#     - 'dentro' = el cruce se dio dentro de las bandas.                                                                                                                     #
#     - 'no' = valor que es devuelto cuando no se selecciono el cruce por medio de media movil.                                                                              #
#                                                      ############################################################                                                          #
#                                                               3.FORMA DE USO EJEMPLO USANDO MEDIA MOVIL                                                                    #
#                                                      ############################################################                                                          #
#                                   valorrsi,valormedia,cruce,donde=rsi_indicador(data,70,30,14,"sma","sma",14,"si","si")                                                    #
# Declaramos las variables para guardar los valores: valorrsi,valormedia,cruce,donde                                                                                         #
# valorrsi = Guardamos el valor de RSI.                                                                                                                                      #
# valormedia= Guardamos el valor de la media movil.                                                                                                                          #
# cruce= Guardamos el valor del cruce entre RSI y MA.                                                                                                                        #
# donde= Guardamos donde se dio el cruce si fuera o dentro de las bandas de RSI.                                                                                             #
# Ahora ya puedes llamar la funcion rsi_indicador(), para ver los datos enviados en los parametros y el orden ver 1.PARAMETROS DE INDICADOR RSI en la parte de arriba        #
#                                   valorrsi,valormedia,cruce,donde=rsi_indicador(data,70,30,14,"sma","sma",14,"si","si")                                                    #
#      mivalorrsi=float(valorrsi)                                                                                                                                            #
#      mivalorrsi=float(valormedia)                                                                                                                                          #
#      mivalorrsi=cruce                                                                                                                                                      #
#      mivalorrsi=donde                                                                                                                                                      #
#                                                      ############################################################                                                          #
#                                                               3.1 FORMA DE USO EJEMPLO USANDO SOLO RSI                                                                     #
#                                                      ############################################################                                                          #
# Si solo quiere devolver solo el valor de RSI se llama de la siguiente manera:                                                                                              #
# valorrsi,valormedia,cruce,donde=rsi_indicador(data,70,30,14,"sma","sma",14,"si","no")                                                                                      #
# mivalorrsi=float(valorrsi)                                                                                                                                                 #
# para ver los datos enviados en los parametros y el orden ver 1.PARAMETROS DE INDICADOR RSI en la parte de arriba                                                           #
#                                                      ############################################################                                                          #
#                                                                        4. FINAL                                                                                            #
#                                                      ############################################################                                                          #
#               No olvides instalar el modulo botgus de la siguiente manera: pip install botgus, para actualizar version: pip install botgus --upgrade                       #
#               luego de instalado el modulo puede llamarlo de la siguiente manera: botgus.rsi_indicador(data,70,30,14,"sma","sma",14,"si","si")                             #
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                               HASTA AQUI LA INFORMACION, NO OLVIDES VISITAR https://www.facebook.com/groups/bitcoinsvgrupo                                                 #
#    WWW.BOTGUS.COM             //#         FRANCISCO ALAS                                                                                                                   #
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def rsi_indicador(datos,venta_rsi,compra_rsi,rsi_periodo,ema_rsi,ema_mediamovil,ema_longitud,cruce_ma_anterior,habilita_cruce):
    #Calcular el valor de RSI
    fuente_datos = datos['close'].astype(float).diff()
    arriba = fuente_datos.clip(lower=0)
    abajo = -1 * fuente_datos.clip(upper=0)
    if ema_rsi == "ema":
        ma_arriba = arriba.ewm(com = rsi_periodo - 1, adjust=True, min_periods = rsi_periodo).mean()
        ma_abajo = abajo.ewm(com = rsi_periodo - 1, adjust=True, min_periods = rsi_periodo).mean()
    elif ema_rsi=="sma":
        ma_arriba = arriba.rolling(rsi_periodo).mean()
        ma_abajo = abajo.rolling(rsi_periodo).mean()
    rsi_media = ma_arriba / ma_abajo
    rsi_calculo_final=100 - (100/(1 + rsi_media))
    rsi_valor = rsi_calculo_final.iloc[-1]
    if habilita_cruce=='si':
        # Agregamos el cálculo de la media móvil simple o exponencial
        if ema_mediamovil == 'sma':
            ma_valores = rsi_calculo_final.rolling(ema_longitud).mean()
        elif ema_mediamovil == 'ema':
            ma_valores = rsi_calculo_final.ewm(span=ema_longitud).mean()
        # Agregamos el cálculo de la media móvil simple
        ma_valor = ma_valores.iloc[-1]
        # Agregamos el cálculo del cruce entre el RSI y la media móvil
        cruce = 'no_hay_cruce'
        if cruce_ma_anterior=='si':
            valor_rsi_anterior = rsi_calculo_final.iloc[-2]
            valor_ma_anterior = ma_valores.iloc[-2]
            if valor_rsi_anterior < valor_ma_anterior and rsi_valor > ma_valor:
                cruce = 'cruce_hacia_arriba'
            elif valor_rsi_anterior > valor_ma_anterior and rsi_valor < ma_valor:
                cruce = 'cruce_hacia_abajo'
        else:
            if rsi_valor > ma_valor:
                cruce = 'cruce_hacia_arriba'
            elif  rsi_valor < ma_valor:
                cruce = 'cruce_hacia_abajo'
        # Agregamos el cálculo de si el cruce se dio dentro o fuera de las bandas
        donde_sedio_elcruce = 'dentro'
        if (rsi_valor < compra_rsi or rsi_valor > venta_rsi) and (valor_rsi_anterior >= compra_rsi and valor_rsi_anterior <= venta_rsi):
            donde_sedio_elcruce = 'fuera'
    else:
        ma_valor='no'
        cruce='no'
        donde_sedio_elcruce='no'
    return rsi_valor, ma_valor, cruce, donde_sedio_elcruce
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                               FIN INDICADOR RSI                                                                            #
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
