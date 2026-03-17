from copy import deepcopy
from node import Node
from divas_data import divas

ATTRIBUTE_PRIORITY = [
    "tipo_ato",
    "debut",
    "origem",
    "estilo",
    "visual",
    "etnia",
    "veio_de_grupo",
    "reality",
    "atriz",
    "idioma",
]

BOOLEAN_ATTRIBUTES = {"veio_de_grupo", "reality", "atriz"}


def make_question(attr, value):
    if attr == "tipo_ato":
        if value == "grupo":
            return "É um grupo?"
        return "É uma artista solo?"

    if attr == "debut":
        return f"Estreou nos anos {value.replace('s', '')}?"

    if attr == "origem":
        mapping = {
            "eua": "É dos Estados Unidos?",
            "reino_unido": "É do Reino Unido?",
            "colombia": "É da Colômbia?",
            "barbados": "É de Barbados?",
            "canada": "É do Canadá?",
            "global": "É um grupo/global act multinacional?",
            "suecia": "É da Suécia?",
            "africa": "É africana?",
            "espanha": "É da Espanha?",
            "brasil": "É do Brasil?",
        }
        return mapping.get(value, f"A origem é {value}?")

    if attr == "idioma":
        mapping = {
            "ingles": "Canta majoritariamente em inglês?",
            "espanhol": "Canta majoritariamente em espanhol?",
            "portugues": "Canta majoritariamente em português?",
        }
        return mapping.get(value, f"O idioma principal é {value}?")

    if attr == "estilo":
        mapping = {
            "pop": "O estilo principal é pop?",
            "rnb": "O estilo principal é R&B?",
            "rock_pop": "O estilo principal é pop rock?",
            "latino": "O estilo principal é latino?",
            "latin": "O estilo principal é latino?",
            "funk": "O estilo principal é funk?",
            "alt_pop": "O estilo principal é alt-pop?",
            "dance_pop": "O estilo principal é dance-pop?",
        }
        return mapping.get(value, f"O estilo principal é {value}?")

    if attr == "visual":
        mapping = {
            "loira": "É mais associada a visual loiro?",
            "morena": "É mais associada a visual moreno?",
            "ruiva": "É mais associada a visual ruivo?",
            "alternativo": "Tem visual alternativo/excêntrico?",
            "misto": "O visual do grupo é misto?",
        }
        return mapping.get(value, f"O visual é {value}?")

    if attr == "etnia":
        mapping = {
            "branca": "É branca?",
            "negra": "É negra?",
            "asiatica": "É asiática?",
            "misto": "O grupo tem etnia mista?",
        }
        return mapping.get(value, f"A etnia é {value}?")

    if attr == "veio_de_grupo":
        return "Veio de um grupo?"

    if attr == "reality":
        return "Ficou famosa por reality show / competição?"

    if attr == "atriz":
        return "Também é atriz?"

    return f"{attr} = {value}?"


def get_distinct_values(candidates, attr, excluded_values=None):
    if excluded_values is None:
        excluded_values = set()

    values = []
    for _, data in candidates.items():
        value = data.get(attr)
        if value not in excluded_values and value not in values:
            values.append(value)
    return values


def choose_best_value_for_attribute(candidates, attr, excluded_values=None):
    if excluded_values is None:
        excluded_values = set()

    values = get_distinct_values(candidates, attr, excluded_values)

    if len(values) <= 1:
        return None

    if attr in BOOLEAN_ATTRIBUTES and True in values:
        yes_count = sum(1 for _, data in candidates.items() if data.get(attr) is True)
        no_count = len(candidates) - yes_count
        if yes_count > 0 and no_count > 0:
            return True

    best_value = None
    best_score = None

    for value in values:
        yes_count = sum(1 for _, data in candidates.items() if data.get(attr) == value)
        no_count = len(candidates) - yes_count

        if yes_count == 0 or no_count == 0:
            continue

        score = abs(yes_count - no_count)

        if best_score is None or score < best_score:
            best_score = score
            best_value = value

    return best_value


def build_decision_tree(candidates=None, attr_index=0, excluded=None):
    if candidates is None:
        candidates = divas

    if excluded is None:
        excluded = {}

    names = list(candidates.keys())

    if len(names) == 1:
        return Node(answer=names[0], candidates=names)

    if len(names) == 0:
        return Node(answer="Nenhuma diva encontrada", candidates=[])

    for idx in range(attr_index, len(ATTRIBUTE_PRIORITY)):
        attr = ATTRIBUTE_PRIORITY[idx]
        excluded_values = excluded.get(attr, set())
        value = choose_best_value_for_attribute(candidates, attr, excluded_values)

        if value is None:
            continue

        question = make_question(attr, value)
        node = Node(question=question, candidates=names)

        yes_candidates = {
            name: data for name, data in candidates.items()
            if data.get(attr) == value
        }

        no_candidates = {
            name: data for name, data in candidates.items()
            if data.get(attr) != value
        }

        node.yes = build_decision_tree(
            yes_candidates,
            attr_index=idx + 1,
            excluded=deepcopy(excluded)
        )

        no_excluded = deepcopy(excluded)
        if attr not in no_excluded:
            no_excluded[attr] = set()
        no_excluded[attr].add(value)

        node.no = build_decision_tree(
            no_candidates,
            attr_index=idx,
            excluded=no_excluded
        )

        return node

    return Node(answer=names if len(names) > 1 else names[0], candidates=names)


def get_root():
    return build_decision_tree(divas)
