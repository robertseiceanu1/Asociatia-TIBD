class Repository:
    def __init__(self, entities_list):
        self.__entities_list = entities_list

    def find_position(self, entity):
        for i in range(len(self.__entities_list)):
            if self.__entities_list[i] == entity:
                return i
        return None

    def find(self, entity):
        for i in range(len(self.__entities_list)):
            if self.__entities_list[i] == entity:
                return self.__entities_list[i]
        return None

    def add(self, entity):
        position = self.find_position(entity)
        if position is not None:
            raise Exception("Entity already exists!")
        self.__entities_list.append(entity)

    def delete(self, entity):
        position = self.find_position(entity)
        if position is None:
            raise Exception("Entity does not exist!")
        del self.__entities_list[position]

    def get_all(self):
        return self.__entities_list
