def taxi_cost(route_length, waiting_time=0) -> int | None:
 
    basic_cost = 80 
    route_length_cost = route_length / 150 * 6
    waiting_time_cost = waiting_time * 3
    
    if route_length < 0:
        return None
    elif route_length == 0:
        return round(
                basic_cost +
                80 +
                waiting_time_cost
                )
    else:
        return round(
                basic_cost +
                route_length_cost +
                waiting_time_cost
                )

# >>> taxi_cost(10)
# 80

# >>> taxi_cost(5369, 24)
# 367

# >>> taxi_cost(0, 32)
# 256
