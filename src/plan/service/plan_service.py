from src.plan.domain.daos.plan_dao import PlanDao


class PlanService:
    def __init__(self):
        self._plan_dao = PlanDao()
        pass

    def get_plan(self, plan_id):
        plan = self._plan_dao.get_plan(plan_id)
        return plan
