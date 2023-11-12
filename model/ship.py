class Ship:
    def __init__(
            self,
            helm_health,
            helm_max_health,
            hull_health,
            hull_max_health,
            npc,
            sail_health,
            sail_max_health,
            ship_name,
            document_id=0
    ):
        self._helm_health = helm_health
        self.helm_max_health = helm_max_health
        self._hull_health = hull_health
        self.hull_max_health = hull_max_health
        self._sail_health = sail_health
        self.sail_max_health = sail_max_health
        self.ship_name = ship_name
        self.npc = npc
        self.document_id = document_id

    # get needs to update through client, could do controller rather than through this
    # could pass in rest client and make the model do it itself

    def get_document_id(self):
        return self.document_id

    def set_document_id(self, id):
        self.document_id = id

    def get_helm_health(self):
        return self._helm_health

    def set_helm_health(self, hp):
        self._helm_health = self._helm_health + hp

    def get_hull_health(self):
        return self._hull_health

    def set_hull_health(self, hp):
        self._hull_health = self._hull_health + hp

    def get_sail_health(self):
        return self._sail_health

    def set_sail_health(self, hp):
        self._sail_health = self._sail_health + hp

    def get_health_string(self, string):
        if string == "helm":
            return self._helm_health
        elif string == "hull":
            return self._hull_health
        elif string == "sail":
            return self._sail_health
        else:
            raise ValueError("String isn't in model!")

    @staticmethod
    def from_dict(source):
        ship = Ship(
            source["helm_health"],
            source["helm_max_health"],
            source["hull_health"],
            source["hull_max_health"],
            source["npc"],
            source["sail_health"],
            source["sail_max_health"],
            source["ship_name"]
        )

        return ship

    def to_dict(self):
        return {
            "helm_health": self._helm_health,
            "helm_max_health": self.helm_max_health,
            "hull_health": self._hull_health,
            "hull_max_health": self.hull_max_health,
            "npc": self.npc,
            "sail_health": self._sail_health,
            "sail_max_health": self.sail_max_health,
            "ship_name": self.ship_name
        }

    def to_dict_filtered(self):
        return {
            "helm_health": self._helm_health,
            "helm_max_health": self.helm_max_health,
            "hull_health": self._hull_health,
            "hull_max_health": self.hull_max_health,
            "sail_health": self._sail_health,
            "sail_max_health": self.sail_max_health,
        }

    def __repr__(self):
        return f"Ship(\
        helm_health={self._helm_health}, \
        helm_max_health={self.helm_max_health}, \
        hull_health={self._hull_health}, \
        hull_max_health={self.hull_max_health}, \
        npc={self.npc}, \
        sail_health={self._sail_health}, \
        sail_max_health={self.sail_max_health}, \
        ship_name={self.ship_name}\
        )"
