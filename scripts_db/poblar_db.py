import random
from src.data.db.models.planes import Plan
from src.data.db.models.descuentos import Descuentos
from src.data.db.models.socios import Socio
from src.socio.domain.dtos.socio_dto import SocioDto
from dotenv import load_dotenv
from typing import List
from src.data.cnn.conexiondb import ConexionDB

SOCIOS_CANT = 100
PRECIOS_PLANES = [2000, 3000, 4000]
DESCUENTOS_CANT = 3
DESCUENTOS_TIPO = ["absoluto", "porcentual"]

load_dotenv()

ConexionDB.get_db()
ConexionDB.dropdb()

planes_list = []
for precio in PRECIOS_PLANES:
    plan = Plan()
    plan.precio = precio
    plan.save()
    planes_list.append(plan.id)

descuentos_list = []
for tipo in DESCUENTOS_TIPO:
    for d in range(0, DESCUENTOS_CANT):
        descuento = Descuentos()
        descuento.tipo = tipo
        descuento.monto = (
            random.uniform(0.1, 0.5)
            if tipo == "porcentual"
            else random.randint(10, 600)
        )
        descuento.cantidad_aplicaciones = random.randint(10, 60)
        descuento.save()
        descuentos_list.append(descuento.id)

socios_list: List[SocioDto] = []
for x in range(0, SOCIOS_CANT):
    socio = Socio()
    socio.nombre = f"Nombre Test '{x}"
    socio.estado = "activo"
    socio.plan_id = planes_list[random.randint(0, len(planes_list) - 1)]
    socio.discount = random.sample(
        descuentos_list, random.randint(0, len(descuentos_list))
    )
    socio.fecha_vigencia = "2022-03-10"
    socios_list.append(socio)


socios_list = [Socio(**key._data) for key in socios_list]
Socio.objects.insert(socios_list)
