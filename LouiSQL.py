# need to ensure thread saftey for use of table.

class RowError(Exception):
    def cheese(self):
        return

class SQL: # rename to Database or something
    def __init__(self):
        self.tables = set()

    def add_table(self, *attributes):
        self.tables.add(SQL.Table(*attributes))
        # how to call tables when querying? Sort this out.
        # Querying in the outer class will also only be grabbing tables and putting them together
        # the manipulation of tables and pulling info from tables will be done inside the SQL.Table class.
    class Smart_Organise:
        def __init__():
            self.tables : list['Table':list[str:'name']] = {}
            self.rules = 0 # way to add rules to decide what table data would go in. So I put in Student(id, accomodation, department, teacher) it looks if department and teacher need to be added to the department table, and either way, the student is put in the student table and an assosication is given between them.

        def add(self, entry):
            return


    class Table:
        def __init__(self, *attributes):
            self.query = False # checking if it is from a query or if it is its own table
            self.columns = [att for att in attributes]
            assert sum(n.isprimary() for n in self.columns) == 1, f'There needs to be one, and only one, primary key. {[n.isprimary() for n in self.columns]}'
            self.data = set()
            self.size = 0

        def set(self, columns, data, size):
            self.columns = columns
            self.data = data
            self.size = size
        
        def add(self, *args): # add a tuple to the table.
            """
            Adds new row to the table.

            Args:
                *args: Values for each column in the row being added, in the correct order

            Returns:
                fe

            Raises:
                RowError: When an validation is failed on the row, such as a wrong input type or no value given for a required value
            """ # should maybe change *args to **kwargs so then can add certain colums? If it is larger, some rows may be blank or None types? Also means it doesn't matter what order - this isn't important for now so leave this as a note for later.
            new_row = []
            columns = self.columns
            increment_id = columns[0].auto_increment
            if increment_id:
                new_row.append(columns[0].new())

            # Validation of all arguments
            error_message = ''
            for index, item in enumerate(args):
                i = index + 1 if increment_id else index
                error_message += columns[i].validate(item)
            if error_message != '':
                raise RowError(error_message)

            # Add values to row
            for index, item in enumerate(args):
                i = index + 1 if increment_id else index
                new_row.append(columns[i].new(item))

            # add row to table data
            self.data.add(tuple(new_row))
            self.size += 1

        def __repr__(self): # want to do a lot more to this...
            output = f'<LouiSQL Table>\n|'
            for column in self.columns:
                output += f'{column.name:^20}|'
            output += '\n|'
            for _ in self.columns:
                output += '-'*20+'|'
            output += '\n|'
            for i, tt in enumerate(self.data):
                for n in tt:
                    output += f'{n:^20}|'
                if i < self.size: output += '\n|' 
            return output

        # querying
        def select(self, *attributes:str): # select doesn't make a new table! just shows parts of the table it is selecting from!\
                # I will make query/s that will make new tables so will save what I have done so far to refer back to.\
                # Thinking about it though, I still need a way to access and query the answer so I might need to make a new table???
            def get_attribute(attribute):
                for n in self.columns:
                    if n.name == attribute:
                        return n #.copy()

            column_names = [n.name for n in self.columns]
            atts = []
            for n in attributes:
                assert n in column_names, f'{n} is not in this table bro'
                atts.append(get_attribute(n))
            output = Table()
            data = [[] for _ in range(size)]
            for i in range(size):
                for n in att:
                    data[i].append(n.attributes[i]) # this seems very yucky!!
            output.set(columns=atts, data=data, size=size)
            return output

        def join(self, left=False):
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

