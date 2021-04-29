import random
from dataclasses import dataclass, field
import uuid
from typing import Dict
from models.model import Model
from common.database import Database
from common import score_calc

@dataclass
class Card(Model):
    collection: str = field(init=False, default="cards")
    cpf: int
    income: float
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)


    def json(self) -> Dict:
        return {
            "_id": self._id,
            "cpf": self.cpf,
            "income": self.income,
            "score": score_calc(self.income)[0],
            "credit": score_calc(self.income)[1]
        }

    @classmethod
    def get_by_cpf(cls, cpf_num: int) -> "Card":
        return cls.find_one_by("cpf", cpf_num)


