from datetime import datetime
import pytz

bogota_timezone=pytz.timezone("America/Bogota") # hora de bogota en base de datos de timezone
bogota_date=datetime.now(bogota_timezone)

print("Bogota: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

mexico_timezone=pytz.timezone("America/Mexico_City") # hora de bogota en base de datos de timezone
mexico_date=datetime.now(mexico_timezone)

print("Mexico: ", mexico_date.strftime("%d/%m/%Y, %H:%M:%S"))


caracas_timezone=pytz.timezone("America/Caracas") # hora de bogota en base de datos de timezone
caracas_date=datetime.now(caracas_timezone)

print("Caracas ", caracas_date.strftime("%d/%m/%Y, %H:%M:%S"))
