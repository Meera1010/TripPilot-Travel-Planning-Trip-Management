class PackingOptimizerService:
    """Weather & Activity Based Packing List Generator."""

    RECOMMENDED_CATEGORIES = {
        'warm': [
            {'item_name': 'Light Cotton T-Shirts', 'quantity': 5, 'category': 'clothes'},
            {'item_name': 'Shorts / Linen Pants', 'quantity': 3, 'category': 'clothes'},
            {'item_name': 'Sunglasses & Sunscreen SPF 50', 'quantity': 1, 'category': 'toilet'},
            {'item_name': 'Swimwear', 'quantity': 2, 'category': 'beach'},
            {'item_name': 'Flip Flops & Sandals', 'quantity': 1, 'category': 'clothes'}
        ],
        'cold': [
            {'item_name': 'Thermal Base Layers', 'quantity': 3, 'category': 'clothes'},
            {'item_name': 'Heavy Down Jacket', 'quantity': 1, 'category': 'clothes'},
            {'item_name': 'Woolen Beanie & Gloves', 'quantity': 2, 'category': 'clothes'},
            {'item_name': 'Waterproof Trekking Boots', 'quantity': 1, 'category': 'clothes'},
            {'item_name': 'Lip Balm & Body Butter', 'quantity': 1, 'category': 'toilet'}
        ],
        'essentials': [
            {'item_name': 'Passport & Physical Visa Copies', 'quantity': 1, 'category': 'documents'},
            {'item_name': 'Universal Travel Power Adapter', 'quantity': 1, 'category': 'electronics'},
            {'item_name': 'Power Bank 20000mAh', 'quantity': 1, 'category': 'electronics'},
            {'item_name': 'First Aid Kit & Prescription Meds', 'quantity': 1, 'category': 'health'}
        ]
    }

    @staticmethod
    def generate_packing_recommendations(climate='warm', duration_days=7):
        """Generate smart checklist based on climate and trip duration."""
        preset = PackingOptimizerService.RECOMMENDED_CATEGORIES.get(climate, PackingOptimizerService.RECOMMENDED_CATEGORIES['warm'])
        items = list(PackingOptimizerService.RECOMMENDED_CATEGORIES['essentials'])

        multiplier = max(1, round(duration_days / 5.0))
        for item in preset:
            items.append({
                'item_name': item['item_name'],
                'quantity': item['quantity'] * multiplier,
                'category': item['category']
            })

        return items
