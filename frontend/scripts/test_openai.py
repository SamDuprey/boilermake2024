import os
from openai import OpenAI
from decouple import config
import asyncio
def generate_story(subreddit):
  
    # gets the API key from the .env file
    OPENAI_API_KEY = config('OPENAI_API_KEY')
    client = OpenAI(api_key=OPENAI_API_KEY)

    user_message = f"Create a short example post that replicates the nature of stories in the subreddit r/{subreddit}. Make the post short, under 200 words. The story should contain crazy, scanalous topics that create discussion. But the narrator shouldn't ever directly say that the story is contraversial, as it is more effective to show than tell. In fact, avoid sounding corny at all costs, and do NOT say the phrase 'buckle up'"

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion.choices[0].message.content

##def main():
    ##subreddit_name = "TIFU"
    ##result = generate_story(subreddit_name)
    ##print(result)

##if __name__ == "__main__":
    ##main()
