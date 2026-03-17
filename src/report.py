def generate_report(df):

    import os
    import pandas as pd

    os.makedirs("reports", exist_ok=True)

    total_revenue = df["invoice_amount"].sum()

    summary_df = pd.DataFrame({
        "Metric": ["Total Customers", "Total Revenue"],
        "Value": [len(df), total_revenue]
    })

    with pd.ExcelWriter("reports/invoice_report.xlsx") as writer:

        df.to_excel(writer, sheet_name="Invoices", index=False)
        summary_df.to_excel(writer, sheet_name="Summary", index=False)

    print("Invoice report generated")