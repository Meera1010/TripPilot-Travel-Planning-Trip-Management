from flask import Blueprint, request
from app.models import GarmentTemplate
from app.utils.svg_library import SVG_GARMENTS, SVG_ACCESSORIES
from app.utils.helpers import api_response

garments_api = Blueprint('garments_api', __name__)

@garments_api.route('/templates', methods=['GET'])
def list_templates():
    category = request.args.get('category')
    query = GarmentTemplate.query
    if category:
        query = query.filter_by(category=category)
    templates = query.all()
    return api_response(True, data=[t.to_dict() for t in templates])

@garments_api.route('/categories', methods=['GET'])
def list_categories():
    categories = [
        {'id': 'dress', 'name': 'Dresses & Gowns', 'icon': 'ph-coat-hanger'},
        {'id': 'saree', 'name': 'Sarees & Heritage Drapes', 'icon': 'ph-sparkle'},
        {'id': 'kurti', 'name': 'Kurtis & Tunics', 'icon': 'ph-t-shirt'},
        {'id': 'shirt', 'name': 'Shirts & Blouses', 'icon': 'ph-t-shirt'},
        {'id': 'skirt', 'name': 'Skirts & Bottoms', 'icon': 'ph-t-shirt'},
        {'id': 'jacket', 'name': 'Jackets & Outerwear', 'icon': 'ph-coat-hanger'},
        {'id': 'trousers', 'name': 'Trousers & Pants', 'icon': 'ph-pants'},
        {'id': 'gown', 'name': 'Evening Gowns', 'icon': 'ph-crown'},
        {'id': 'accessory', 'name': 'Bags, Shoes & Jewelry', 'icon': 'ph-handbag'}
    ]
    return api_response(True, data=categories)

@garments_api.route('/presets', methods=['GET'])
def list_presets():
    return api_response(True, data={
        'garments': SVG_GARMENTS,
        'accessories': SVG_ACCESSORIES
    })
