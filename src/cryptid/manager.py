class Manager:
    def __init__(self):
        self.entities = {}
        self.components = {}

    def add_entity(self, entity):
        self.entities |= {entity, len(self.entities) + 1}
