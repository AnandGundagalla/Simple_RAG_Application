import re
from datetime import datetime
import json

def parse_order_details(text_block):
    # Extract Order ID
    order_id = re.search(r"Order Number\s*[-:]\s*(\S+)", text_block)
    order_id = order_id.group(1) if order_id else None

    # Extract Client Name
    client_match = re.search(r"Customer:\s*([^|]+)", text_block)
    client_name = client_match.group(1).strip() if client_match else None

    # Extract Date and Convert to YYYY-MM-DD
    date_match = re.search(r"Order Date:\s*([0-9]{1,2}\s+\w+\s+[0-9]{4})", text_block)
    if date_match:
        parsed_date = datetime.strptime(date_match.group(1), "%d %B %Y")
        order_date = parsed_date.strftime("%Y-%m-%d")
    else:
        order_date = None

    # Extract Amount Total
    amount_match = re.search(r"Amount Total\s*=\s*USD\s*([\d,]+\.\d{2})", text_block)
    if amount_match:
        amount_clean = amount_match.group(1).replace(",", "")
        order_total = float(amount_clean)
    else:
        order_total = None

    # Build JSON structure
    output = {
        "order_id": order_id,
        "client_name": client_name,
        "order_date": order_date,
        "order_total": order_total
    }

    return json.dumps(output, indent=4)


# Example usage:
text = """
Order Number - PO/2024/8821
Customer: Global Manufacturing | Priority: RUSH
Order Date: 15 November 2025
Amount Total = USD 2,375.00 (tax excluded)
Notes: Rush order, dispatch within 48 hours.
"""

print(parse_order_details(text))
