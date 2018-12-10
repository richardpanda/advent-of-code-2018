from stars import Stars


class TestStars:
    def test_compute_message_time(self):
        with open("sample.txt") as f:
            stars = Stars(list(f))
            assert stars.compute_message_time() == 3

        with open("input.txt") as f:
            stars = Stars(list(f))
            assert stars.compute_message_time() == 10159
