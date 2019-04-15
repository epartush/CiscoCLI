def list_template(mypath):
    from os import listdir
    from os.path import isfile, join
    import os
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    while True:
        cls()
        print "\n ##### Templates ##### "
        for files in onlyfiles:
            print " " + str(onlyfiles.index(files)+1)+".  " +files
        print " b.  back\n"
        file_name= raw_input("Select: ")
        if file_name.isdigit() and file_name > 0:
            if int(file_name) <= len(onlyfiles): # .index(files):
                file_name = onlyfiles[int(file_name)-1]
                return file_name
        elif file_name == 'b':
            return 'b'


def load_config(path,attr):
    # new_conf=[]
    template=[]
    if attr != 0:
        print  "Using attributes"
    else:
        print "Using template\n"



    with open (path, 'r') as f:
        for line in f:
            line = line.strip('\n')
            template.append(line.split(' '))

    if attr != 0:
        return rebuild(attr,template)

    if attr == 0:
        # if raw_input("Print template? [Y/N]").lower() == 'y':
        #     print " ## Template ##"
        for line in template:
            print ' '.join(line)
        return template

def rebuild(attr,template):
    #template=[]
    new_conf=[]
    # raw_input("\nPress any key to rebuild.. \n")
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
                        print "error: Template and device key mismatch, please check"
                elif word[0] == '%':
                    print "Enter Value for " + word[1:] +":"
                    line[line.index(word)] = raw_input()
        new_conf.append(' '.join(line))
    return new_conf

def writetofile (newconfig,filename):
    import time,os
    from datetime import datetime
    TS = datetime.fromtimestamp(time.time()).strftime('%H-%M-%S')
    if not os.path.exists('output/'):
        os.mkdir('output', 0755)
    f = open ('output/'+filename+TS+'.txt', 'w+')
    for line in newconfig:
        print line
        f.write(line+'\n')
    f.close()

    #s