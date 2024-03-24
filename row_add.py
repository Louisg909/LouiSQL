
def add(self, **kwargs):
    new_row = []
    columns = self.columns

    # Autoincrementing the id if needed
    increment_id = columns[0].auto_increment
    if increment_id:
        new_row.append(columns[0].new())

    # Validation of all arguments
    error_message = ''
    


