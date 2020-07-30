from os.path import join

from jpype import JClass, getDefaultJVMPath, shutdownJVM, startJVM

if __name__ == '__main__':

    zemberek_path: str = join('..', '..', 'Dependencies', 'Zemberek-Python', 'bin', 'zemberek-full.jar')

    try:
        startJVM(
            getDefaultJVMPath(),
            '-ea',
            f'-Djava.class.path={zemberek_path}',
            convertStrings=False
        )
    except:
        exit(False)


    TurkishSentenceExtractor: JClass = JClass(
        'zemberek.tokenization.TurkishSentenceExtractor'
    )

    extractor: TurkishSentenceExtractor = TurkishSentenceExtractor.DEFAULT

    sentences = extractor.fromParagraph((
        'Prof. Dr. Veli Davul açıklama yaptı. Kimse %6.5 lik enflasyon oranını beğenmemiş!'
        'Kimse %6.5 lik enflasyon oranını beğenmemiş!'
        'Oysa maçta ikinci olmuştuk... Değil mi?'
    ))

    for i, word in enumerate(sentences):
        print(f'Sentence {i+1}: {word}')

    try:
        shutdownJVM()
    except:
        exit(False)