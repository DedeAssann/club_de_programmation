"""
_summary_

We'll try to write a module that translate texts from one language to another.

_extended_summary_
"""

from deep_translator import GoogleTranslator


def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.read()
        return lines


def get_text_from_input():
    "..."
    text = input("Input the text you wish too translate : ")
    return text


def traducteur(text: str) -> str:
    "..."
    target_language = input(
        "Input the language in which you wanna translate your text : "
    )
    translator = GoogleTranslator(source="auto", target=target_language)
    translated_text = translator.translate(text)
    return translated_text


if __name__ == "__main__":
    input(
        """Welcome! This program will help you translate any given text into different languages.\nPress
        Enter key to continue..."""
    )
    choice = input(
        """
        Choose one option (1-3) from the available options.
        1) Give a proper text to translate
        2) Translate an existing document
        3) Exit Program
        
        """
    )
    if int(choice) not in (1, 2, 3):
        print("\nInvalid Input!\nExiting Program.")
        exit(-1)
    elif int(choice) == 1:  # give a proper text for translation
        text = get_text_from_input()
        # traducteur(text)
        translated_text = traducteur(text)
        print(translated_text)
    elif int(choice) == 2:  # translate an existing document
        filepath = input("""Enter path to the Document : """)
        text = read_file(filepath)
        translated_text = traducteur(text)
        print("\n\n\n\n", translated_text)
    elif int(choice) == 3:
        exit(-1)
    else:
        pass
