import sys
from Relation import Relation
from Relations import Relations
from Attributes import Attributes
from Attribute import Attribute

def load_schema(file_name):
    relations = Relations()
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            relation_name = parts[0]
            attributes = Attributes()
            for attr in parts[1:]:
                aname, atype, key = attr.split(':')
                attributes.add_attribute(Attribute(aname, atype, key))
            relation = Relation(relation_name, attributes)
            relations.add_relation(relation)
    return relations

def main():
    if len(sys.argv) < 2:
        print("Please provide the schema file as argument.")
        sys.exit(1)

    schema_file = sys.argv[1]
    relations = load_schema(schema_file)
    
    while True:
        print("\ni. DEFINE RELATION SCHEME")
        print("m. MODIFY RELATION SCHEME")
        print("d. DELETE RELATION SCHEME")
        print("p. PRINT DATABASE SCHEME")
        print("q. QUIT")

        option = input("Enter your option (i rname, d rname, m rname, p, q): ").strip()

        if option == 'p':
            print(relations)
        elif option == 'i':
            rname = input("Enter relation name: ")
            attributes_input = input("Attributes (aname1:atype1:key1, aname2:atype2:key2,...): ")
            attributes = Attributes()
            for attr in attributes_input.split(','):
                aname, atype, key = attr.split(':')
                attributes.add_attribute(Attribute(aname, atype, key))
            relations.add_relation(Relation(rname, attributes))
        elif option == 'm':
            rname = input("Enter relation name to modify: ")
            action = input("Modify action (a: add, d: delete): ")
            if action == 'a':
                attribute_details = input("Attribute details to add (aname:atype:key): ")
                relations.modify_relation(rname, 'a', attribute_details)
                print(f"Attribute {attribute_details} inserted!")
            elif action == 'd':
                attribute_name = input("Attribute name to delete: ")
                relations.modify_relation(rname, 'd', attribute_name)
                print(f"Attribute {attribute_name} deleted!")
        elif option == 'd':
            rname = input("Enter relation name to delete: ")
            relations.delete_relation(rname)
            print(f"Relation {rname} has been deleted")
        elif option == 'q':
            print("Bye!")
            break

if __name__ == "__main__":
    main()
