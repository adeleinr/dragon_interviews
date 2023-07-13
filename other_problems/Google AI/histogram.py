from collections import defaultdict
def automatic_histogram(dataset, num_buckets):
    counter = defaultdict(int)
    histogram = {}
    min_value = dataset[0]
    max_value = dataset[0]
    for item in dataset:
        if item > max_value:
            max_value = item
        elif item < min_value:
            min_value = item
        counter[item] += 1
    num_ranges_in_bucket = max_value // num_buckets

    curr_lower_key_range = min_value
    for i in range(num_buckets):
        if i + 1 < num_buckets:
            curr_upper_key_range = curr_lower_key_range + num_ranges_in_bucket
        else:
            curr_upper_key_range = max_value
        if curr_lower_key_range == max_value:
            key = str(curr_lower_key_range)
        else:
            key = str(curr_lower_key_range) + "-" + str(curr_upper_key_range)
        print(key)
        for j in range(curr_upper_key_range, curr_upper_key_range + 1):
            if key not in histogram:
                histogram[key] = 0
            histogram[key] = histogram[key] + counter[j]
        curr_lower_key_range = curr_upper_key_range + 1
    return histogram

print(automatic_histogram([1,2,2,3,4,5], 3))
print(automatic_histogram([1,2,2,3,4,10], 3))
