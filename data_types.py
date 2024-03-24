from validate import DataType, Required, Unique


class Type:
    def __init__(self, name, datatype, unique=False, primary=False, required=False, auto_increment=False, formatting : list['methods']=None, idd=None):
        self.id = idd
        self.name = name
        self.formatting = formatting
        self.type = datatype
        self.unique_attributes = set()
        self.unique = unique
        self.auto_increment = auto_increment
        self.primary = primary
        self.validations = [test for test in [Unique if unique else None, Required if required else None, DataType] if test is not None]
        print(self.validations)
        self.attributes = []

    def __hash__(self):
        return self.id # only place for id - remove this and id if redundant - properly implement if not

    def validate(self, value):
        for validation in self.validations:
            print(validation)
            if not validation.test(value, self):
                return validation.error_message(value) + '\n'
        return ''

    
    def __contains__(self, item):
        return item in self.unique_attributes

    def isprimary(self):
        return self.primary

    def copy(self):
        return self # make new instance of Type with all the same internals??

    def add(self):
        return

    def new_pre(self):
        return None

    def new(self, value=None):
        """
        Takes in a new piece of data, does any processing either to the object or to the value, and then returns this value.

        Returns:
            value: returns the value to be added to the table
        """
        self.new_pre() # for the children if extra functionability is needed
        if self.validate(value): # validate
            if value not in self.unique_attributes:
                self.unique_attributes.add(value) # used for seeing if a unique value exists.
        if self.formatting != None:
            for method in self.formatting:
                value = method(value)
        return value



if __name__ == '__main__':
    integer = Type('int', int, True, False, False, False)
    integer.new(23)
    integer.new(24)



# specific types:

class ID(Type):
    def __init__(self):
        super().__init__('id', int, unique=True, primary=True, required=True, auto_increment=True)
        self.max = 0

    def new(self): # overriding new method for id
        self.max += 1
        return self.max

class Text(Type):
    def __init__(self, name, unique=False, primary=False, required=False, formatting=None):
        super().__init__(name, str, unique=unique, primary=primary, required=required, formatting=formatting) 


class Password(Type):
    def __init__(self, name):
        super().__init__(name, str, required=True)


#class Text(Type):
#
#class Integer(Type):
#
#class Float(Type):

