from boarding_passes import boarding_passes
from typing import List

highest_seat_id = 0


def get_num(code: str, range: List[int]) -> int:
    range = range
    for letter in code:
        mid = round((range[1] - range[0]) / 2)
        if letter in 'FL':  # lower half
            range[1] -= mid
        elif letter in 'BR':  # upper half
            range[0] += mid
        else:
            return None
    return range[0] if letter in 'FL' else range[1]


if __name__ == "__main__":
    for bp in boarding_passes:
        row_code, column_code = bp[:7], bp[7:]  # 0-127 0-7

        row = get_num(row_code, [0, 127])
        col = get_num(column_code, [0, 7])
        seat_id = row * 8 + col

        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    print(highest_seat_id)
