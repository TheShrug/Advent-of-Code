class Guards:
    def __init__(self):
        self.guards = []
        self.shifts = []

    def find_or_create_guard(self, log_entry):
        guard_id = log_entry.split(' ')[3].strip('#')
        for guard_index, guard in enumerate(self.guards):
            if guard[0] == guard_id:
                return self.guards[guard_index][1]
        new_guard = [guard_id, Guard(guard_id)]
        self.guards.append(new_guard)
        return new_guard[1]

    def add_guard_shift(self, log_entries):
        self.shifts.append(log_entries)

    def simulate_guard_shifts(self):
        for shift in self.shifts:
            guard = self.find_or_create_guard(shift[0])
            if shift.__len__() > 1:
                del shift[0]
                guard.simulate_shift(shift)

    def get_guard_from_id(self, guard_id):
        for guard in self.guards:
            if guard_id == guard[0]:
                return guard[1]
        return None


class Guard:
    def __init__(self, guard_id):
        self.id = guard_id
        self.total_minutes_slept = 0
        self.minutes_slept_on = []
        for i in range(60):
            self.minutes_slept_on.append(0)

    def simulate_shift(self, shift_list):
        sleep_from = int(shift_list[0].split(' ')[1].split(':')[1].strip(']'))
        sleep_to = int(shift_list[1].split(' ')[1].split(':')[1].strip(']'))
        self.sleep(sleep_from, sleep_to)
        del shift_list[0:2]
        if shift_list.__len__() > 0:
            self.simulate_shift(shift_list)

    def sleep(self, sleep_from_int, sleep_to_int):
        while sleep_from_int < sleep_to_int:
            self.total_minutes_slept += 1
            self.minutes_slept_on[sleep_from_int] += 1
            sleep_from_int += 1


# sort the logs
file = open("input.txt")
logs = []
for line in file:
    logs.append(line.strip("\n"))
logs.sort()

# create the guards object
guards = Guards()

# parse through the logs adding shifts to the guards object
shift_start_index = None
shift_end_index = None
for index, log in enumerate(logs):
    if log.find('#') > -1:
        if shift_start_index is None:
            shift_start_index = index
        if shift_start_index != index:
            shift_end_index = index
        if shift_start_index is not None and shift_end_index is not None:
            guards.add_guard_shift(logs[shift_start_index:shift_end_index])
        shift_start_index = index

# after all shifts are added, lets simulate the shifts
guards.simulate_guard_shifts()

# after shifts are simulated we have guard objects that contain the data on when they slept and we can print out answers
max_slept_guard_id = 0
max_minutes_slept = 0

for guard in guards.guards:
    if guard[1].total_minutes_slept > max_minutes_slept:
        max_minutes_slept = guard[1].total_minutes_slept
        max_slept_guard_id = guard[0]

optimal_guard = guards.get_guard_from_id(max_slept_guard_id)

answer1 = int(optimal_guard.id) * optimal_guard.minutes_slept_on.index(max(optimal_guard.minutes_slept_on))

print("answer 1:", answer1)

answer_2_guard = 0
answer_2_minute = 0

for guard in guards.guards:
    max_minute = guard[1].minutes_slept_on.index(max(guard[1].minutes_slept_on))
    if max_minute > answer_2_minute:
        answer_2_minute = max_minute
        answer_2_guard = guard[0]

print("answer 2:", int(answer_2_guard) * answer_2_minute)