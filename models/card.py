from dataclasses import dataclass, field
import uuid
from typing import Dict
from models.model import Model
from common.score_calc import score_calc

@dataclass(eq=False)
class Card(Model):
    collection: str = field(init=False, default="creditcards")
    cpf: int
    income: float
    score: int
    credit: float
    approval: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)


    def json(self) -> Dict:
        return {
            "_id": self._id,
            "cpf": self.cpf,
            "income": self.income,
            "score": self.score,
            "credit": self.credit,
            "approval": self.approval
        }

    @classmethod
    def get_by_cpf(cls, cpf_num: int) -> "Card":
        return cls.find_one_by("cpf", cpf_num)


