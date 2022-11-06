# String concatenation
try:

    def madlib_func(Para, noun):
        ans = para.format(noun)
        return ans

    madlibs_list = ['CACTUS', 'VACUUM', 'LOVE', 'LOCKER', 'SPEECH']
    madlib_chosen_by_user = input('''{} {} Which Madlib yoy like to play Please 
 Enter a name : '''.format(madlibs_list, '\n')).upper()
    Noun = input("Noun : ")

    # you can find these MADLIBS on https://www.madlibs.com/
    if madlib_chosen_by_user == madlibs_list[0]:
        para = '''I like my donuts with extra {} on them.'''
        print(madlib_func(para, Noun))
    elif madlib_chosen_by_user == madlibs_list[1]:
        para = "Be careful not to vacuum the {} when you clean under your bed. PLAY WITH FRIENDS VACUUM"
        print(madlib_func(para, Noun))
    elif madlib_chosen_by_user == madlibs_list[3]:
        para = "My gym locker stinks because I'm always leaving my dirty {} in there!!"
        madlib_func(para, Noun)
    elif madlib_chosen_by_user == madlibs_list[4]:
        para = "Once that {} music comes on, it's time to shut down your acceptance"
        print(madlib_func(para, Noun))
    else: # Default one
        para = 'Love is what makes the {} go round.'
        print(madlib_func(para, Noun))

except Exception as e:
    print(e)

