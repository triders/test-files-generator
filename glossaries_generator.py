from typing import Literal
from faker import Faker
import datetime


def get_word(min_length, faker_instance):
    word = faker_instance.word()
    if len(word) <= min_length:
        return get_word(min_length, faker_instance)
    return word


def generate_dnt_glossary(
        size: int,
        language: Literal["en_us", "ru_ru", "ja_jp", "fr_fr", "zh_tw", "zh_cn", "ar_aa", "pt_pt"] = "en_us",
        cs_types: tuple = ("lower", "upper", "regular", "cUstom", "custoM", "cUSTOM", "CUSTOm", "CustoM"),
        words_in_term=2,
        file_name="dnt"
):
    try:
        f = Faker(language)
    except:
        raise ValueError(f"Language {language} is not supported")

    dnt_list = []
    with open(f"{file_name}_{str(size)}_{language}_{len(cs_types)}_cs_types_{datetime.datetime.now()}.csv", "w") as file:
        for i in range(size):
            while True:
                # we need while True to avoid terms duplication; the loop breaks on the last line
                dnt_term = ""
                for _ in range(words_in_term):
                    dnt_term += get_word(4, f) + " "

                if dnt_term not in dnt_list:
                    dnt_list.append(dnt_term)
                else:
                    continue

                new_term_list = []
                if "lower" in cs_types:
                    new_term_list.append(dnt_term.lower())
                if "upper" in cs_types:
                    new_term_list.append(dnt_term.upper())
                if "regular" in cs_types:
                    new_term_list.append(dnt_term[0].upper() + dnt_term[1:].lower())
                if "cUstom" in cs_types:
                    new_term_list.append(dnt_term[0].lower() + dnt_term[1].upper() + dnt_term[2:].lower())
                if "custoM" in cs_types:
                    new_term_list.append(dnt_term[:-1].lower() + dnt_term[-1].upper())
                if "cUSTOM" in cs_types:
                    new_term_list.append(dnt_term[0].lower() + dnt_term[1:].upper())
                if "CUSTOm" in cs_types:
                    new_term_list.append(dnt_term[:-1].upper() + dnt_term[-1].lower())
                if "CustoM" in cs_types:
                    new_term_list.append(dnt_term[0].upper() + dnt_term[1:-1].lower()+ dnt_term[-1].upper())

                for term in new_term_list:
                    file.write(f"{term}\n")
                break


def generate_unidirectional_glossary(
        size: int,
        cs_types: tuple =("lower", "upper", "regular", "cUstom", "custoM", "cUSTOM", "CUSTOm", "CustoM"),
        source_language: Literal["en_us", "ru_ru", "ja_jp", "fr_fr", "zh_tw", "zh_cn", "ar_aa", "pt_pt"] = "en_us",
        target_language: Literal["en_us", "ru_ru", "ja_jp", "fr_fr", "zh_tw", "zh_cn", "ar_aa", "pt_pt"] = "ru_ru",
        words_in_term=2,
        file_name="unidir",
):
    try:
        f_source = Faker(source_language)
        f_target = Faker(target_language)
    except:
        raise ValueError(f"language pair {source_language}, {target_language}  is not supported")

    gloss_list = []
    with open(f"{file_name}_{str(size)}_{source_language}_{target_language}_{len(cs_types)}_cs_types_{datetime.datetime.now()}.csv", "w") as file:
        for i in range(size):
            while True:
                # we need while True to avoid terms duplication; the loop breaks on the last line
                source_term = ""
                target_term = ""
                for _ in range(words_in_term):
                     source_term += get_word(4, f_source) + " "
                for _ in range(words_in_term):
                    target_term += get_word(4, f_target) + " "

                uni_term = source_term[:-1] + "," + target_term[:-1]

                if uni_term not in gloss_list:
                    gloss_list.append(uni_term)
                else:
                    continue

                new_term_list = []
                if "lower" in cs_types:
                    new_term_list.append(uni_term.lower())
                if "upper" in cs_types:
                    new_term_list.append(uni_term.upper())
                if "regular" in cs_types:
                    uni_term_split = uni_term.split(",")
                    new_term_list.append(
                        uni_term_split[0][0].upper() + uni_term_split[0][1:].lower() + \
                        "," + \
                        uni_term_split[1][0].upper() + uni_term_split[1][1:].lower())
                if "cUstom" in cs_types:
                    uni_term_split = uni_term.split(",")
                    new_term_list.append(
                        uni_term_split[0][0].lower() + uni_term_split[0][1].upper() + uni_term_split[0][2:].lower() + \
                        "," + \
                        uni_term_split[1][0].lower() + uni_term_split[1][1].upper() + uni_term_split[1][2:].lower())

                if "custoM" in cs_types:
                    uni_term_split = uni_term.split(",")
                    new_term_list.append(
                        uni_term_split[0][:-1].lower() + uni_term_split[0][-1].upper() + \
                        "," + \
                        uni_term_split[1][:-1].lower() + uni_term_split[1][-1].upper())

                if "cUSTOM" in cs_types:
                    uni_term_split = uni_term.split(",")
                    new_term_list.append(
                        uni_term_split[0][0].lower() + uni_term_split[0][1:].upper() + \
                        "," + \
                        uni_term_split[1][0].lower() + uni_term_split[1][1:].upper())

                if "CUSTOm" in cs_types:
                    uni_term_split = uni_term.split(",")
                    new_term_list.append(
                        uni_term_split[0][:-1].upper() + uni_term_split[0][-1].lower() + \
                        "," + \
                        uni_term_split[1][:-1].upper() + uni_term_split[1][-1].lower())

                if "CustoM" in cs_types:
                    uni_term_split = uni_term.split(",")
                    new_term_list.append(
                        uni_term_split[0][0].upper() + uni_term_split[0][1:-1].lower() + uni_term_split[0][-1].upper() + \
                        "," + \
                        uni_term_split[1][0].upper() + uni_term_split[1][1:-1].lower() + uni_term_split[1][-1].upper())

                for term in new_term_list:
                    file.write(f"{term}\n")
                break


if __name__ == "__main__":

    generate_dnt_glossary(
        size=1000,
        language="en_us",
        cs_types=("lower", "upper", "regular", "cUstom", "custoM", "cUSTOM", "CUSTOm", "CustoM"),
        words_in_term=2
    )

    generate_unidirectional_glossary(
        size=1000,
        source_language="en_us",
        target_language="pt_pt",
        cs_types=("lower", "upper", "regular", "cUstom", "custoM", "cUSTOM", "CUSTOm", "CustoM"),
        words_in_term=2,
    )
