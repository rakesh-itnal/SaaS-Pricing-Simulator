def calculate_bill(row):

    plan = row["plan"]
    usage = row["api_calls"]

    if plan == "Basic":
        base_price = 20
        limit = 10000
        extra_rate = 0.002

    elif plan == "Pro":
        base_price = 50
        limit = 50000
        extra_rate = 0.001

    else:
        return 0

    extra_usage = max(usage - limit, 0)

    extra_cost = extra_usage * extra_rate

    total = base_price + extra_cost

    return round(total, 2)