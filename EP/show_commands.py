
def show_menu():
    import os
    shows_menu=["show running","show ip int br","show ip route", "show ip protocols", "show clock","show platform", "show module", "show version", "show cdp ne", "show inventory | i PID"]
    #shows_menu=['show ver','show ip int br']
    select=[]
    shows=[]
    while True:
        os.system('cls' if os.name=='nt' else 'clear')
        for show in shows_menu:
            if str(shows_menu.index((show))) not in select:
                print str(shows_menu.index(show))+". "+show
        print '======= Selected ======'
        for stored in shows:
            print stored

        select.append(raw_input('\nSelect a command number \nPress "c" to Clear selection \nPress "e" to Execute \nPress "b" to go back\n   Please enter your selection:  '))
        if select[-1].isdigit() and int(select[-1]) < len(shows_menu):
            #print select[-1] + " " + str(len(shows_menu))
            shows.append(shows_menu[int(select[-1])])
        elif select[-1].lower() == 'e':
            break
        elif select[-1].lower() == 'c':
            shows=[]
            select=[]
        elif select[-1].lower() == 'b':
            shows=[]
            break


    #print select
    return shows

