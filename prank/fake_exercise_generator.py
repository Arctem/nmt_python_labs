from phrase_maker import phrase_maker

import fake_exercises

replacements = {
    'BEGINLIST': '\\begin{itemize}',
    'ENDLIST': '\\end{itemize}',
    'LISTITEM.': '\\item',
    'BEGINTABLE': '\\begin{centering}\n\\begin{tabular}{c | c | c}' +
        '\n\\toprule',
    'ENDTABLE': '\\bottomrule\n\\end{tabular}\n\\end{centering}',
}
def convert(phrase):
    for rep in replacements:
        phrase = phrase.replace(rep, replacements[rep])
        phrase = phrase.replace(rep.capitalize(), replacements[rep])
        phrase = phrase.replace(rep.lower(), replacements[rep])

    name, desc = phrase.split(': ', 1)
    name = name.lower()
    phrase = '\\begin{ex}[' + name + '] ' + desc + '\\end{ex}'
    return phrase

def main():
    phrase_maker.load_module(fake_exercises)
    #print(convert(phrase_maker.make('exercise', capitalize=False)))
    #print(phrase_maker.make('exercise', capitalize=False))
    #return

    phrases = []
    for i in range(100):
        phrase = phrase_maker.make('exercise', capitalize=False)
        phrase = convert(phrase)

        phrases.append(phrase)

    exercises = '\n\n'.join(phrases)

    target = '../labs/lab9'

    original = open(target + '.tex', 'r').read()
    modified = original.replace('%INSERT HERE', exercises)
    with open(target + '_prank.tex', 'w') as output:
        output.write(modified)

if __name__ == '__main__':
    main()