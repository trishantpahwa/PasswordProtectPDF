from sqlite3 import connect
from sqlite3 import Error
from os.path import exists
import sys
import traceback


class database:

    __tables = ['Books']
    __books_column_types = [('CUST_ID', 'INT', 'NOT NULL PRIMARY KEY'),
                            ('Name', 'VARCHAR(20)', 'NOT NULL'),
                            ('Phone Number', 'VARCHAR(13)', 'NOT NULL'),
                            ('Address', 'VARCHAR(30)', 'NOT NULL'),
                            ('User Password', 'VARCHAR(20)', 'NOT NULL'),
                            ('Owner Password', 'VARCHAR(20)', 'NOT NULL'),
                            ('Date', 'VARCHAR(10)', 'NOT NULL')]
    
    __books_columns = [ x[0] for x in __books_column_types ]

    __table_name = None
    __columns = None
    __conn = None
    __c = None

    __statement = ''

    def __init__(self, table_name):  # table_name[string]
        db_file = 'books_database.db'
        self.__conn = connect(db_file)
        self.__c = self.__conn.cursor()
        if not exists(db_file):
            self.__create_database(db_file)
        self.__set_table_name(table_name)
        self.__set_columns()
        self.__conn = connect(db_file)
        self.__c = self.__conn.cursor()
        print('Connected to database')

    def __create_database(self, file_name):  # file_name[string]
        file = open(file_name, 'w')
        file.close()

    def __set_table_name(self, table_name):  # table_name[string]
        self.__statement = 'SELECT name from sqlite_master WHERE type=\"table\"'
        tables = self.__execute_query()
        tables = [table[0] for table in tables]
        if len(tables) > 0:
            self.__table_name = table_name
            if table_name not in tables:
                if self.__table_name == 'books':
                    self.__create_table(self.__books_column_types)
        else:
            self.__table_name = table_name
            self.__create_table(self.__books_column_types)

    def __set_columns(self):
        if self.__table_name == 'books':
            self.__columns = self.__books_columns

    def __execute_query(self):
        try:
            self.__c.execute(self.__statement)
            rows = self.__c.fetchall()
            return rows
        except Error:
            print(Error)
            traceback.print_stack(Error)

    def disconnect_from_server(self):
        self.__conn.commit()
        self.__conn.close()

    def print_records(self, columns=None, constraints=None):  # columns[list(string)] constraints[dict(string,string)]
        print_statement = 'SELECT '
        if columns is None:
            print_statement += '* FROM ' + self.__table_name
        else:
            if type(columns) == type(list()):
                for column in columns:
                    if column in constraints.keys():
                        constraint = constraints.get(column)
                        print_statement += constraint + '(' + column + ')' + ','
                    else:
                        print_statement += column + ','
                print_statement = print_statement.rstrip(',') + ' FROM ' + \
                    self.__table_name
                self.__statement = print_statement
            if type(columns) == type(dict()):
                for key, value in columns.items():
                    print_statement += key + ','
                print_statement = print_statement.rstrip(',') + ' FROM ' + \
                    self.__table_name
                print_statement += ' WHERE '
                for key, value in columns.items():
                    print_statement += key + '=\"' + value + '\" AND '
                print_statement = print_statement.rstrip(' AND ')
        self.__statement = print_statement
        return self.__execute_query()

    def insert_records(self, values):  # values[list(string)]
        insert_statement = 'INSERT INTO ' + self.__table_name + ' VALUES('
        for value in values:
            insert_statement += '\'' + value + '\','
        insert_statement = insert_statement.rstrip(',') + ')'
        self.__statement = insert_statement
        return self.__execute_query()

    def update_records(self, current_values={}, update_values={}):  # current_values[dict(string,string)] update_values[dict(string, string)]
        update_statement = 'UPDATE ' + self.__table_name + ' SET '
        for key, value in update_values.items():
            update_statement += key + '=\'' + value + '\' AND '
        update_statement = update_statement.rstrip(' AND ') + ' WHERE '
        for key, value in current_values.items():
            update_statement += key + '=\'' + value + '\' AND '
        update_statement = update_statement.rstrip(' AND ')
        self.__statement = update_statement
        return self.__execute_query()

    def delete_records(self, values={}):  # values[dict(string,string)]
        delete_statement = 'DELETE FROM ' + self.__table_name + ' WHERE '
        for key, value in values.items():
            delete_statement += key + '=\'' + value + '\' AND '
        delete_statement = delete_statement.rstrip(' AND ')
        self.__statement = delete_statement
        return self.__execute_query()

    def __create_table(self, columns):  # columns[list(string)]
        create_statement = 'CREATE TABLE ' + self.__table_name + ' ('
        for column, data_type, constraint in columns:
            create_statement += column + ' ' + data_type + ' ' + constraint + ','
        create_statement = create_statement.rstrip(',')
        create_statement += ')' + ";"
        self.__statement = create_statement
        print(self.__table_name + ' created')
        return self.__execute_query()


    '''
    def __set_columns(self, columns):  # When columns are not hard-coded
        get_columns_query = 'PRAGMA table_info(' + self.__table_name + ')'
        self.__statement = get_columns_query
        rows = self.__execute_query()
        rows = [row[0] for row in rows]
        self.__columns = columns
    '''


