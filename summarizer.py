import openai
openai.api_key = "enterAPIKey"
def summarize_results(results):
    prompt = "Summarize the following web search results:\n\n"
    for title, url in results:
        prompt += f"- {title} ({url})\n"
    prompt += "\nProvide a clear and concise summary:"

    response = openai.ChatCompletion.create(
        model="gpt-4",  
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    return response['choices'][0]['message']['content']