# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
import json

class ProductTemplateController(http.Controller):
    @http.route('/api/products', auth='none', type="http", methods=['GET'], csrf=False)
    def get_products_handler(self, **kw):
        Product = request.env['product.template'].sudo()
        products = Product.search([])

        results = [
            {
                'id': product.id,
                'name': product.name,
                'list_price': product.list_price,
            } for product in products 
            ]
        
        return Response(json.dumps(results), content_type='application/json', status=200)
    
    # Add a new route to create a product
    @http.route('/api/products', auth='none', type="http", methods=['POST'], csrf=False)
    def create_products_handler(self, **kw):
        reqbody = json.loads(request.httprequest.data)
        Product = request.env['product.template'].sudo()

        new_product = Product.create({
            'name': reqbody['name'],
            'list_price': reqbody['list_price'],
        })
        
        return Response(json.dumps({
            'id': new_product.id,
            'name': new_product.name,
            'list_price': new_product.list_price,
        }), content_type='application/json', status=201)
    
    # Add a new route to get a product by id
    @http.route('/api/products/<int:product_id>', auth='none', type="http", methods=['GET'], csrf=False)
    def get_product_by_id(self, product_id, **kw):
        Product = request.env['product.template'].sudo()
        products = Product.browse(product_id)

        if not products.exists():
            return Response(json.dumps({'error': 'Product not found'}), content_type='application/json', status=404)
        
        response = {
            'id': products.id,
            'name': products.name,
            'list_price': products.list_price,
        }
        return Response(json.dumps(response), content_type='application/json', status=200)
    
    # Add a new route to update a product by id
    @http.route('/api/products/<int:product_id>', auth='none', type="http", methods=['PUT'], csrf=False)
    def update_product_by_id(self, product_id, **kw):
        reqbody = json.loads(request.httprequest.data)
        Product = request.env['product.template'].sudo()
        products = Product.browse(product_id)

        if not products.exists():
            return Response(json.dumps({'error': 'Product not found'}), content_type='application/json', status=404)
        
        products.write({
            'name': reqbody['name'],
            'list_price': reqbody['list_price'],
        })
        
        return Response(json.dumps({
            'id': products.id,
            'name': products.name,
            'list_price': products.list_price,
        }), content_type='application/json', status=200)
    
    # Add a new route to delete a product by id
    @http.route('/api/products/<int:product_id>', auth='none', type="http", methods=['DELETE'], csrf=False)
    def delete_product_by_id(self, product_id, **kw):
        Product = request.env['product.template'].sudo()
        products = Product.browse(product_id)

        if not products.exists():
            return Response(json.dumps({'error': 'Product not found'}), content_type='application/json', status=404)
        
        products.unlink()
        return Response(json.dumps({'success': 'Product deleted'}), content_type='application/json', status=200)