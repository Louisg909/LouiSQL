
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


def s(self, *at:str): 
    def ga(A):
        for n in self.columns:
            if n.name == A:
                return n #.copy()

    cn = [n.name for n in self.columns]
    atts = []
    for n in at:
        assert n in cn, f'{n} is not in this table bro'
        atts.append(ga(n))
    o = Table()
    data = [[] for _ in range(size)]
    for i in range(size):
        for n in att:
            data[i].append(n.at[i]) # this seems very yucky!!
    o.set(columns=atts, data=data, size=size)
    return o
