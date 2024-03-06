

class SQL:
    class Type:
        def __init__(self, name, datatype, unique=False, primary=False, auto_increment=False):
            self.name = name
            self.type = datatype
            self.attributes = []
            self.unique = unique
            self.auto_increment = auto_increment
            self.primary = primary
        
        def __contains__(self, item):
            return item in self.attributes

        def isprimary(self):
            return self.primary

        def copy(self):
            return self # make new instance of Type with all the same internals??

    class ID(Type):
        def __init__(self, auto_increment=True):
            self.name = 'id'
            self.type = int
            self.unique = True
            self.auto_increment = auto_increment
            self.primary = True
            self.max = 0

        def __contains__(self, item):
            return item < self.max

        def new(self):
            self.max += 1
            return self.max



    class Table:
        def __init__(self, *attributes):
            self.query = False # checking if it is from a query or if it is its own table
            self.columns = [att for att in attributes]
            assert sum(n.isprimary() for n in self.columns) == 1, f'There needs to be one, and only one, primary key. {[n.isprimary() for n in self.columns]}'
            self.data = [] # data is stored in columns so think I don't need this? If remove, need to edit `__repr__` method
            self.size = 0

        def set(self, columns, data, size):
            self.columns = columns
            self.data = data
            self.size = size
        
        def add_value(self, *args):
            typle = []
            increment_id = self.columns[0].auto_increment
            if increment_id:
                typle.append(self.columns[0].new())
            for i, item in enumerate(args):
                ic = i+1 if increment_id else i
                assert type(item) is self.columns[ic].type, f'{item} is not of type {self.columns[ic].type}.'
                assert not (item in self.columns[ic] and self.columns[ic].unique), f'{self.columns[ic].name} is set to be unique, and {item} already exists.'
                #if self.columns[ic].unique:
                #    self.columns[ic].attributes.append(item)
                self.columns[ic].attributes.append(item)
                typle.append(item)
            self.data.append(typle)
            self.size += 1

        def __repr__(self):
            output = '|'
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

