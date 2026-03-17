from src.pricing import calculate_bill

def generate_invoices(df):

    df["invoice_amount"] = df.apply(calculate_bill, axis=1)

    return df