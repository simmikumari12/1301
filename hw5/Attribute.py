class Attribute:
    def __init__(self, an, at, ky):
        self.aname = an  # Attribute name
        self.atype = at  # Attribute type
        self.key = ky    # Is it a key? (y or n)
    
    def __str__(self):
        key_str = "KEY" if self.key == 'y' else ""
        return f"{self.aname}:{self.atype}:{key_str}".strip(':')
