class Relation:
    def __init__(self, rname, attrs):
        self.rname = rname
        self.attributes = attrs
    
    def __str__(self):
        return f"{self.rname}({self.attributes})"
