class EntityHelper:
    @staticmethod
    async def get_entities_attribute_map(entities, attribute_title):
        attributes_map = map(lambda entity: getattr(entity, attribute_title), entities)
        return attributes_map
