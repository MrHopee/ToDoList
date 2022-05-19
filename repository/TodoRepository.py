from Database.Connection import cursor, connection


class TodoRepository:
    def get_tasks(self):
        cursor.execute("SELECT * FROM todo_list")
        results = cursor.fetchall()
        result_list = []
        for row in results:
            result_list.append({
                "id": row['id'],
                "content": row['content'],
                "is_mark_as_completed": row['is_mark_as_completed'],
            })
        return result_list

    def add_todo(self, content):
        cursor.execute("INSERT INTO todo_list (content) VALUES(%s)", (content,))
        connection.commit()

    def remove_todo(self, id):
        cursor.execute("DELETE FROM todo_list WHERE id = %s", (id,))
        connection.commit()

    def edit_todo(self, id, content):
        cursor.execute("UPDATE todo_list SET content = %s WHERE id = %s", (content, id))
        connection.commit()
        return

    def mark_as_completed(self, id, ):
        cursor.execute(" UPDATE todo_list SET is_mark_as_completed = true WHERE id = %s", (id,))
        connection.commit()
        return
