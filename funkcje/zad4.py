def PrintAnimal(*animals):
    for animal in animals:
        if animal == 'cat':
            # this function prints a cat ascii-art
            txt = r'''
            |\---/|
            | o_o |
             \_^_/'''
            print(txt)
        elif animal == 'bear':
            txt = r'''
            /  \.-"""-./  \
            \    -   -    /
             |   o   o   |
             \  .-'"'-.  /
              '-\__Y__/-'
                 `---`'''
            print(txt)
        elif animal == 'bat':
            # this function prints a bat ascii-art
            txt = r'''
              /\                 /\
             / \'._   (\_/)   _.'/ \
            /_.''._'--('.')--'_.''._\
            | \_ / `;=/ " \=;` \ _/ |
             \/ `\__|`\___/`|__/`  \/
                     \(/|\)/  
                '''
            print(txt)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % (animal))
            return False
    return

PrintAnimal('bear', 'bat')

