class CurrencyService:
    """Multi-Currency Exchange Rate Conversion Engine."""

    USD_EXCHANGE_RATES = {
        'USD': 1.0,
        'EUR': 0.92,
        'GBP': 0.79,
        'JPY': 155.40,
        'INR': 83.50,
        'AUD': 1.50,
        'CAD': 1.36,
        'CHF': 0.90,
        'CNY': 7.23,
        'SGD': 1.35
    }

    @staticmethod
    def convert_currency(amount, from_currency='USD', to_currency='EUR'):
        """Convert monetary value between international currencies."""
        from_rate = CurrencyService.USD_EXCHANGE_RATES.get(from_currency.upper(), 1.0)
        to_rate = CurrencyService.USD_EXCHANGE_RATES.get(to_currency.upper(), 1.0)

        usd_equivalent = amount / from_rate
        converted_amount = usd_equivalent * to_rate

        return {
            'original_amount': amount,
            'from_currency': from_currency.upper(),
            'to_currency': to_currency.upper(),
            'converted_amount': round(converted_amount, 2),
            'exchange_rate': round(to_rate / from_rate, 4)
        }
