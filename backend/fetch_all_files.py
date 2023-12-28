from connection import connection


def fetch_all_files():
    try:
        conn = connection()
        cursor = conn.cursor()

        query = '''SELECT filename, location FROM uploaded_files '''
        cursor.execute(query)
        rows = cursor.fetchall()

        lst = []
        for row in rows:
            result_dict = {
                "filename": row[0],
                "location": row[1]
            }
            lst.append(result_dict)
        return lst
    except Exception as e:
        return f"Error: {e}"
    # finally:
        # pass
        # return "sai"
        # conn.close()
