# Embedded file name: scripts/client/web/web_client_api/platform/base.py


class IPlatformWebApi(object):

    def getType(self):
        raise NotImplementedError

    def isInited(self):
        raise NotImplementedError

    def isConnected(self):
        raise NotImplementedError