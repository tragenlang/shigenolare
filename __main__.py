#!/usr/bin/env python3

from collections import namedtuple, OrderedDict
from flask import Flask, Markup, render_template, request
from tragen_dict import words

section_link = namedtuple('section_link', 'template_file message')

app = Flask(__name__)


section_files = OrderedDict([
    ('Dictionary', section_link('RenderDictionary.html', 'Dictionary of Trägen Words')),
    ('Grammar', section_link('Tragen_Grammar.html',
                             Markup('Grammar (including overviews of <i>Phonology, Morphology, and Syntax</i>)'))),
    ('History', section_link('Tragen_History.html', 'History')),
    ('Morphology', section_link('Tragen_Morphology.html', 'Morphology')),
    ('Phonetics', section_link('Phonetics.html', 'Phonology/Phonetics')),
    ('Syntax', section_link('Tragen_Syntax.html', 'Syntax')),
    ('Tragenovegi', section_link('Tragenovegi.html',
                                 Markup('<i><b>Trägenovégi</b></i> (the Trägen Writing System)'))),
    ('Vocabulary', section_link('VocabAndWordFormation.html', 'Vocabulary / Word Formation'))
    ])


@app.route('/')
def welcome():
    return render_template('ShigenolareWelcomePage.html',
                           section_files=section_files)


@app.route('/<section>')
def render_section(section):
    return render_template(section_files[section].template_file)


@app.route('/Dictionary')
def show_dictionary():
    if 'search' not in request.args:
        return render_template('RenderDictionary.html',
                               words=words,
                               type_styles={'word': 'tragen-word',
                                            'affix': 'tragen-affix',
                                            'postposition': 'postposition'},
                               num_defs=sum(len(defs) for defs in words.items()))
    else:
        return render_template('DictionarySearch.html',
                               search=request.args['search'])


if __name__ == '__main__':
    app.run(debug=__debug__)
