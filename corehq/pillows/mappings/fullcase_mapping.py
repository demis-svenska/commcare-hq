FULL_CASE_INDEX="full_cases_a58449a2c4cb6d1f78a485170b258a8c"
FULL_CASE_MAPPING={'date_formats': ['yyyy-MM-dd', "yyyy-MM-dd'T'HH:mm:ssZZ", "yyyy-MM-dd'T'HH:mm:ss.SSSSSS", "yyyy-MM-dd'T'HH:mm:ss.SSSSSS'Z'", "yyyy-MM-dd'T'HH:mm:ss'Z'", "yyyy-MM-dd'T'HH:mm:ssZ", "yyyy-MM-dd'T'HH:mm:ssZZ'Z'", "yyyy-MM-dd'T'HH:mm:ss.SSSZZ", "yyyy-MM-dd'T'HH:mm:ss", "yyyy-MM-dd' 'HH:mm:ss", "yyyy-MM-dd' 'HH:mm:ss.SSSSSS", "mm/dd/yy' 'HH:mm:ss"], 'dynamic': True, '_meta': {'comment': 'Autogenerated [casexml.apps.case.models.CommCareCase] mapping from ptop_generate_mapping 03/21/2013', 'created': None}, 'date_detection': False, 'properties': {'opened_on': {'type': 'date', 'format': "yyyy-MM-dd||yyyy-MM-dd'T'HH:mm:ssZZ||yyyy-MM-dd'T'HH:mm:ss.SSSSSS||yyyy-MM-dd'T'HH:mm:ss.SSSSSS'Z'||yyyy-MM-dd'T'HH:mm:ss'Z'||yyyy-MM-dd'T'HH:mm:ssZ||yyyy-MM-dd'T'HH:mm:ssZZ'Z'||yyyy-MM-dd'T'HH:mm:ss.SSSZZ||yyyy-MM-dd'T'HH:mm:ss||yyyy-MM-dd' 'HH:mm:ss||yyyy-MM-dd' 'HH:mm:ss.SSSSSS||mm/dd/yy' 'HH:mm:ss"}, 'location_': {'type': 'string'}, 'domain': {'fields': {'domain': {'index': 'analyzed', 'type': 'string'}, 'exact': {'index': 'not_analyzed', 'type': 'string'}}, 'type': 'multi_field'}, 'referrals': {'type': 'object', 'enabled': False}, 'xform_ids': {'index': 'not_analyzed', 'type': 'string'}, 'server_modified_on': {'type': 'date', 'format': "yyyy-MM-dd||yyyy-MM-dd'T'HH:mm:ssZZ||yyyy-MM-dd'T'HH:mm:ss.SSSSSS||yyyy-MM-dd'T'HH:mm:ss.SSSSSS'Z'||yyyy-MM-dd'T'HH:mm:ss'Z'||yyyy-MM-dd'T'HH:mm:ssZ||yyyy-MM-dd'T'HH:mm:ssZZ'Z'||yyyy-MM-dd'T'HH:mm:ss.SSSZZ||yyyy-MM-dd'T'HH:mm:ss||yyyy-MM-dd' 'HH:mm:ss||yyyy-MM-dd' 'HH:mm:ss.SSSSSS||mm/dd/yy' 'HH:mm:ss"}, 'indices': {'dynamic': False, 'type': 'object', 'properties': {'identifier': {'type': 'string'}, 'referenced_type': {'type': 'string'}, 'referenced_id': {'type': 'string'}}}, 'initial_processing_complete': {'type': 'boolean'}, 'export_tag': {'type': 'string'}, 'computed_modified_on_': {'type': 'date', 'format': "yyyy-MM-dd||yyyy-MM-dd'T'HH:mm:ssZZ||yyyy-MM-dd'T'HH:mm:ss.SSSSSS||yyyy-MM-dd'T'HH:mm:ss.SSSSSS'Z'||yyyy-MM-dd'T'HH:mm:ss'Z'||yyyy-MM-dd'T'HH:mm:ssZ||yyyy-MM-dd'T'HH:mm:ssZZ'Z'||yyyy-MM-dd'T'HH:mm:ss.SSSZZ||yyyy-MM-dd'T'HH:mm:ss||yyyy-MM-dd' 'HH:mm:ss||yyyy-MM-dd' 'HH:mm:ss.SSSSSS||mm/dd/yy' 'HH:mm:ss"}, 'external_id': {'fields': {'exact': {'index': 'not_analyzed', 'type': 'string'}, 'external_id': {'index': 'analyzed', 'type': 'string'}}, 'type': 'multi_field'}, 'actions': {'type': 'object', 'dynamic': False}, 'owner_id': {'type': 'string'}, 'computed_': {'type': 'object', 'enabled': False}, 'user_id': {'type': 'string'}, 'version': {'type': 'string'}, 'modified_on': {'type': 'date', 'format': "yyyy-MM-dd||yyyy-MM-dd'T'HH:mm:ssZZ||yyyy-MM-dd'T'HH:mm:ss.SSSSSS||yyyy-MM-dd'T'HH:mm:ss.SSSSSS'Z'||yyyy-MM-dd'T'HH:mm:ss'Z'||yyyy-MM-dd'T'HH:mm:ssZ||yyyy-MM-dd'T'HH:mm:ssZZ'Z'||yyyy-MM-dd'T'HH:mm:ss.SSSZZ||yyyy-MM-dd'T'HH:mm:ss||yyyy-MM-dd' 'HH:mm:ss||yyyy-MM-dd' 'HH:mm:ss.SSSSSS||mm/dd/yy' 'HH:mm:ss"}, 'closed_on': {'type': 'date', 'format': "yyyy-MM-dd||yyyy-MM-dd'T'HH:mm:ssZZ||yyyy-MM-dd'T'HH:mm:ss.SSSSSS||yyyy-MM-dd'T'HH:mm:ss.SSSSSS'Z'||yyyy-MM-dd'T'HH:mm:ss'Z'||yyyy-MM-dd'T'HH:mm:ssZ||yyyy-MM-dd'T'HH:mm:ssZZ'Z'||yyyy-MM-dd'T'HH:mm:ss.SSSZZ||yyyy-MM-dd'T'HH:mm:ss||yyyy-MM-dd' 'HH:mm:ss||yyyy-MM-dd' 'HH:mm:ss.SSSSSS||mm/dd/yy' 'HH:mm:ss"}, 'closed': {'type': 'boolean'}, 'type': {'fields': {'exact': {'index': 'not_analyzed', 'type': 'string'}, 'type': {'index': 'analyzed', 'type': 'string'}}, 'type': 'multi_field'}, 'name': {'fields': {'exact': {'index': 'not_analyzed', 'type': 'string'}, 'name': {'index': 'analyzed', 'type': 'string'}}, 'type': 'multi_field'}}}