
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
def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    
    # Test case 1
    present_capacities = [113, 116, 80, 95, 92, 70]
    counts = count_batteries_by_health(present_capacities)
    assert counts["healthy"] == 2, f"Test case 1 failed, got {counts['healthy']}, expected 2"
    assert counts["exchange"] == 3, f"Test case 1 failed, got {counts['exchange']}, expected 3"
    assert counts["failed"] == 1, f"Test case 1 failed, got {counts['failed']}, expected 1"
    
    # Test case 2
    present_capacities_healthy = [120, 115, 118, 110, 112]
    counts_healthy = count_batteries_by_health(present_capacities_healthy)
    assert counts_healthy["healthy"] == 5, f"Test case 2 failed, got {counts_healthy['healthy']}, expected 5"
    assert counts_healthy["exchange"] == 0, f"Test case 2 failed, got {counts_healthy['exchange']}, expected 0"
    assert counts_healthy["failed"] == 0, f"Test case 2 failed, got {counts_healthy['failed']}, expected 0"

    # Test case 3 (Boundary conditions)
    present_capacities_boundary = [120, 0, 60, 90, 30]
    counts_boundary = count_batteries_by_health(present_capacities_boundary)
    assert counts_boundary["healthy"] == 1, f"Test case 3 failed, got {counts_boundary['healthy']}, expected 1"
    assert counts_boundary["exchange"] == 1, f"Test case 3 failed, got {counts_boundary['exchange']}, expected 1"
    assert counts_boundary["failed"] == 3, f"Test case 3 failed, got {counts_boundary['failed']}, expected 3"

    # Test case 4 (All failed batteries)
    present_capacities_all_failed = [50, 45, 30, 20, 15]
    counts_all_failed = count_batteries_by_health(present_capacities_all_failed)
    assert counts_all_failed["healthy"] == 0, f"Test case 4 failed, got {counts_all_failed['healthy']}, expected 0"
    assert counts_all_failed["exchange"] == 0, f"Test case 4 failed, got {counts_all_failed['exchange']}, expected 0"
    assert counts_all_failed["failed"] == 5, f"Test case 4 failed, got {counts_all_failed['failed']}, expected 5"

    print("All tests passed!")

# Run the test function
test_bucketing_by_health()
