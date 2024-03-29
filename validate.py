

class Validation:
    @classmethod
    def error_message(cls, value):
        return f'\'{value}\' failed {cls.__name__}'


class DataType(Validation):
    def test(value, Type):
        return isinstance(value, Type.type)


# Used when an item is required, such as for the id, username, or passwords
class Required(Validation):
    def test(value, Type):
        return (value != "") and (value != None)


# checking if the item is unique, such as for IDs, usernames, or emails
class Unique(Validation):
    def test(value, Type):
        return not value in Type.unique_attributes


if __name__ == '__main__':
    item = ''
    if Required.test(item):
        print('Passed')
    else:
        print(Required.error_message(item))

    








"""
def validate(self, value):
    for validation in self.validations:
        if not validation.test(value):
            raise Exception(f'Validation test {validation.name} failed due to {validation.error_message(value)}')
    return isinstance(value, self.datatype)
"""
