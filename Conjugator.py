import re

INFINITIVE = 'tocar'  # input('Input a verb infinitive: ')
STEM = INFINITIVE[:-2]
END = INFINITIVE[-2:]


def build_stem(infinitive, mood, tense, person):
    stem = infinitive[:-2]
    end = infinitive[-2:]

    # C to ZC change
    if (mood == 'Indicative' and tense == 'Present' and person == '1s') or (
            mood == 'Subjunctive' and tense == 'Present' and person in ['1s', '2s', '3s', '1p', '2p', '3p']):

        if (infinitive.endswith('cer')) and (not infinitive.endswith('ercer')):
            if (len(re.findall('[aeiou][aeiouy]*', stem)) >= 2) or (infinitive.endswith('acer')):
                return re.sub('c$', 'zc', stem)

        elif infinitive.endswith('ucir'):
            return re.sub('c$', 'zc', stem)

    # Basic orthographic corrections
    if (mood == 'Indicative' and tense == 'Preterite' and person == '1s') or \
            (mood == 'Subjunctive' and tense == 'Present' and person in ['1s', '2s', '3s', '1p', '2p', '3p']):
        if end == 'ar':
            ar_stem_ends = {'c': 'qu', 'g': 'gu', 'gu': 'gü', 'z': 'c'}
            for i in ar_stem_ends:
                stem = re.sub(f'{i}$', f'{ar_stem_ends[i]}', stem)

    elif (mood == 'Indicative' and tense == 'Present' and person == '1s') or \
            (mood == 'Subjunctive' and tense == 'Present' and person in ['1s', '2s', '3s', '1p', '2p', '3p']):

        if end == 'er':
            stem_ends = {'c': 'z', 'g': 'j'}
            for i in stem_ends:
                stem = re.sub(f'{i}$', f'{stem_ends[i]}', stem)

        elif end == 'ir':
            stem_ends = {'c': 'z', 'g': 'j', 'ug': 'g', 'qu': 'c'}
            for i in stem_ends:
                stem = re.sub(f'{i}$', f'{stem_ends[i]}', stem)

    # Add -y before -i if vowel ends with uir
    if not (infinitive.endswith(('guir', 'quir'))) and infinitive.endswith('uir'):
        if mood == 'Indicative':
            if ((tense == 'Present') and (person in ['1s', '2s', '3s', '3p'])) or (
                    (tense == 'Preterite') and (person in ['3s', '3p'])):
                return re.sub('u$', 'uy', stem)

        elif mood == 'Subjunctive':
            if (tense == 'Present') and (person in ['1s', '2s', '3s', '1p', '2p', '3p']):
                return re.sub('u$', 'uy', stem)

        elif (mood == 'Participles') and (tense == 'Present'):
            return re.sub('u$', 'uy', stem)

    # def stemchange(temp_stem, infinitive, mood, tense, person):
    #     END = infinitive[-2:]
    #     diphthong_verbs_o = ('mostrar', 'mover', 'dormir')
    #     diphthong_verbs_e = ('pensar', 'perder')
    #     umlaut_verbs_o = ('dormir')
    #
    #     def diphthong_o(stem):
    #         # if INFINITIVE in PLACEHOLDER_LIST:
    #         stem = stem.replace('o', 'eu', 1)[::-1]
    #         if stem.startswith('ue'):
    #             return stem.replace('ue', 'hue', 1)
    #         return stem
    #
    #     def diphthong_e(stem):
    #         # if INFINITIVE in PLACEHOLDER_LIST:
    #         stem = stem.replace('e', 'ei', 1)[::-1]
    #         if stem.startswith('ie'):
    #             return stem.replace('ie', 'ye', 1)
    #         return stem
    #
    #     def umlaut_o(stem):
    #         return stem[::-1].replace('o', 'u', 1)[::-1]
    #
    #     def umlaut_e(stem):
    #         return stem[::-1].replace('e', 'i', 1)[::-1]
    #
    #     for i in temp_stem[::-1]:
    #
    #         if (i == 'e') or (i == 'o'):
    #             STEM_VOWEL = i
    #
    #             if (END == 'ar') or (END == 'er'):
    #                 if (mood == 'Indicative' or 'Subjunctive') and (tense == 'Present') \
    #                         and (person in ['1s', '2s', '3s', '3p']):
    #                     if STEM_VOWEL == 'o':
    #                         if infinitive in diphthong_verbs_o:
    #                             return diphthong_o(temp_stem)
    #
    #                     if STEM_VOWEL == 'e':
    #                         if infinitive in diphthong_verbs_e:
    #                             return diphthong_e(temp_stem)
    #
    #             else:
    #                 if STEM_VOWEL == 'o':
    #                     if infinitive in umlaut_verbs_o:
    #                         if (mood == 'Indicative' or 'Subjunctive') and (tense == 'Present') \
    #                                 and (person in ['1s', '2s', '3s', '3p']):
    #                             return diphthong_o(temp_stem)[::-1]
    #
    #                         elif ((tense == 'Preterit') and (person in ['3s', '3p'])) \
    #                                 or (mood == 'Subjunctive', tense == 'Present', person in ['1p', '2p']):
    #                             return umlaut_o(temp_stem)
    #
    #                         else:
    #                             break
    #
    #                 if STEM_VOWEL == 'e':
    #                     if mood == 'Indicative':
    #                         if (tense == 'Present') and (person in ['1s', '2s', '3s', '3p']):
    #                             if temp_stem.endswith('nt'):
    #                                 return diphthong_e(temp_stem)
    #                             elif temp_stem.endswith('ed'):
    #                                 return umlaut_e(temp_stem)
    #                         elif (tense == 'Preterite') and (temp_stem.endswith('ed' or 'nt')) and (
    #                                 person in ['3s', '3p']):
    #                             return umlaut_e(temp_stem)
    #
    #                     elif (mood == 'Subjunctive') and (tense == 'Present'):
    #                         if temp_stem.endswith('nt'):
    #                             if person in ['1s', '2s', '3s', '3p']:
    #                                 return diphthong_e(temp_stem)
    #                             else:
    #                                 return umlaut_e(temp_stem)
    #
    #                         elif temp_stem.endswith('ed'):
    #                             return umlaut_e(temp_stem)
    #
    # if basicorthcorrections(final_stem, infinitive, mood, tense, person):
    #     final_stem = basicorthcorrections(final_stem, infinitive, mood, tense, person)
    #
    # if ctozc(final_stem, infinitive, mood, tense, person):
    #     final_stem = ctozc(final_stem, infinitive, mood, tense, person)
    #
    # if utouy(final_stem, infinitive, mood, tense, person):
    #     final_stem = utouy(final_stem, infinitive, mood, tense, person)
    #
    # if stemchange(final_stem, infinitive, mood, tense, person):
    #     final_stem = stemchange(final_stem, infinitive, mood, tense, person)

    return stem


CONJUGATION_TREE = {
    'Indicative': {
        'Present': {
            '1s': {'ar': 'o', 'er': 'o', 'ir': 'o', 'ír': 'o'},
            '2s': {'ar': 'as', 'er': 'es', 'ir': 'es', 'ír': 'es'},
            '3s': {'ar': 'a', 'er': 'e', 'ir': 'e', 'ír': 'e'},
            '1p': {'ar': 'amos', 'er': 'emos', 'ir': 'imos', 'ír': 'imos'},
            '2p': {'ar': 'áis', 'er': 'éis', 'ir': 'ís', 'ír': 'ís'},
            '3p': {'ar': 'an', 'er': 'en', 'ir': 'en', 'ír': 'en'}
        },
        'Preterite': {
            '1s': {'ar': 'é', 'er': 'í', 'ir': 'í', 'ír': 'í'},
            '2s': {'ar': 'aste', 'er': 'iste', 'ir': 'iste', 'ír': 'iste'},
            '3s': {'ar': 'ó', 'er': 'ió', 'ir': 'ió', 'ír': 'ió'},
            '1p': {'ar': 'amos', 'er': 'imos', 'ir': 'imos', 'ír': 'imos'},
            '2p': {'ar': 'asteis', 'er': 'isteis', 'ir': 'isteis', 'ír': 'isteis'},
            '3p': {'ar': 'aron', 'er': 'ieron', 'ir': 'ieron', 'ír': 'ieron'}
        },
        'Imperfect': {
            '1s': {'ar': 'aba', 'er': 'ía', 'ir': 'ía', 'ír': 'ía'},
            '2s': {'ar': 'abas', 'er': 'ías', 'ir': 'ías', 'ír': 'ías'},
            '3s': {'ar': 'aba', 'er': 'ía', 'ir': 'ía', 'ír': 'ía'},
            '1p': {'ar': 'ábamos', 'er': 'íamos', 'ir': 'íamos', 'ír': 'íamos'},
            '2p': {'ar': 'abais', 'er': 'íais', 'ir': 'íais', 'ír': 'íais'},
            '3p': {'ar': 'aban', 'er': 'ían', 'ir': 'ían', 'ír': 'ían'}
        },
        'Conditional': {
            '1s': {'ar': 'aría', 'er': 'ería', 'ir': 'iría', 'ír': 'iría'},
            '2s': {'ar': 'arías', 'er': 'erías', 'ir': 'irías', 'ír': 'irías'},
            '3s': {'ar': 'aría', 'er': 'ería', 'ir': 'iría', 'ír': 'iría'},
            '1p': {'ar': 'aríamos', 'er': 'eríamos', 'iríamos': 'ir', 'ír': 'iríamos'},
            '2p': {'ar': 'aríais', 'er': 'eríais', 'ir': 'iríais', 'ír': 'iríais'},
            '3p': {'ar': 'arían', 'er': 'erían', 'ir': 'irían', 'ír': 'irían'}
        },
        'Future': {
            '1s': {'ar': 'aré', 'er': 'eré', 'ir': 'iré', 'ír': 'iré'},
            '2s': {'ar': 'arás', 'er': 'erás', 'ir': 'irás', 'ír': 'irás'},
            '3s': {'ar': 'ará', 'er': 'erá', 'ir': 'irá', 'ír': 'irá'},
            '1p': {'ar': 'aremos', 'er': 'eremos', 'ir': 'iremos', 'ír': 'iremos'},
            '2p': {'ar': 'aréis', 'er': 'eréis', 'ir': 'iréis', 'ír': 'iréis'},
            '3p': {'ar': 'arán', 'er': 'erán', 'ir': 'irán', 'ír': 'irán'}
        },
    },
    'Subjunctive': {
        'Present': {
            '1s': {'ar': 'e', 'er': 'a', 'ir': 'a', 'ír': 'a'},
            '2s': {'ar': 'es', 'er': 'as', 'ir': 'as', 'ír': 'as'},
            '3s': {'ar': 'e', 'er': 'a', 'ir': 'a', 'ír': 'a'},
            '1p': {'ar': 'emos', 'er': 'amos', 'ir': 'amos', 'ír': 'amos'},
            '2p': {'ar': 'éis', 'er': 'áis', 'ir': 'ás', 'ír': 'ás'},
            '3p': {'ar': 'en', 'er': 'an', 'ir': 'an', 'ír': 'an'}
        },
        'Imperfect 1': {
            '1s': {'ar': 'ara', 'er': 'iera', 'ir': 'iera', 'ír': 'iera'},
            '2s': {'ar': 'aras', 'er': 'ieras', 'ir': 'ieras', 'ír': 'ieras'},
            '3s': {'ar': 'ara', 'er': 'iera', 'ir': 'iera', 'ír': 'iera'},
            '1p': {'ar': 'ara', 'er': 'iéramos', 'ir': 'iéramos', 'ír': 'iéramos'},
            '2p': {'ar': 'áramos', 'er': 'ierais', 'ir': 'ierais', 'ír': 'ierais'},
            '3p': {'ar': 'aran', 'er': 'ieran', 'ir': 'ieran', 'ír': 'ieran', }
        },
        'Imperfect 2': {
            '1s': {'ar': 'ase', 'er': 'iese', 'ir': 'iese', 'ír': 'iese'},
            '2s': {'ar': 'ases', 'er': 'ieses', 'ir': 'ieses', 'ír': 'ieses'},
            '3s': {'ar': 'ase', 'er': 'iese', 'ir': 'iese', 'ír': 'iese'},
            '1p': {'ar': 'ásemos', 'er': 'iésemos', 'ir': 'iésemos', 'ír': 'iésemos'},
            '2p': {'ar': 'aseis', 'er': 'ieseis', 'ir': 'ieseis', 'ír': 'ieseis'},
            '3p': {'ar': 'asen', 'er': 'iesen', 'ir': 'iesen', 'ír': 'iesen'}
        },
        'Future': {
            '1s': {'ar': 'are', 'er': 'iere', 'ir': 'iere', 'ír': 'iere'},
            '2s': {'ar': 'ares', 'er': 'ieres', 'ir': 'ieres', 'ír': 'ieres'},
            '3s': {'ar': 'are', 'er': 'iere', 'ir': 'iere', 'ír': 'iere'},
            '1p': {'ar': 'áremos', 'er': 'iéremos', 'ir': 'iéremos', 'ír': 'iéremos'},
            '2p': {'ar': 'aremos', 'er': 'iereis', 'ir': 'iereis', 'ír': 'iereis'},
            '3p': {'ar': 'aren', 'er': 'ieren', 'ir': 'ieren', 'ír': 'ieren'}
        },
    },

    'Imperative': {
        'Positive': {
            '2s': {'ar': 'a', 'er': 'e', 'ir': 'e', 'ír': 'e'},
            '3s': {'ar': 'e', 'er': 'a', 'ir': 'a', 'ír': 'a'},
            '1p': {'ar': 'emos', 'er': 'amos', 'ir': 'amos', 'ír': 'amos'},
            '2p': {'ar': 'ad', 'er': 'ed', 'ir': 'id', 'ír': 'id'},
            '3p': {'ar': 'en', 'er': 'an', 'ir': 'an', 'ír': 'an'}
        },
        'Negative': {
            '2s': {'ar': 'es', 'er': 'as', 'ir': 'as', 'ír': 'as'},
            '3s': {'ar': 'e', 'er': 'a', 'ir': 'a', 'ír': 'a'},
            '1p': {'ar': 'emos', 'er': 'amos', 'ir': 'amos', 'ír': 'amos'},
            '2p': {'ar': 'éis', 'er': 'áis', 'ir': 'ás', 'ír': 'ás'},
            '3p': {'ar': 'en', 'er': 'an', 'ir': 'an', 'ír': 'an'}
        }
    },

    # 'Participles': {
    #     'Present': {
    #         'N/A': ''
    #     },
    #     'Past': {
    #         'N/A': ''
    #     }
    # }
}

for MOOD in CONJUGATION_TREE:
    print(MOOD)
    for TENSE in CONJUGATION_TREE[MOOD]:
        print('\t' + TENSE)
        for PERSON in CONJUGATION_TREE[MOOD][TENSE]:
            STEM = build_stem(STEM, INFINITIVE, MOOD, TENSE, PERSON)
            print('\t\t' + PERSON + ': ' + CONJUGATION_TREE[MOOD][TENSE][PERSON][END])
