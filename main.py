def count_batteries_by_health(present_capacities):
    # Constants
    rated_capacity = 120  # Rated capacity of a new battery in Ah

    # Initialize counts
    health_counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }

    # Iterate through each battery's present capacity
    for present_capacity in present_capacities:
        # Compute state of health (SoH)
        soh_percentage = (present_capacity / rated_capacity) * 100

        # Classify batteries based on SoH
        if soh_percentage > 80:
            health_counts["healthy"] += 1
        elif 62 <= soh_percentage <= 80:
            health_counts["exchange"] += 1
        else:
            health_counts["failed"] += 1

    # Return the counts
    return health_counts

# Test function
def count_batteries_by_health(present_capacities):
    # Constants
    rated_capacity = 120  # Rated capacity of a new battery in Ah

    # Initialize counts
    health_counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }

    # Iterate through each battery's present capacity
    for present_capacity in present_capacities:
        # Compute state of health (SoH)
        soh_percentage = (present_capacity / rated_capacity) * 100

        # Classify batteries based on SoH
        if soh_percentage >= 80:
            health_counts["healthy"] += 1
        elif 62 <= soh_percentage < 80:
            health_counts["exchange"] += 1
        else:
            health_counts["failed"] += 1

    # Return the counts
    return health_counts

# Test function
def test_count_batteries_by_health():
    print("Counting batteries by SoH...\n")

    # Provided Test Case
    present_capacities_provided = [113, 116, 80, 95, 92, 70]
    counts_provided = count_batteries_by_health(present_capacities_provided)
    assert counts_provided["healthy"] == 2, f"Provided test case failed, got {counts_provided['healthy']}, expected 2"
    assert counts_provided["exchange"] == 3, f"Provided test case failed, got {counts_provided['exchange']}, expected 3"
    assert counts_provided["failed"] == 1, f"Provided test case failed, got {counts_provided['failed']}, expected 1"

    # Test case 1 (Upper Bound: Maximum Rated Capacity)
    present_capacities_max = [120, 120, 120, 120, 120]
    counts_max = count_batteries_by_health(present_capacities_max)
    assert counts_max["healthy"] == 5, f"Test case 1 failed, got {counts_max['healthy']}, expected 5"
    assert counts_max["exchange"] == 0, f"Test case 1 failed, got {counts_max['exchange']}, expected 0"
    assert counts_max["failed"] == 0, f"Test case 1 failed, got {counts_max['failed']}, expected 0"

    # Test case 2 (Lower Bound: Minimum Rated Capacity)
    present_capacities_min = [0, 0, 0, 0, 0]
    counts_min = count_batteries_by_health(present_capacities_min)
    assert counts_min["healthy"] == 0, f"Test case 2 failed, got {counts_min['healthy']}, expected 0"
    assert counts_min["exchange"] == 0, f"Test case 2 failed, got {counts_min['exchange']}, expected 0"
    assert counts_min["failed"] == 5, f"Test case 2 failed, got {counts_min['failed']}, expected 5"

    # Test case 3 (Boundary at 80% SoH: Healthy and Exchange Boundary)
    present_capacities_boundary_80 = [96, 96, 96, 96, 96]
    counts_boundary_80 = count_batteries_by_health(present_capacities_boundary_80)
    assert counts_boundary_80["healthy"] == 5, f"Test case 3 failed, got {counts_boundary_80['healthy']}, expected 5"
    assert counts_boundary_80["exchange"] == 0, f"Test case 3 failed, got {counts_boundary_80['exchange']}, expected 0"
    assert counts_boundary_80["failed"] == 0, f"Test case 3 failed, got {counts_boundary_80['failed']}, expected 0"


    # Test case 4 (Edge Case at 100% SoH)
    present_capacities_edge_100 = [120, 120, 120, 120, 120]
    counts_edge_100 = count_batteries_by_health(present_capacities_edge_100)
    assert counts_edge_100["healthy"] == 5, f"Test case 4 failed, got {counts_edge_100['healthy']}, expected 5"
    assert counts_edge_100["exchange"] == 0, f"Test case 4 failed, got {counts_edge_100['exchange']}, expected 0"
    assert counts_edge_100["failed"] == 0, f"Test case 4 failed, got {counts_edge_100['failed']}, expected 0"

    # Test case 5 (Edge Case at 0% SoH)
    present_capacities_edge_0 = [0, 0, 0, 0, 0]
    counts_edge_0 = count_batteries_by_health(present_capacities_edge_0)
    assert counts_edge_0["healthy"] == 0, f"Test case 5 failed, got {counts_edge_0['healthy']}, expected 0"
    assert counts_edge_0["exchange"] == 0, f"Test case 5 failed, got {counts_edge_0['exchange']}, expected 0"
    assert counts_edge_0["failed"] == 5, f"Test case 5 failed, got {counts_edge_0['failed']}, expected 5"

    print("All tests passed!")

test_count_batteries_by_health()
