from grade import Grade


class TestGrade:

    def test_initial_value_ok(self):
        grade = Grade(4.0, '3.3.33')
        assert grade.value == 4.0

    def test_initial_value_to_low(self):
        grade = Grade(-1.0, '3.3.35')
        assert grade.value == -1.0

    def test_initial_value_to_high(self):
        grade = Grade(7.0, '3.3.35')
        assert grade.value == -1.0

    def test_date_set(self):
        grade = Grade(3.0, '3.3.33')
        assert grade.date == '3.3.33'
