import locale 
locale.setlocale(locale.LC_ALL, "ru")

import codecs

def main():
    try:
        lj = codecs.open('lj.txt', 'r', 'utf_8_sig')
    except IOError:
        print('Error! Cannot open file lj.txt!')
        exit(0)
    d2 = codecs.open('d2.txt', 'w', 'utf_8_sig')
    
    imageNo = 1
    
    while True:
        ch = lj.read(1)
        if not ch:
            break
        if ch == '<':
            ch = lj.read(1)
            if ch == 'l':    # removing lj-cut or lj-embed and changing lj user
                st = lj.read(3)                  # lj-cut
                if st == 'j-c':
                    while lj.read(1) != '>':
                        continue
                    continue
                elif st == 'j-e':                # lj-embed
                    while lj.read(1) != '\n':
                        continue
                    continue
                elif st == 'j u':                # lj user
                    while lj.read(1) != '"':
                        continue
                    st = ''
                    while True:
                        ch = lj.read(1)
                        if ch == '"':
                            break
                        st += ch
                    while lj.read(1) != '>':
                        continue
                    d2.write('<a href="https://' + st + '.livejournal.com">' + st + '</a>')
                    continue
                else:
                    print('Unexpectedly there is something other than lj-cut and lj-embed')
                    break
            elif ch == '/':    # continue removing lj-cut or lj-embed
                ch = lj.read(1)
                if ch == 'l':
                    st = lj.read(3)
                    if st == 'j-c':
                        while lj.read(1) != '>':
                            continue
                        continue
                    elif st == 'j-e':
                        while lj.read(1) != '\n':
                            continue
                        continue
                    else:
                        print('Unexpectedly there is something other than lj-cut and lj-embed')
                        break
                else:
                    d2.write('</')
            elif ch == 'i':
                ch = lj.read(1)
                if ch == 'm':    # changing img
                    while lj.read(1) != '>':
                        continue
                    d2.write('<img src="' + str(imageNo) + '" title="">')
                    imageNo = imageNo + 1
                    continue
                elif ch == 'f':    # changing iframe (video only)
                    nQuotes = 0
                    while nQuotes < 10:
                        if lj.read(1) == '"':
                            nQuotes = nQuotes + 1
                    st = lj.read(12)
                    if st == ' data-link="':
                        while True:
                            ch = lj.read(1)
                            if ch != '"':
                                d2.write(str(ch))
                            else:
                                break
                        while lj.read(1) != '>':
                            continue
                        while lj.read(1) != '>':    # removing </iframe> in the end
                            continue
                        continue
                    else:
                        print('It\'s not video!')
                        break
                else:
                    d2.write('<i')
            elif ch == 'a':    # changing link to user page
                st = lj.read(34)
                if st == ' href="https://www.drive2.ru/users':
                    while lj.read(1) != '>':
                        continue
                    ch = lj.read(1)
                    st = ''
                    while ch != '<':
                        st = st + ch
                        ch = lj.read(1)
                    d2.write('<user name="' + st + '">')
                    st = lj.read(3)
                    if st == '/a>':
                        continue
                    else:
                        print('Unexpected error occured!')
                        break
                else:
                    d2.write('<a' + st)
                    continue
            else:
                d2.write('<')
        d2.write(str(ch))
    
    lj.close()
    d2.close()


main()