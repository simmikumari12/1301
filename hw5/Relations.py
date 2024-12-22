from Attribute import Attribute

class Relations:
    def __init__(self):
        self.relations = {}
    
    def add_relation(self, relation):
        self.relations[relation.rname] = relation
    
    def delete_relation(self, relation_name):
        if relation_name in self.relations:
            del self.relations[relation_name]
    
    def modify_relation(self, relation_name, action, attribute_details):
        relation = self.relations.get(relation_name)
        if relation:
            if action == 'a':
                name, atype, key = attribute_details.split(':')
                relation.attributes.add_attribute(Attribute(name, atype, key))
            elif action == 'd':
                relation.attributes.delete_attribute(attribute_details)
    
    def __str__(self):
        return '\n'.join(str(relation) for relation in self.relations.values())
