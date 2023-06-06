import openai
from scraper import returnTitles



headlines = returnTitles()

for headline in headlines:
    prompt = f"What is your comment about {headline}?"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=64,
        n=1,
        stop=None,
        temperature=0.5,
    )
    comment = response.choices[0].text.strip()
    print(f"Comment about {headline}: {comment}")
