import sys
import getopt
 
def site():
    name = None
    url = None
 
    argv = sys.argv[1:]
 
    try:
        opts, args = getopt.getopt(argv, "n:u:",  
                                   ["name=",
                                    "url="])  # 长选项模式
     
    except:
        print("Error")
 
    for opt, arg in opts:
        if opt in ['-n', '--name']:
            name = arg
        elif opt in ['-u', '--url']:
            url = arg
     
 
    print( name + " " + url)
 
site()