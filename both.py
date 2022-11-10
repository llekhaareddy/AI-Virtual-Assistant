import wikipedia
import wolframalpha

while True:
    user_input = input("Question: ")

    try:
        app_id = "4U5XKV-Y973PYUR8W"
        client = wolframalpha.Client(app_id)
        res = client.query(user_input)
        answer = next(res.results).text
        print(answer)
    except:
        print(wikipedia.summary(user_input, auto_suggest=False))
    