import re
import tests

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

def match_nsd_descriptor (name_intent, number_vfs):
    # print(number_vfs)
    if number_vfs == str(2):
        print("------------------------------------------------------------------------------")
        print("Getting starting - Onboarding and Instantiating Process")
        tests.onboarding_and_instantiation(1, name_intent, 4)
    if number_vfs == str(3):
        print("------------------------------------------------------------------------------")
        print("Getting starting - Onboarding and Instantiating Process")
        tests.onboarding_and_instantiation(1, name_intent, 5)
    if number_vfs == str(4):
        print("------------------------------------------------------------------------------")
        print("Getting starting - Onboarding and Instantiating Process")
        tests.onboarding_and_instantiation(1, name_intent, 6)
    if number_vfs == str(5):
        print("------------------------------------------------------------------------------")
        print("Getting starting - Onboarding and Instantiating Process")
        tests.onboarding_and_instantiation(1, name_intent, 7)
    if number_vfs == str(6):
        print("------------------------------------------------------------------------------")
        print("Getting starting - Onboarding and Instantiating Process")
        tests.onboarding_and_instantiation(1, name_intent, 8)