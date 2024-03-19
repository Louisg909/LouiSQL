from validate import DataType, Required, Unique


class Type:
    def __init__(self, name, datatype, unique=False, primary=False, required=False, auto_increment=False):
        self.name = name
        self.type = datatype
        self.unique_attributes = set()
        self.unique = unique
        self.auto_increment = auto_increment
        self.primary = primary
        self.validations = [test for test in [Unique if unique else None, Required if required else None, DataType] if test is not None]
        self.attributes = []

    def validate(self, value):
        for validation in self.validations:
            if not validation.test(value, self):
                return validation.fail_message(value) + '\n'
        return None

    
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
        return value



if __name__ == '__main__':
    integer = Type('int', int, True, False, False, False)
    integer.new(23)
    integer.new(24)



# specific types:


class ID(Type):
    def __init__(self):
        super().__init__(self, 'id', int, True, True, True, True)
        self.max = 0

    def new(self): # overriding new method for id
        self.max += 1
        return self.max

class Password(Type):
    def __init__(self, name):
        super().__init__(self, name, str)

    def add(self, value):
        return


#class Text(Type):
#
#class Integer(Type):
#
#class Float(Type):

