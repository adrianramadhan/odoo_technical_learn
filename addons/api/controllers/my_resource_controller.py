# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response

import json

class MyResourceController(http.Controller):
    @http.route('/api/resources', auth='none', type="http", methods=['GET'], csrf=False)
    def get_resources_handler(self, **kw):
        Resource = request.env['my.resource'].sudo()
        resources = Resource.search([])

        results = [
            {
                'id': resource.id,
                'name': resource.name,
                'description': resource.description,
                'price': resource.price,
                'active': resource.active
            } for resource in resources 
            ]
        
        return Response(json.dumps(results), content_type='application/json', status=200)
    
    @http.route('/api/resources', auth='none', type="http", methods=['POST'], csrf=False)
    def create_resources_handler(self, **kw):
        reqbody = json.loads(request.httprequest.data)
        Resource = request.env['my.resource'].sudo()

        new_resource = Resource.create({
            'name': reqbody['name'],
            'description': reqbody['description'],
            'price': reqbody['price'],
        })
        
        return Response(json.dumps({
            'id': new_resource.id,
            'name': new_resource.name,
            'description': new_resource.description,
            'price': new_resource.price,
        }), content_type='application/json', status=201)
    
    @http.route('/api/resources/<int:resource_id>', auth='none', type="http", methods=['GET'], csrf=False)
    def get_resource_by_id(self, resource_id, **kw):
        Resource = request.env['my.resource'].sudo()
        resources = Resource.browse(resource_id)

        if not resources.exists():
            return Response(json.dumps({'error': 'Resource not found'}), content_type='application/json', status=404)
        
        response = {
            'id': resources.id,
            'name': resources.name,
            'description': resources.description,
            'price': resources.price,
            'active': resources.active
        }
        return Response(json.dumps(response), content_type='application/json', status=200)
    
    @http.route('/api/resources/<int:resource_id>', auth='none', type="http", methods=['PUT'], csrf=False)
    def update_resources_handler(self, resource_id, **kw):
            reqbody = json.loads(request.httprequest.data)
            Resource = request.env['my.resource'].sudo()

            resource = Resource.browse(resource_id)
            
            if not resource.exists():
                return Response(json.dumps({'error': 'Resource not found'}), content_type='application/json', status=404)

            resource.write(reqbody)

            return Response(json.dumps({
                'id': resource.id,
                'name': resource.name,
                'description': resource.description,
                'price': resource.price,
            }), content_type='application/json', status=200)
    
    @http.route('/api/resources/<int:resource_id>', auth='none', type="http", methods=['DELETE'], csrf=False)
    def delete_resources_handler(self, resource_id, **kw):
        Resource = request.env['my.resource'].sudo()

        resource = Resource.browse(resource_id)
        
        if not resource.exists():
            return Response(json.dumps({'error': 'Resource not found'}), content_type='application/json', status=404)

        resource.unlink()

        return Response(json.dumps({
            'message': 'Resource deleted successfully'
        }), content_type='application/json', status=200)