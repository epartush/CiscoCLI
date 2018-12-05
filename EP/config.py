
def load_config(path,attr):
    new_conf=[]
    template=[]
    if attr != 0:
        print  "Using attributes"
    else:
        print "Using open template"

    #f = open(path,'r')
    f = [line.rstrip('\n') for line in open(path, 'r')]
    with open (path, 'r') as f:
        for line in f:
            line = line.strip('\n')
            template.append(line.split(' '))
    if raw_input("Print template? [Y/N]").lower() == 'y':
        print " ## Template ##"
        for line in template:
            print ' '.join(line)

    raw_input("\nPress any key to rebuild.. \n")
    for line in template:
        if attr == 0:
            print ' '.join(line)
        for word in line:
            if word != '':
                if attr != 0 and word[0] == '%':
                    if word[1:].lower() in attr:
                        #print attr[word[1:].lower()]
                        line[line.index(word)] = attr[word[1:].lower()]
                    else:
                        print "!!Missing Info!!!"
                elif word[0] == '%':
                    print "Enter Value for " + word[1:]
                    line[line.index(word)] = raw_input()
        new_conf.append(' '.join(line))
    return new_conf

def writetofile (newconfig,filename):
    import time
    from datetime import datetime
    TS = datetime.fromtimestamp(time.time()).strftime('%H-%M-%S')
    f = open ('output/'+filename+TS+'.txt', 'w+')
    for line in newconfig:
        print line
        f.write(line+'\n')
    f.close()



