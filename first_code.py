
def work():
    print('---->>>>fun')
    user = input('enter your opinion yes/no: ')
    if user == 'yes':
        print('enjoy ur treat')
    else:
        print('make your own treat')
        print('and make sure it will touch your soul')
        work()


work()
