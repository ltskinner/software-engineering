
class DataBase(object):
    """Subsystem"""
    def insert(self, table, data):
        return "OK"

    def query(self, query):
        return [[], []]


class DataTap(object):
    """Subsystem"""
    def aggregate_data(self):
        return [['01', "ok we have an article"]]


class EntityExtractor(object):
    """Subsystem"""
    def __init__(self):
        self.model = "THE MODEL"

    def extract_entities(self, data):
        return [['too', 'easayy']]


class DataSystem(object):
    """Facade"""
    def __init__(self):
        self.database = DataBase()
        self.source = DataTap()
        self.entity_model = EntityExtractor()

    def get_todays_data(self):
        data = self.source.aggregate_data()
        entities = self.entity_model.extract_entities(data)
        self.database.insert("docs", data)
        self.database.insert("entities", entities)

    def query(self, query):
        return self.database.query(query)


if __name__ == "__main__":

    system = DataSystem()
    system.get_todays_data()

    data = system.query("SELECT * FROM docs")

    print(data)
