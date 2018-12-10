import sqlite3

connection = sqlite3.connect('customers.db')
print 'Opened db successfully'


def create_table(table_name, fields):
    primary_key = 'PRIMARY KEY'
    statement = 'CREATE TABLE ' + table_name.upper() + '('
    for field in fields:
        for i in range(0, len(field)):
            statement += field[i].upper() + ' '
        statement = statement.rstrip(' ')
        statement += ', '
    statement = statement.rstrip(', ')
    statement += ')'
    pos = statement.find('INT NOT NULL') + 3
    statement = statement[:pos] + ' PRIMARY KEY ' + statement[pos:] + ';'
    connection.execute(statement)


def insert_into_table(table_name, values):
    statement = 'INSERT INTO ' + table_name + ' VALUES ('
    for value in values:
        if type(value) == str:
            value = '\'' + value + '\''
        statement += str(value) + ', '
    statement = statement.rstrip(', ')
    statement += ');'
    connection.execute(statement)


def select_from_table(table_name, where_clause={}, display_column='*'):
    statement = 'SELECT ' + display_column + ' FROM ' + table_name
    if len(where_clause) != 0:
        statement += ' WHERE '
        for i in range(0, len(where_clause)):
            key = str(where_clause.keys()[i])
            statement += key + '=\"' + str(where_clause[key]) + '\" AND '
    statement = statement.rstrip('AND ') + ';'
    results = connection.execute(statement)
    results = results.fetchall()
    res = []
    for result in results:
        res.append(result[0])
    return res


def menu():
    print '1.) Setup for first time.'
    print '2.) Supply 1 eBook.'
    print '3.) Display an entry.'
    print '5.) Delete an entry.'
    choice = int(raw_input('Enter choice: '))
    if choice == 1:
        table_name = raw_input('Enter table name: ')
        no_of_fields = int(raw_input('Enter number of fields: ')) + 1
        fields = []
        for i in range(1, no_of_fields):
            field = []
            field.append(raw_input('Enter field ' + str(i) + ': '))
            field.append(raw_input('Enter field ' + str(i) + ' type: '))
            not_null = raw_input('NOT NULL field(y/n): ')
            if not_null == 'Y' or 'y':
                field.append('NOT NULL')
            field = tuple(field)
            fields.append(field)
        create_table(table_name, fields)
    if choice == 2:
        table_name = raw_input('Enter table_name: ')
        columns = connection.execute('PRAGMA table_info(' + table_name + ');')
        values = []
        for column in columns:
            value = raw_input('Enter value of ' + column[1] + ' [' + column[2] + ']: ')
            values.append(value)
        insert_into_table(table_name, values)
    if choice == 3:
        table_name = raw_input('Enter table_name: ')
        columns = connection.execute('PRAGMA table_info(' + table_name + ');')
        for column in columns:
            print column
        # column_to_print = raw_input('Enter number of choice of column to print: ')


'''table_name = 'CUSTOMERS'
fields = [('Cust_ID', 'INT', 'NOT NULL'), ('NAME', 'CHAR(20)', 'NOT NULL'), ('PHONE_NUMBER', 'CHAR(10)', 'NOT NULL'),
          ('ADDRESS', 'CHAR(50)'), ('USER_PASSWORD', 'CHAR(15)', 'NOT NULL'),
          ('OWNER_PASSWORD', 'CHAR(15)', 'NOT NULL'), ('DATE', 'CHAR(10)', 'NOT NULL')]
values = [2, 'RAM', '9999999999', 'Faridabad', 'password1', 'password2', '20181005']

# menu()
create_table(table_name, fields)
insert_into_table(table_name, values)
result = select_from_table(table_name, {'CUST_ID': 2, 'NAME': 'RAM', 'USER_PASSWORD': 'password1'}, 'OWNER_PASSWORD')'''
connection.close()
