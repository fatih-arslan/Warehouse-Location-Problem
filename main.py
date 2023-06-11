def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    num_warehouses, num_customers = map(int, lines[0].split())
    warehouses = []
    customers = []

    for i in range(1, num_warehouses + 1):
        capacity, cost = map(float, lines[i].split())
        warehouses.append((capacity, cost))

    for i in range(num_warehouses + 1, len(lines), 2):
        demand = int(lines[i])
        customer_costs = list(map(float, lines[i + 1].split()))
        customers.append((demand, customer_costs))

    return warehouses, customers

def allocate_warehouses(warehouses, customers):
    num_warehouses = len(warehouses)
    num_customers = len(customers)
    assigned_warehouses = [0] * num_customers
    remaining_capacity = [warehouse[0] for warehouse in warehouses]

    for customer_index in range(num_customers):
        min_cost = float('inf')
        min_cost_warehouse = -1

        for warehouse_index in range(num_warehouses):
            warehouse_capacity, warehouse_cost = warehouses[warehouse_index]
            customer_demand, customer_costs = customers[customer_index]

            if (
                warehouse_capacity >= customer_demand
                and customer_costs[warehouse_index] < min_cost
                and remaining_capacity[warehouse_index] >= customer_demand
            ):
                min_cost = customer_costs[warehouse_index]
                min_cost_warehouse = warehouse_index

        if min_cost_warehouse != -1:
            assigned_warehouses[customer_index] = min_cost_warehouse
            remaining_capacity[min_cost_warehouse] -= customers[customer_index][0]

    total_cost = 0
    for i in range(num_customers):
        total_cost += customers[i][1][assigned_warehouses[i]]

    for w in set(assigned_warehouses):
        total_cost += warehouses[w][1]

    return round(total_cost, 2), assigned_warehouses

file_name = 'wl_16_1'
input_file = f"input_files/{file_name}"
warehouses, customers = read_input_file(input_file)
cost, assignments = allocate_warehouses(warehouses, customers)

print("Optimum Cost:", cost)
print("Warehouse Assignments:", end=" ")
for i in assignments:
    print(i, end=" ")



