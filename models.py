from db import db


class DeltaModel(db.Model):
    __tablename__ = "delta_model"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rep_dt = db.Column(db.DATE)
    delta = db.Column(db.Float(precision=2))

    def __init__(self, rep_dt: str, delta: float):
        self.rep_dt = rep_dt
        self.delta = delta

    def __str__(self):
        return {"id": self.id, "rep_dt": self.rep_dt, "delta": self.delta}

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save(self) -> None:
        db.session.add(self)
