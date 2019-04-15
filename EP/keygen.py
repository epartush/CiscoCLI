import curses
# from curses import wrapper
# stdscr = curses.initscr()

# curses.noecho()


# begin_x = 20; begin_y = 7
# height = 5; width = 40
# win = curses.newwin(height, width, begin_y, begin_x)

def check(stdscr):
    stdscr = curses.initscr()
    # curses.init_color()
    c=['']
    phrase=['']
    #curses.newwin(2,50,2,0)
    while 1:
        stdscr.addstr(0,0,"Type in your phrase, Press '~' to clear, 'Q' to quit and 'Enter' to store once you got 64. " + phrase[-1])

        stdscr.refresh()
        c.append(chr(stdscr.getch()))

        if c[-1] == '\x7f' and len(c) > 2:

            c.pop(-1)
            c.pop()


        elif c[-1] == '\n':
            c.pop()
            if len(''.join(c).strip('\n').encode('hex')) == 64:

            #for char in c:
             #   phrase.append(chr(char))
            #stdscr.addstr("Pretty text", curses.color_pair(3))
                phrase=''.join(c).strip('\r\n').encode(('hex'))
                stdscr.addstr(2,0, "Stored                ")
            elif len(''.join(c).strip('\n').encode('hex')) < 64:
                stdscr.addstr(2,0, "Add more characters   ")

            elif len(''.join(c).strip('\n').encode('hex')) > 64:
                stdscr.addstr(2,0, "Delete some characters")

        elif c[-1] == 'Q':
            return str(phrase)

        elif c[-1] == '~':
            c = ['']
            phrase = ['']
            stdscr.addstr(2,0, "Cleared                 ")

        elif c[-1] == curses.KEY_HOME:
            x = y = 0


        stdscr.addstr(3,0,''.join(c)+(80-(len(''.join(c))))*' ')
        stdscr.refresh()

        stdscr.addstr(1,0,str(len(''.join(c).strip('\n\r').encode(('hex'))))+ "  ")

        stdscr.refresh()


'''phrase =wrapper(check)

print "your key is " + phrase
print "the length of the key is " + str(len(phrase))
print "your phrase is " + phrase.decode('hex')
'''