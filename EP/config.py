
def load_config(path):
    new_conf=[{}]
    attbr = {
            'HOSTNAME' : 'Router',
            }
    #f = open(path,'r')
    f = [line.rstrip('\n') for line in open(path, 'r')]
    print f
    for line in f:
        print line
        line =  line.split(' ')
        for word in line:
            if word != '':
                if word[0] == '%':
                    print "Enter Value for " + word[1:]
                    line[line.index(word)] = raw_input()
        new_conf.append (' '.join(line))
    return new_conf
