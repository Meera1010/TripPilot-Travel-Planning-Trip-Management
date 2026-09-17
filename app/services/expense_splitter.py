class ExpenseSplitterService:
    """Group Debt Simplification & Balance Settlement Graph Algorithm."""

    @staticmethod
    def calculate_group_balances(expenses):
        """Calculate net balance per user across trip expenses."""
        user_balances = {}

        for exp in expenses:
            payer_id = exp.paid_by_id
            user_balances[payer_id] = user_balances.get(payer_id, 0.0) + exp.amount

            for split in exp.splits:
                user_id = split.user_id
                user_balances[user_id] = user_balances.get(user_id, 0.0) - split.share_amount

        return user_balances

    @staticmethod
    def simplify_debts(user_balances, user_names=None):
        """Minimum-Cash-Flow Greedy Debt Settlement Algorithm."""
        user_names = user_names or {}
        debtors = []
        creditors = []

        for uid, bal in user_balances.items():
            rounded_bal = round(bal, 2)
            if rounded_bal < -0.01:
                debtors.append({'user_id': uid, 'amount': -rounded_bal})
            elif rounded_bal > 0.01:
                creditors.append({'user_id': uid, 'amount': rounded_bal})

        settlements = []
        d_idx = 0
        c_idx = 0

        while d_idx < len(debtors) and c_idx < len(creditors):
            debtor = debtors[d_idx]
            creditor = creditors[c_idx]

            settle_amount = min(debtor['amount'], creditor['amount'])

            settlements.append({
                'from_user_id': debtor['user_id'],
                'from_user_name': user_names.get(debtor['user_id'], f"User #{debtor['user_id']}"),
                'to_user_id': creditor['user_id'],
                'to_user_name': user_names.get(creditor['user_id'], f"User #{creditor['user_id']}"),
                'amount': round(settle_amount, 2)
            })

            debtor['amount'] -= settle_amount
            creditor['amount'] -= settle_amount

            if debtor['amount'] < 0.01:
                d_idx += 1
            if creditor['amount'] < 0.01:
                c_idx += 1

        return settlements
