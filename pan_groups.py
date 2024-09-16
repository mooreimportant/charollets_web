address_to_groups = {}
for group in group_data:
    if group['static_value']:
        for address in group['static_value']:
            if address not in address_to_groups:
                address_to_groups[address] = []
            address_to_groups[address].append(group['name'])

# Function to find all parent groups recursively
def find_all_groups(group_name, group_data, visited=None):
    if visited is None:
        visited = set()
    if group_name in visited:
        return []
    visited.add(group_name)
    groups = [group_name]
    for group in group_data:
        if group.get('static_value') is not None:
            if group_name in group.get('static_value', []):
                groups.extend(find_all_groups(group['name'], group_data, visited))
    return groups

# Add group memberships to address data
for address in address_data:
    address_name = address['name']
    groups = address_to_groups.get(address_name, [])
    all_groups = set()
    for group in groups:
        all_groups.update(find_all_groups(group, group_data))
    address['group_membership'] = list(all_groups)

# Write to CSV
csv_columns = address_data[0].keys()
csv_file = "combined_address_data.csv"
try:
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in address_data:
            writer.writerow(data)
except IOError:
    print("I/O error")

print(f"CSV file '{csv_file}' created successfully.")
