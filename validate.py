import sys

def validate():
    fobj = open("simple_conns_port.log")
    print "validating the log file..."
    riskyports = []
    ports = ["80","443"]
    for line in fobj:
        if line.rstrip().startswith('#') == False:
            unknownport = True
            for port in ports:
                if port == line.rstrip():
                    unknownport = False
            if unknownport == True:
                riskyports.append(line.rstrip())
    fobj.close()
    return riskyports

def printresult(riskyports, result):
     print prefix + ": {\"result\":\" " + result + "\", \"info\": {\"unknown_ports\": [" + ", ".join(riskyports) + "]}}"



if __name__ == "__main__":
    if len(sys.argv) == 2:
        prefix = sys.argv[1]
        riskyports = validate()
        if len(riskyports)==0:
            printresult(riskyports,"CLEAN")
        elif len(riskyports)<3:
            printresult(riskyports,"SUSPICIOUS")
        else:
            printresult(riskyports,"MALICIOUS")


    else:
        print "ID is missing!"
