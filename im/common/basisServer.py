from twisted.application.service import Service

class BasisService(Service):

    def startService(self):
        super(BasisService, self).startService()
        print("startService....")

    def stopService(self):
        super(BasisService, self).stopService()
        print('stopService.....')