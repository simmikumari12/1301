import sys
from Time import Time

def generate_time(s):
    """Converts a string time to a Time object."""
    hour, minute_ampm = s[:-5], s[-4:]
    hour, minute = map(int, hour.split('.'))
    ampm = minute_ampm.strip()
    return Time(hour, minute, ampm)

def read_data(fname):
    """Reads the file and returns a list of non-comment lines."""
    with open(fname, 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip() and not line.startswith("#")]

def extract_data_parts(data):
    """Extracts time intervals and step counts from the data."""
    result = []
    for line in data:
        start_time, end_time, steps = line.split(":")
        start = generate_time(start_time)
        end = generate_time(end_time)
        steps = int(steps)
        result.append((start, end, steps))
    return result

def remove_bad_data(data):
    """Removes data where start time is after end time."""
    valid_data = []
    for start, end, steps in data:
        if start.after(end):
            print(f"INVALID data: {start} : {end} : {steps}")
        else:
            valid_data.append((start, end, steps))
    return valid_data

def compute_stats(data):
    """Computes the total steps and total walking minutes."""
    total_steps = 0
    total_minutes = 0
    for start, end, steps in data:
        total_steps += steps
        total_minutes += start.minutes_between(end)
    return total_steps, total_minutes

def main():
    total_steps, total_minutes = compute_stats(remove_bad_data(extract_data_parts(read_data(sys.argv[1]))))
    print("\nTotal steps: ", total_steps)
    print("Hourly steps rate: ", int(total_steps / (total_minutes / 60)), "\n")

if __name__ == "__main__":
    main()
