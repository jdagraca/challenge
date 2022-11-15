import unittest

from src.descuento.domain.entity.descuento import DescuentoDomain


class TestValidarDescuentosDisponibles(unittest.TestCase):
    def test_validar_descuentos_disponibles(self):
        descuentos = self._object_descuento()
        resul = descuentos.validar_disponibilidad()
        self.assertEqual(resul, False)

    def _object_descuento(self):
        capitals = {"cantidad_aplicaciones": "0", "monto": "200", "tipo": "absoluto"}
        return DescuentoDomain.map_from_dict(capitals)
