from src.data.cnn.conexiondb import ConexionDB
from src.descuento.service.descuento_service import DescuentoService
from src.pago.service.pago_service import PagoService
from src.socio.service.socio_service import SocioService


class ProcesarPagos:
    @staticmethod
    def run():
        try:
            socio_service = SocioService()
            socios_activos = socio_service.get_socios_activos()

            for socio in socios_activos:
                ProcesarPagos._run_procesar_pago(socio.id)

        except Exception as ex:
            print(ex)
        finally:
            ConexionDB.close()

    @staticmethod
    def _run_procesar_pago(id_socio):
        try:

            socio_service = SocioService()
            pago_service = PagoService()
            descuentos_service = DescuentoService()

            print("********************************************************")
            print("OBTENIENDO SOCIO")

            socio = socio_service.get_socio(id_socio)

            print("VALIDANDO DESCUENTOS DISPONIBLES")

            descuentos_aplicar = socio_service.get_descuentos_habilitados(id_socio)

            print("GENERANDO PAGO")

            pago = pago_service.add_pago(
                id_socio, socio.fecha_vigencia, descuentos_aplicar, socio.plan_id.precio
            )

            print("EXTENDIENDO VIGENCIA SOCIO")

            socio_service.extender_vigencia(id_socio)

            print("DESCONTANDO APLICACIONES EN DESCUENTO")

            descuentos_service.descontar_aplicacion(descuentos_aplicar)

        except Exception as ex:
            # TODO Implemetrar logging
            print(f"ERROR:: {ex}")
