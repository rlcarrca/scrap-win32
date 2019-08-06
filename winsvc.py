'''

 Author: Robert Carr
 Date: June 1, 2015
 Description : Python example of creating a windows service.
 
 http://essiene.blogspot.com/2005/04/python-windows-services.html

 Usage : python aservice.py install
 Usage : python aservice.py start
 Usage : python aservice.py stop
 Usage : python aservice.py remove
 
 C:\>python aservice.py  --username <username> --password <PASSWORD> --startup auto install

'''
import win32serviceutil
import win32service
import win32api
import win32con
import win32event
import win32evtlogutil
import servicemanager
import socket


class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "TestService"
    _svc_display_name_ = "Test Service"
    _svc_description_ = "Tests Python service framework by receiving and echoing messages over a named pipe"
         

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_,''))
        self.main()

    def main(self):
        pass

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)

