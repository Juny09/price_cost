def calculate_selling_price(cost, margin_percent):
    """
    Calculate selling price based on profit margin.

    Example:
    Cost = RM100
    Margin = 30%
    Selling Price = RM100 / (1 - 0.30)
                  = RM142.86
    """

    if cost < 0:
        raise ValueError("Cost cannot be negative.")

    if margin_percent < 0 or margin_percent >= 100:
        raise ValueError("Margin must be between 0% and 99.99%.")

    margin = margin_percent / 100

    selling_price = cost / (1 - margin)

    return round(selling_price, 2)