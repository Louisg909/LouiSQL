# need to ensure thread saftey for use of table.
from table import Table


class SQL: # rename to Database or something
    def __init__(self):
        self.tables = set()

    def add_table(self, *attributes):
        self.tables.add(SQL.Table(*attributes))
        # how to call tables when querying? Sort this out.
        # Querying in the outer class will also only be grabbing tables and putting them together
        # the manipulation of tables and pulling info from tables will be done inside the SQL.Table class.


    def pull(self, table:str, columns:list[str]=None) -> 'Table':
        """
        Performs a simple select of columns ""
        """
        return table0.get_columns(self.tables[table])







    class Smart_Organise:
        def __init__():
            self.tables : list['Table':list[str:'name']] = {}
            self.rules = 0 # way to add rules to decide what table data would go in. So I put in Student(id, accomodation, department, teacher) it looks if department and teacher need to be added to the department table, and either way, the student is put in the student table and an assosication is given between them.

        def add(self, entry):
            return


            
                


if __name__ == '__main__':
    table1 = SQL.Table(SQL.ID(), SQL.Type('name', str), SQL.Type('type', str))
    table2 = SQL.Table(SQL.ID(), SQL.Type('name', str), SQL.Type('type_f', str))
    table1.add_value('Cheese', 'Ameera')
    table1.add_value('Poop', 'I love Ameera')
    table2.add_value('Poopy', ' 2222 I love Ameera')
    table2.add_value('Yarss', 'Table 2 tings love Ameera')
    print('Table 1:')
    print(table1)
    print('Table 2:')
    print(table2)
    table3 = table2.select('name')

