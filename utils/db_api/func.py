from sqlite3 import Error
import sqlite3 


class DBS:
    def post_sql_query(sql_query):
        with sqlite3.connect("./bot.db") as connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(sql_query)
                except Error:
                    pass
                result = cursor.fetchall()
                return result
        
    def create_users_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS USERS(           
            user_id TEXT,
            username TEXT,
            full_name TEXT)
        '''
        self.post_sql_query(query)
    
    def user_register (self, user_id, user_name, full_name):
        query = f"SELECT * FROM users WHERE user_id='{user_id}'"
        data = self.post_sql_query(query)
        if not data:
            insert_query = f"INSERT INTO users(user_id, username, full_name) VALUES ('{user_id}', '{user_name}', '{full_name}')"
            self.post_sql_query(insert_query)
    
    def chat_register (self, chat_id ):
        query = f"SELECT * FROM groups WHERE chat_id='{chat_id}'"
        data = self.post_sql_query(query)
        if not data:
            insert_query = f"INSERT INTO groups(chat_id) VALUES ('{chat_id}')"
            self.post_sql_query(insert_query)

    def getGroups (self):
        query = f"SELECT * FROM groups"
        data = self.post_sql_query(query)
        if len(data) == 0:
            return False
        return data
    
    def delGroup(self, chat_id):
        query =f"DELETE FROM groups WHERE chat_id='{chat_id}';"
        print(query)
        self.post_sql_query(f"DELETE FROM groups WHERE chat_id='{chat_id}';")