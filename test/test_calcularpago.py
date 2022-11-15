import unittest

from src.descuento.domain.dtos.descuento_dto import DescuentoDto
from src.pago.domain.entity.pago import PagosDomain


class TestCalCularPago(unittest.TestCase):
    def test_calcular_pago(self):
        pago_domain = PagosDomain()
        descuentos = self._object_descuentos()
        precio_plan = 6000.0
        resul = pago_domain.set_monto(descuentos, precio_plan)
        self.assertEqual(resul, precio_plan - 300)

    def _object_descuentos(self):
        descuentos_list = list()
        desc_1 = {"cantidad_aplicaciones": "1", "monto": "200", "tipo": "absoluto"}
        desc_2 = {"cantidad_aplicaciones": "1", "monto": "100", "tipo": "absoluto"}
        descuentos_list.append(DescuentoDto.map_from_dict(desc_1))
        descuentos_list.append(DescuentoDto.map_from_dict(desc_2))
        return descuentos_list


if __name__ == "__main__":
    unittest.main()
