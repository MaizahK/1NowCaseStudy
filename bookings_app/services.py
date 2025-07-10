
# mock function to return stripe response
def stripe_deposit(user, amount):
    return {
        "status": "success",
        "charge_id": "ch_123456789"
    }