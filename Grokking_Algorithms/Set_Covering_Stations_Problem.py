states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
stations = {
    "kOne": {"id", "nv", "ut"},
    "kTwo": {"wa", "id", "mt"},
    "kThree": {"or", "nv", "ca"},
    "kFour": {"nv", "ut"},
    "kFive": {"ca", "az"},
}

final_stations = set()

while states_needed:
    best_stations = None
    states_covered = set()
    for station, states in stations.items():  # Return tuple of two station and states found in the hash table
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_stations = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_stations)


print(final_stations)   # Time Taken 2.5 sec
