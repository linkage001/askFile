from ooba_api import OobaApi
from tools import list_files_in_dir, read_pdf, save_to_csv
from questions import questions

ooba_api = OobaApi()

files = list_files_in_dir('CVs/GV')
results = []
for file in files:
    if 'pdf' not in file:
        continue
    content = read_pdf(file)
    name = file.split('/')[-1].split('.')[0]
    name = name.replace('-cv', '').replace('-', ' ').replace('  ', ' ').strip()
    print(name)

    item = {
        "name": name,
    }

    # ask age
    age_question = """What is the probable age of the person described in the CV above?"""
    prompt = f'{content}\n\n{age_question}'
    prompt = ooba_api.format_question(age_question, ooba_api.templates.chat_ml) + 'The probable age of the person is '
    age = ooba_api.complete(prompt, max_tokens=2)
    item['age'] = age

    # ask questions
    for question in questions:
        prompt = f'{content}\n\n{question.question}'
        prompt = ooba_api.format_question(prompt, ooba_api.templates.chat_ml) + 'Chosen answer: <<'
        answer = ooba_api.complete(prompt, max_tokens=1)
        try:
            item[question.question.split('\n')[0]] = question.options[answer]
        except Exception:
            pass

    results.append(item)

print(results)
save_to_csv(results, "results.csv")
