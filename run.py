
from im.common.common_server import CommonServer

from twisted.python import log
from twisted.application import service
from twisted.internet import tcp
from im.common.log import LoggerSetting
# from im.common.basisServer import BasisService


if __name__ == "__main__":
    import os, sys
    if 'twisted.internet.reactor' in sys.modules:
        del sys.modules['twisted.internet.reactor']

    if os.name == 'nt':
        sys.path.insert(0, "win32")
        sys.path.insert(0, 'win32/lib')
        from twisted.internet import iocpreactor
        iocpreactor.install()
    else:
        from twisted.internet import epollreactor
        epollreactor.install()
    port = 18080
    # log.startLogging(LoggerSetting('tcp_game_server_%s_%s.log' % ("127.0.0.1", port), 'log'))
    # top_server = service.MultiService()
    # basis = BasisService()
    # basis.setServiceParent(top_server)
    # factory = CommonRegister(1)
    from twisted.internet import reactor
    # reactor.listenTCP(port, factory)

    serviceTag = '%s:%s:%s' % ("pushServer", "127.0.0.1", port)
    factory = CommonServer(u"ws://%s:%s" % ("127.0.0.1", port))
    reactor.listenTCP(port, factory)
    reactor.run()
