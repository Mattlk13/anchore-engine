import datetime
import json

from anchore_engine.configuration.localconfig import get_host_id


class Event(object):
    __type__ = None

    def __init__(self, user_id, level, message, details, service, resource_type, request_id=None, resource_id=None):
        self.user_id = user_id
        self.level = level
        self.message = message
        self.details = details if details else {}
        self.timestamp = datetime.datetime.utcnow().isoformat()
        self.service = service
        self.host_id = get_host_id()
        self.request_id = request_id
        self.resource_id = resource_id
        self.resource_type = resource_type

    def to_json(self):
        msg = dict()
        msg['type'] = self.__type__
        msg['level'] = self.level
        msg['message'] = self.message
        msg['details'] = self.details
        msg['timestamp'] = self.timestamp
        msg['resource'] = {'user_id': self.user_id, 'type': self.resource_type}
        if self.resource_id:
            msg['resource']['id'] = self.resource_id
        msg['source'] = {'service': self.service, 'host_id': self.host_id}
        if self.request_id:
            msg['source']['request_id'] = self.request_id

        return json.dumps(msg)
