def summarise_data(file, col_index):
    with open(file, 'r') as f:
        max_val = float('-inf')
        min_val = float('inf')
        total = 0
        count = 0

        if col_index is not int:
            return ValueError("IndexError - col_index out of range")

        for line in f:
            values = line.strip().split(',')
            if col_index >= len(values):
                return ValueError("IndexError - col_index out of range")
            try:
                value = float(values[col_index])
            except ValueError:
                return ValueError("ValueError - invalid value in data")
            max_val = max(max_val, value)
            min_val = min(min_val, value)
            total += value
            count += 1
        mean = round(total / count, 2)
        return [max_val, min_val, total, count, mean]
