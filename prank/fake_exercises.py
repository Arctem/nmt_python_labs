data = {
    'exercise': {
        'template': ['{filename}[project]: {description}'],

        'filename': ['{old_words/template}.py'],

        'description': ['{intro} {requirements}'],

        'intro': ['Using {Module}, {create} a {prog_thing} to {prog_action}.',
            '{Create} a {prog_thing} that {prog_actions}.',
            '{Create} a {prog_thing} such that {prog_actioning} {does} {prog_action}.',
            '{Redo} {former_lab} to {prog_action}.',
            '{Redo} {former_lab} using {prog_things}.'],

        'prog_thing': ['{prog_adj} {prog_thing}', '{prog_adj} {prog_noun}'],
        'prog_things': ['{prog_adj} {prog_things}', '{prog_adj} {prog_nouns}'],
        'prog_adj': ['recursive', 'iterative', 'object-oriented', 'lambda',
            'higher-order', 'first-class', 'obfuscated', 'threaded'],
        'prog_noun': ['function', 'class', 'program', 'interface', 'set',
            'list', 'dictionary'],
        'prog_nouns': ['functions', 'classes', 'programs', 'interfaces', 'sets',
            'lists', 'dictionaries'],
        'prog_verb': ['invert', 'iterate over', 'reduce', 'simplify', 'parse',
            'call', 'return', 'create'],
        'prog_verbs': ['inverts', 'iterates over', 'reduces', 'simplifies',
            'parses', 'calls', 'returns', 'creates'],
        'prog_verbing': ['calling', 'returning'],

        'prog_action': ['{prog_verb} a group of {adjective,prog_adj} {nouns}',
            'repeatedly {math}'],
        'prog_actions': ['{prog_verbs} a group of {adjective,prog_adj} {nouns}',
            'takes in {input} and {prog_actions}'],
        'prog_actioning': ['{prog_verbing} a {prog_thing}',
            '{prog_verbing} {weird_cmd}'],

        'weird_cmd': ['{function}({no_args,args})',
            '{module}.{function}({no_args,args})'],
        'function': ['map', 'reduce', 'sort', 'split', 'filter', 'obfuscate',
            '{old_words/template}', 'load_module', 'make', 'compile', 'name'],
        'module': ['{module}.{module}', 'functools', 'math', 'magic', 'antigravity', 'PIL', 'urllib',
            'sys', 'os', 'random', 'pickle', 're', 'matplotlab'],
        'no_args': [''],
        'args': ['{arg}, {args}', '{arg}'],
        'arg': ['{old_words/template}', '{function}', '{module}', '{prog_adj}',
            '{prog_noun}'],

        'input': ['a text file', 'a list of {nouns} terminated by {stop}'],

        'stop': ['stop', 'cease', 'terminate', 'stop now', 'plzstop',
            'a null terminator', 'EOF', 'a stop sign',
            'a group of misled parents with their hearts in the right place'],

        'adjective': ['irritated', 'invisible', 'hidden', 'inverted',
            'green', 'volatile', 'sorted'],
        'nouns': ['hamsters', 'toddlers', 'phone numbers', 'sentences',
            'fans', 'text files', 'images', 'calendars', 'cars'],

        'requirements': ['{requirement} {requirements}',
            '{requirement} {requirement}\n{requirements}',
            '{requirement} {requirement} {requirement}'],
        'requirement': ['Make sure to {technobabble}.',
            'It should {technobabble}.'],

        'create': ['write', 'make', 'create'],
        'redo': ['rewrite', 'redo', 'update'],

        'does': ['will'],

        'former_lab': ['{filename} from Lab {gen/number}'],

        'technobabble': ['include the lessons learned in {former_lab}',
            'use {weird_cmd}', 'include support for {prog_things}',
            'catch errors involving {prog_things,nouns}'],

        'math': ['{math_word} ${mathbabble}$'],
        'math_word': ['calculate', 'invert', 'integrate'],
        'mathbabble': ['y = {mathbabble}', '{mathbabble}x',
            '{gen/number}^{gen/number}', '{gen/number}/{gen/number}',
            '{mathbabble}{gen/consonant,gen/vowel}_{gen/consonant,gen/vowel}',
            '{mathbabble} ({mathbabble})'],

        'extra_req': [],
    },

    'old_words' : {
        'template' : ['{old_disease}', '{old_units}', '{old_technology}',
            '{old_science}'],

        #Source: http://en.wikipedia.org/wiki/List_of_deprecated_terms_for_diseases
        'old_disease' : ['apoplexy', 'bilious', 'consumption', 'dropsy',
        'front-street', 'gleet', 'grippe', 'lockjaw', 'norwalk', 'phthisis',
        'quinsy', 'squinsy', 'undulant'],

        #Source: http://en.wikipedia.org/wiki/Category:Obsolete_units_of_measurement
        'old_units' : ['abucco', 'adowlie', 'angula', 'atom', 'bahar', 'buddam',
            'carcel', 'carucate', 'cawnie', 'chungah', 'coomb', 'corgee',
            'cubit', 'cullingey', 'cullishigay', 'delisle', 'dessiatin',
            'dharni', 'dirham', 'ell', 'fanega', 'firlot', 'garce', 'girah',
            'grzywna', 'guz', 'hekat', 'hobbit', 'homer', 'juchart', 'katha',
            'koku', 'kula', 'ligne', 'mache', 'marabba', 'metretes', 'morgen',
            'munjandie', 'oka', 'oxgang', 'peck', 'perch', 'poncelet', 'pood',
            'spat', 'toise', 'unglie', 'wey', 'yojana', 'zentner', 'zolotnik',
            'ordlach'],

        #Source: http://en.wikipedia.org/wiki/Category:Obsolete_technologies
        'old_technology' : ['ballista', 'calculagraph', 'carriage', 'catapult',
            'kinescope', 'mimeograph', 'multi-image', 'pulse-dial', 'rotary',
            'stauroscope', 'sundial'],

        #Source: http://en.wikipedia.org/wiki/Category:Obsolete_scientific_theories
        'old_science' : ['adamic', 'aether', 'antiperistasis', 'barlow',
            'caloric', 'corpuscular', 'cyclol', 'dark-star', 'dualism',
            'enochian', 'etheric', 'firmament', 'galactocentrism', 'geohumoral',
            'vacui', 'imponderable', 'japhetic', 'quasar', 'lescarbault',
            'limbic', 'luminiferous', 'milne', 'phrenol', 'polflucht',
            'recapitulation', 'reticular', 'sublunary', 'impetus',
            'thomson-berthelot', 'troidal', 'trepidation', 'tychonic',
            'vulcan'],

        #Possible other source: http://en.wikipedia.org/wiki/Category:Obsolete_taxonomic_groups, http://en.wikipedia.org/wiki/Category:Modern_obsolete_currencies, http://en.wikipedia.org/wiki/Category:Former_entities
  },
}