from sqlalchemy import text


class TestStudents:

    def test_add_student(self, session):
        new_student = {
            "user_id": 999999,
            "level": "Beginner",
            "education_form": "group",
            "subject_id": 1,
        }
        session.execute(
            text(
                "INSERT INTO student "
                "(user_id, level, education_form, subject_id) "
                "VALUES (:user_id, :level, :education_form, :subject_id)"
            ),
            new_student,
        )
        session.commit()

        result = session.execute(
            text("SELECT level FROM student WHERE user_id = :id"),
            {"id": new_student["user_id"]},
        ).fetchone()

        assert result is not None
        assert result[0] == "Beginner"

        session.execute(
            text("DELETE FROM student WHERE user_id = :id"),
            {"id": new_student["user_id"]},
        )
        session.commit()

    def test_update_student(self, session):
        user_id = 999998
        session.execute(
            text(
                "INSERT INTO student "
                "(user_id, level, education_form, subject_id) "
                "VALUES (:user_id, :level, :education_form, :subject_id)"
            ),
            {
                "user_id": user_id,
                "level": "Beginner",
                "education_form": "group",
                "subject_id": 1,
            },
        )
        session.commit()

        session.execute(
            text(
                "UPDATE student SET level = :level "
                "WHERE user_id = :id"
            ),
            {"level": "Advanced", "id": user_id},
        )
        session.commit()

        result = session.execute(
            text("SELECT level FROM student WHERE user_id = :id"),
            {"id": user_id},
        ).fetchone()

        assert result[0] == "Advanced"

        session.execute(
            text("DELETE FROM student WHERE user_id = :id"),
            {"id": user_id},
        )
        session.commit()

    def test_delete_student(self, session):
        user_id = 999997
        session.execute(
            text(
                "INSERT INTO student "
                "(user_id, level, education_form, subject_id) "
                "VALUES (:user_id, :level, :education_form, :subject_id)"
            ),
            {
                "user_id": user_id,
                "level": "Beginner",
                "education_form": "group",
                "subject_id": 1,
            },
        )
        session.commit()

        session.execute(
            text("DELETE FROM student WHERE user_id = :id"),
            {"id": user_id},
        )
        session.commit()

        result = session.execute(
            text("SELECT * FROM student WHERE user_id = :id"),
            {"id": user_id},
        ).fetchone()

        assert result is None
