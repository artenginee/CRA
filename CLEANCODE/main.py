def decrease_one_day(rooms: list):
    for room_num in range(len(rooms)):
        if rooms[room_num] == 0:
            continue
        rooms[room_num] -= 1