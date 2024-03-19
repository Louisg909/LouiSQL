from LouiSQL import SQL
Table=SQL.Table
from data_types import Type, Text, ID, Password
import formats
t = Table(ID(), Text('username',formatting=[formats.lower]), Password('password'))





















