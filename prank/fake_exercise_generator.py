from phrase_maker import phrase_maker

import fake_exercises

def main():
    phrase_maker.load_module(fake_exercises)
    print(phrase_maker.make('exercise', capitalize=False))

if __name__ == '__main__':
    main()