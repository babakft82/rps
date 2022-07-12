from datetime import datetime

CHOOSE_OPTION = ("r", "p", "s")

RULES = {
    ('p', 'r'): 'p',
    ('p', 's'): 's',
    ('r', 's'): 'r'
}

score_board = {
    "user": 0,
    "system": 0

}


def test_decorator(func):
    def wrap_function(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        duration = end_time - start_time
        hours = duration.seconds // 3600
        minutes = duration.seconds // 60
        seconds = duration.seconds % 60
        print(
            f"Elapsed time: {hours}: {minutes}: {seconds}",
        )
    return wrap_function
