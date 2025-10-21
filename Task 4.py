import random
import string

def generate_random_dicts(min_dicts=2, max_dicts=10, min_keys=2, max_keys=5):
    num_dicts = random.randint(min_dicts, max_dicts)
    return [
        {k: random.randint(0, 100) for k in random.sample(string.ascii_lowercase, random.randint(min_keys, max_keys))}
        for _ in range(num_dicts)
    ]

def merge_dicts(dicts):
    merged = {}
    for i, d in enumerate(dicts):
        for key, value in d.items():
            if key not in merged or value > merged[key][0]:
                merged[key] = (value, i + 1)
    return merged

def rename_keys(merged, dicts):
    result = {}
    for key, (value, idx) in merged.items():
        key_name = f"{key}_{idx}" if sum(key in d for d in dicts) > 1 else key
        result[key_name] = value
    return result

def main_module2():
    dicts = generate_random_dicts()
    print("Generated list of dicts:")
    print(dicts)

    merged = merge_dicts(dicts)
    result = rename_keys(merged, dicts)

    print("\nFinal merged dict:")
    print(result)

if __name__ == "__main__":
    main_module2()
