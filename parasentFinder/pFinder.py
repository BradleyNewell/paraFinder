import re

file = input("Enter file path:")
file = file + '.txt'
term = input("Enter search term:")
search_selection = input('Please enter "Sentence" to search for sentences including your search term or'
                         ' "Paragraph" to search for paragraphs including your search term: ')


def getText():
    with open(file, 'r', encoding='utf-8') as text:
        text = text.read()
        keyword = term
        try:
            if search_selection.title() == "Sentence":
                sentence = re.findall(r'([^.]*' + keyword + '[^.]*)', text)
                str(sentence)
                for line in sentence:
                    line = line.replace("\n", ' ')
                    print(line)

            elif search_selection.title() == "Paragraph":
                paragraph = re.findall(r'([^\n]*' + keyword + '[^\n]*)', text)

                print(paragraph)
            else:
                print("Please enter a valid search selection")
        except NameError:
            print("Enter valid name")


getText()



