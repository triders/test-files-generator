from typing import Literal
from faker import Faker
import datetime
import random


def generate_dnt_glossary(
        size: int,
        language: Literal["en_us", "ru_ru", "ja_jp", "fr_fr", "zh_tw", "zh_cn", "ar_aa", "pt_pt"] = "en_us",
        cs_types: list = ["lower", "upper", "regular", "cUstom", "custoM", "cUSTOM", "CUSTOm", "CustoM"],
        file_name="dnt"
):
    f = Faker(language)
    dnt_list = []
    with open(f"{file_name}_{str(size)}_{language}_{len(cs_types)}_cs_types_{datetime.datetime.now()}.csv", "w") as file:
        for i in range(size):
            while True:
                dnt_term = f"{f.word()} {f.word()}"
                if dnt_term not in dnt_list:
                    dnt_list.append(dnt_term)
                else:
                    continue

                new_term_list = []
                if "lower" in cs_types:
                    new_term_list.append(dnt_term)  # already in lowercase
                if "upper" in cs_types:
                    new_term_list.append(dnt_term.upper())
                if "regular" in cs_types:
                    new_term_list.append(dnt_term[0].upper() + dnt_term[1:])
                if "cUstom" in cs_types:
                    new_term_list.append(dnt_term[0].lower() + dnt_term[1].upper() + dnt_term[2:])
                if "custoM" in cs_types:
                    new_term_list.append(dnt_term[:-1].lower() + dnt_term[-1].upper())
                if "cUSTOM" in cs_types:
                    new_term_list.append(dnt_term[0].lower() + dnt_term[1:].upper())
                if "CUSTOm" in cs_types:
                    new_term_list.append(dnt_term[:-1].upper() + dnt_term[-1].lower())
                if "CustoM" in cs_types:
                    new_term_list.append(dnt_term[0].upper() + dnt_term[1:-1].lower()+ dnt_term[-1].upper())

                if i == size - 1:
                    break
                for term in new_term_list:
                    file.write(f"{term}\n")
                break


def generate_unidirectional_glossary(
        size: int,
        cs_types: list = ["lower", "upper", "regular", "custom"],
        source_language: Literal["en_us", "ru_ru", "ja_jp", "fr_fr", "zh_tw", "zh_cn", "ar_aa", "pt_pt"] = "en_us",
        target_language: Literal["en_us", "ru_ru", "ja_jp", "fr_fr", "zh_tw", "zh_cn", "ar_aa", "pt_pt"] = "ja_jp",
        file_name="unidir",
):
    f_source = Faker(source_language)
    f_target = Faker(target_language)

    gloss_list = []
    with open(f"{file_name}_{str(size)}_{source_language}_{target_language}_{datetime.datetime.now()}.csv", "w") as file:
        for i in range(size):
            while True:
                uni_term = f"{f_source.word()} {f_source.word()}, {f_target.word()} {f_target.word()}"
                term_cs_type = random.choice(cs_types)

                if term_cs_type == "lower":
                    pass  # already in lowercase
                elif term_cs_type == "upper":
                    uni_term = uni_term.upper()
                elif term_cs_type == "regular":
                    uni_term_split = uni_term.split(", ")
                    uni_term = uni_term_split[0][0].upper() + uni_term_split[0][1:] + \
                               ", " + \
                               uni_term_split[1][0].upper() + uni_term_split[1][1:]
                elif term_cs_type == "custom":
                    uni_term_split = uni_term.split(", ")
                    uni_term = uni_term_split[0][0].lower() + uni_term_split[0][1].upper() + uni_term_split[0][2:] + \
                               ", " + \
                               uni_term_split[1][0].lower() + uni_term_split[1][1].upper() + uni_term_split[1][2:]

                if uni_term not in gloss_list:
                    if i == size - 1:
                        file.write(f"{uni_term}")
                        break
                    file.write(f"{uni_term}\n")
                    gloss_list.append(uni_term)
                    break


if __name__ == "__main__":
    generate_dnt_glossary(
        size=5,
        language="en_us",
        cs_types=["lower", "upper", "regular", "cUstom", "custoM", "cUSTOM", "CUSTOm", "CustoM"]
    )
    # generate_dnt_glossary(100, language="en_us", cs_types=["lower", "upper", "regular", "custom"])
    # generate_unidirectional_glossary(100, source_language="en_us", target_language="ru_ru", cs_types=["lower", "upper", "custom"])
    # generate_unidirectional_glossary(10, source_language="ru_ru", target_language="pt_pt", cs_types=["custom"])
