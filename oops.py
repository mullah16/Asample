class Demo(object):
    def __init__(self):
        print "this is a constructor", self

    def __del__(self):
        print "this is a destructor", self

d= Demo()
print d
print Demo

class PackageManager(object):
    def __init__(self,name,version):
        self.name =name
        self.version = version

    def get_information(self):
        print "name:",self.name
        print "version:",self.version

pm = PackageManager("hello", 2.2)
pm.get_information()