
def add_student(conn, name, grade):
    """Ajouter un étudiant dans la base de données."""
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO students (name, grade) VALUES (%s, %s)",
            (name, grade)
        )
    conn.commit()


def get_student(conn, student_id):
    """Lire un étudiant à partir de son identifiant."""
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id, name, grade FROM students WHERE id = %s",
            (student_id,)
        )
        return cur.fetchone()



def average_grade(conn):
    """Calculer la moyenne des notes."""
    with conn.cursor() as cur:
        cur.execute("SELECT AVG(grade) FROM students")
        result = cur.fetchone()
        return float(result[0]) if result[0] is not None else 0.0
