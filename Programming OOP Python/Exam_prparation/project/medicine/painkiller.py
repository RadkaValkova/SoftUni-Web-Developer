from project.medicine.medicine import Medicine


class Painkiller(Medicine):
    default_health_increase = 20

    def __init__(self):
        super().__init__(health_increase=self.default_health_increase)