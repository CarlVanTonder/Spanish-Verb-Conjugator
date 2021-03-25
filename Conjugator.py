import re

INFINITIVE = input('Input a verb infinitive: ')

def BUILD_STEM(stem, infinitive, mood, tense, person):
    final_stem = stem

    def basicorthcorrections(temp_stem, infinitive, mood, tense, person):
        end = infinitive[-2:]
        if (mood == 'Indicative', tense == 'preterite', person == '1s') or (mood == 'subjunctive', tense == 'present', person in ['1s','2s','3s','1p','2p','3p']):
            if end == 'ar':
                stem_ends = {'c':'uq', 'g':'ug', 'ug':'üg', 'z':'c'}
                for i in stem_ends:
                    if temp_stem.startswith(i):
                        return (temp_stem.replace(i, stem_ends[i], 1))[::-1]

        elif (mood == 'Indicative', tense == 'present', person == '1s') or (mood == 'subjunctive', tense == 'present', person in ['1s','2s','3s','1p','2p','3p']):
            if end == 'er':
                stem_ends = {'c':'z', 'g':'j'}
                for i in stem_ends:
                    if temp_stem.startswith(i):
                        return (temp_stem.replace(i, stem_ends[i], 1))[::-1]

            else:
                stem_ends = {'c':'z', 'g':'j', 'ug':'g', 'qu':'c'}
                for i in stem_ends:
                    if temp_stem.startswith(i):
                        return (temp_stem.replace(i, stem_ends[i], 1))[::-1]

    def ctozc(temp_stem, infinitive, mood, tense, person):
        if (mood == 'Indicative', tense == 'present', person == '1s') or (mood == 'subjunctive', tense == 'present', person in ['1s','2s','3s','1p','2p','3p']):
            def zc(stems):
                return stems[::1].replace('c','cz',1)[::-1]

            if (infinitive.endswith('cer')) and (not infinitive.endswith('ercer')):
                if len(re.findall(re.compile('[aeiou][aeiouy]*'), temp_stem)) >= 2:
                    return zc(temp_stem)

                elif infinitive.endswith('acer'):
                    return zc(temp_stem)

            elif infinitive.endswith('ucir'):
                return zc(temp_stem)

    def utouy(temp_stem, infinitive, mood, tense, person):
        def uy(temp_stem):
            return temp_stem[::-1].replace('u', 'yu', 1)[::-1]

        if not (infinitive.endswith(('guir', 'quir'))) and infinitive.endswith('uir'):
            if mood == 'Indicative':
                if ((tense == 'Present') and (person in ['1s', '2s', '3s', '3p'])) or ((tense == 'Preterite') and (person in ['3s', '3p'])):
                    return uy(temp_stem)

            elif mood == 'Subjunctive':
                if (tense == 'Present') and (person in ['1s', '2s', '3s', '1p', '2p', '3p']):
                    return uy(temp_stem)

            elif (mood == 'Participles') and (tense == 'Present'):
                return uy(temp_stem)

    def stemchange(temp_stem, infinitive, mood, tense, person):
        END = infinitive[-2:]
        diphthong_verbs_o = ('mostrar', 'mover', 'dormir')
        diphthong_verbs_e = ('pensar', 'perder')
        umlaut_verbs_o = ('dormir')

        def diphthong_o(stem):
            # if INFINITIVE in PLACEHOLDER_LIST:
            stem = stem.replace('o', 'eu', 1)[::-1]
            if stem.startswith('ue'):
                return stem.replace('ue', 'hue', 1)
            return stem

        def diphthong_e(stem):
            # if INFINITIVE in PLACEHOLDER_LIST:
            stem = stem.replace('e', 'ei', 1)[::-1]
            if stem.startswith('ie'):
                return stem.replace('ie', 'ye', 1)
            return stem

        def umlaut_o(stem):
            return stem[::-1].replace('o', 'u', 1)[::-1]

        def umlaut_e(stem):
            return stem[::-1].replace('e', 'i', 1)[::-1]

        for i in temp_stem[::-1]:

            if (i == 'e') or (i == 'o'):
                STEM_VOWEL = i

                if (END == 'ar') or (END == 'er'):
                    if (mood == 'Indicative' or 'Subjunctive') and (tense == 'Present') \
                            and (person in ['1s', '2s', '3s', '3p']):
                        if STEM_VOWEL == 'o':
                            if infinitive in diphthong_verbs_o:
                                return diphthong_o(temp_stem)

                        if STEM_VOWEL == 'e':
                            if infinitive in diphthong_verbs_e:
                                return diphthong_e(temp_stem)

                else:
                    if STEM_VOWEL == 'o':
                        if infinitive in umlaut_verbs_o:
                            if (mood == 'Indicative' or 'Subjunctive') and (tense == 'Present') \
                                    and (person in ['1s', '2s', '3s', '3p']):
                                return diphthong_o(temp_stem)[::-1]

                            elif ((tense == 'Preterit') and (person in ['3s', '3p'])) \
                                    or (mood == 'Subjunctive', tense == 'Present', person in ['1p', '2p']):
                                return umlaut_o(temp_stem)

                            else:
                                break

                    if STEM_VOWEL == 'e':
                        if mood == 'Indicative':
                            if (tense == 'Present') and (person in ['1s', '2s', '3s', '3p']):
                                if temp_stem.endswith('nt'):
                                    return diphthong_e(temp_stem)
                                elif temp_stem.endswith('ed'):
                                    return umlaut_e(temp_stem)
                            elif (tense == 'Preterite') and (temp_stem.endswith('ed' or 'nt')) and (person in ['3s', '3p']):
                                return umlaut_e(temp_stem)

                        elif (mood == 'Subjunctive') and (tense == 'Present'):
                            if temp_stem.endswith('nt'):
                                if person in ['1s', '2s', '3s', '3p']:
                                    return diphthong_e(temp_stem)
                                else:
                                    return umlaut_e(temp_stem)

                            elif temp_stem.endswith('ed'):
                                return umlaut_e(temp_stem)

    if basicorthcorrections(final_stem, infinitive, mood, tense, person):
        final_stem = basicorthcorrections(final_stem, infinitive, mood, tense, person)

    if ctozc(final_stem, infinitive, mood, tense, person):
        final_stem = ctozc(final_stem, infinitive, mood, tense, person)

    if utouy(final_stem, infinitive, mood, tense, person):
        final_stem = utouy(final_stem, infinitive, mood, tense, person)

    if stemchange(final_stem, infinitive, mood, tense, person):
        final_stem = stemchange(final_stem, infinitive, mood, tense, person)

    return final_stem

print(BUILD_STEM('constru', 'construir', 'Indicative', 'Present', '1s'))

def CONJUGATE_VERB(INF, MOOD, TENSE, PERSON):
    STEM = INFINITIVE[:-2]
    END = INF[-2:]

    if MOOD == 'Indicative':
        if TENSE == 'Present':
            if PERSON == '1s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'o'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'o'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'o'

            if PERSON == '2s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'as'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'es'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'es'

            if PERSON == '3s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'a'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'e'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'e'

            if PERSON == '1p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'amos'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'emos'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'imos'

            if PERSON == '2p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'áis'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'éis'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ís'

            if PERSON == '3p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'an'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'en'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'en'

        elif TENSE == 'Preterite':
            if PERSON == '1s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'é'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'í'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'í'

            if PERSON == '2s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'aste'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iste'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iste'

            if PERSON == '3s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ó'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ió'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ió'

            if PERSON == '1p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'amos'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'imos'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'imos'

            if PERSON == '2p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'asteis'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'isteis'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'isteis'

            if PERSON == '3p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'aron'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ieron'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ieron'

        elif TENSE == 'Imperfect':
            if PERSON == '1s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'aba'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ía'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ía'

            if PERSON == '2s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'abas'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ías'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ías'

            if PERSON == '3s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'aba'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ía'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ía'

            if PERSON == '1p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ábamos'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'íamos'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'íamos'

            if PERSON == '2p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'abais'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'íais'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'íais'

            if PERSON == '3p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'aban'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ían'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ían'

        elif TENSE == 'Conditional':
            if PERSON == '1s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'aría'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ería'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iría'

            if PERSON == '2s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'arías'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'erías'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'irías'

            if PERSON == '3s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'aría'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ería'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iría'

            if PERSON == '1p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'aríamos'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'eríamos'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iríamos'

            if PERSON == '2p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'aríais'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'eríais'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iríais'

            if PERSON == '3p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'arían'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'erían'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'irían'

        elif TENSE == 'Future':
            if PERSON == '1s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'aré'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'eré'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iré'

            if PERSON == '2s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'arás'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'erás'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'irás'

            if PERSON == '3s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ará'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'erá'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'irá'

            if PERSON == '1p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'aremos'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'eremos'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iremos'

            if PERSON == '2p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'aréis'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'eréis'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iréis'

            if PERSON == '3p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'arán'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'erán'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'irán'

    elif MOOD == 'Subjunctive':
        if TENSE == 'Present':
            if PERSON == '1s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'e'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'a'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'a'

            if PERSON == '2s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'es'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'as'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'as'

            if PERSON == '3s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'e'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'a'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'a'

            if PERSON == '1p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'emos'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'amos'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'amos'

            if PERSON == '2p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'éis'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'áis'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'áis'

            if PERSON == '3p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'en'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'an'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'an'

        elif TENSE == 'Imperfect 1':
            if PERSON == '1s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ara'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iera'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iera'

            if PERSON == '2s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'aras'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ieras'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ieras'

            if PERSON == '3s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ara'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iera'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iera'

            if PERSON == '1p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'áramos'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iéramos'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iéramos'

            if PERSON == '2p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'arais'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ierais'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ierais'

            if PERSON == '3p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'aran'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ieran'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ieran'

        elif TENSE == 'Imperfect 2':
            if PERSON == '1s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ase'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iese'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iese'

            if PERSON == '2s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ases'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ieses'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ieses'

            if PERSON == '3s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ase'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iese'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iese'

            if PERSON == '1p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ásemos'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iésemos'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iésemos'

            if PERSON == '2p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'aseis'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ieseis'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ieseis'

            if PERSON == '3p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'asen'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iesen'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iesen'

        elif TENSE == 'Future':
            if PERSON == '1s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'are'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iere'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iere'

            if PERSON == '2s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ares'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ieres'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ieres'

            if PERSON == '3s':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'are'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iere'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iere'

            if PERSON == '1p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'áremos'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iéremos'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iéremos'

            if PERSON == '2p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'areis'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iereis'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iereis'

            if PERSON == '3p':
                if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'aren'
                if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ieren'
                else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ieren'

    # elif MOOD == 'Imperative':
    #     if TENSE == 'Affirmative':
    #         if PERSON == '2s':
    #             if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #
    #         if PERSON == '3s':
    #             if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #
    #         if PERSON == '1p':
    #             if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #
    #         if PERSON == '2p':
    #             if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #
    #         if PERSON == '3p':
    #             if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #
    #     elif TENSE == 'Negative':
    #         if PERSON == '2s':
    #             if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #
    #         if PERSON == '3s':
    #             if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #
    #         if PERSON == '1p':
    #             if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #
    #         if PERSON == '2p':
    #             if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #
    #         if PERSON == '3p':
    #             if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #             else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + ''
    #
    # elif MOOD == 'Participles':
    #     if TENSE == 'Present':
    #         if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ando'
    #         if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iendo'
    #         else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'iendo'
    #
    #     elif TENSE == 'Past':
    #         if END == 'ar': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ado'
    #         if END == 'er': return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ido'
    #         else: return BUILD_STEM(STEM, INFINITIVE, MOOD, TENSE, PERSON) + 'ido'

    else: return None

CONJUGATOR_TREE = {
    'Indicative': {
        'Present': ['1s','2s','3s','1p','2p','3p'],
        'Preterite': ['1s','2s','3s','1p','2p','3p'],
        'Future': ['1s','2s','3s','1p','2p','3p'],
        'Imperfect': ['1s','2s','3s','1p','2p','3p'],
        'Conditional': ['1s','2s','3s','1p','2p','3p'],
    },
    'Subjunctive': {
        'Present': ['1s','2s','3s','1p','2p','3p'],
        'Imperfect 1': ['1s','2s','3s','1p','2p','3p'],
        'Imperfect 2': ['1s','2s','3s','1p','2p','3p'],
        'Future': ['1s','2s','3s','1p','2p','3p']
    },

    'Imperative': {
        'Positive': ['2s','3s','1p','2p','3p'],
        'Negative': ['2s','3s','1p','2p','3p']
    },

    'Participles': {
        'Present': {
            'N/A': ''
        },
        'Past': {
            'N/A': ''
        }
    }
}

for MOOD in CONJUGATOR_TREE:
    print(MOOD)
    for TENSE in CONJUGATOR_TREE[MOOD]:
        print('\t' + TENSE)
        for PERSON in CONJUGATOR_TREE[MOOD][TENSE]:
            print('\t\t' + PERSON + ': ' +  CONJUGATE_VERB(INFINITIVE, MOOD, TENSE, PERSON))
