from common import Event


class FeedSyncBegin(Event):
    __type__ = 'feed_sync_begin'

    def __init__(self, service, groups):
        super(FeedSyncBegin, self).__init__(user_id='admin', level='INFO', message='Begin feed sync', resource_type='Feeds', details={'sync_feed_types': groups}, service=service)


class FeedSyncComplete(Event):
    __type__ = 'feed_sync_complete'

    def __init__(self, service, groups):
        super(FeedSyncComplete, self).__init__(user_id='admin', level='INFO', message='Completed feed sync', resource_type='Feeds', details={'sync_feed_types': groups}, service=service)


class FeedSyncFail(Event):
    __type__ = 'feed_sync_fail'

    def __init__(self, service, groups, error):
        super(FeedSyncFail, self).__init__(user_id='admin', level='ERROR', message='Failed feed sync', resource_type='Feeds', details={'error': str(error), 'sync_feed_types': groups}, service=service)
