class Attributes:
    def __init__(self):
        self.attributes = []
    
    def add_attribute(self, attribute):
        self.attributes.append(attribute)
    
    def delete_attribute(self, attribute_name):
        self.attributes = [attr for attr in self.attributes if attr.aname != attribute_name]
    
    def find_attribute(self, attribute_name):
        return next((attr for attr in self.attributes if attr.aname == attribute_name), None)
    
    def __str__(self):
        return ','.join(str(attr) for attr in self.attributes)
