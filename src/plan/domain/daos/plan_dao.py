from mongoengine import *

from src.data.cnn.conexiondb import ConexionDB
from src.data.db.models.planes import Plan
from src.plan.domain.dtos.plan_dto import PlanDto


class PlanDao:
    def __init__(self):
        self._db: connect = ConexionDB.get_db()

    def get_plan(self, pk) -> PlanDto:
        plan = Plan.objects.get(pk=pk)
        return PlanDto.map_from_orm(plan)
