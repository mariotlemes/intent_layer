import re

def extract_values_from_intent(nile_intent):
    # name_intent = 0
    # number_of_vfs = 0

    start = 'intent'
    end = 'Intent'

    start_index = nile_intent.find(start)
    end_index = nile_intent.find(end)

    if start_index != -1 and end_index != -1:
        name_intent = nile_intent[start_index + len(start):end_index].strip()

    result = re.search(r"middlebox\('(\d+)'\)", nile_intent)
    if result:
        number_of_vfs = result.group(1)
        # print(number_of_vfs)

        return name_intent, number_of_vfs



