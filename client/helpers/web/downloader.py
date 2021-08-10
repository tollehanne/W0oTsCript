# Embedded file name: scripts/client/helpers/web/downloader.py


class IDownloader(object):

    def close(self):
        raise NotImplementedError

    def downloadLowPriority(self, url, callback):
        raise NotImplementedError

    def download(self, url, callback):
        raise NotImplementedError