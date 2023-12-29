from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def ask_chatgpt(message):
    client = OpenAI(
    api_key= os.getenv("GPT3_API_KEY")
    # api_key= st.secrets["GPT3_API_KEY"]
)

    MODEL_NAME = "gpt-3.5-turbo"
    query = generate_query(message)
    # print(query)
    # st.write(query)

    response = client.chat.completions.create(
            model = MODEL_NAME,
            messages = [
                {"role": 'system', "content": query} #our query 
            ]
        )
    # print(response)
    gpt_response = {}
    gpt_response['response'] = response.choices[0].message.content
    gpt_response['text_received_to_gpt'] = message
    gpt_response['completion_tokens'] = response.usage.completion_tokens
    gpt_response['prompt_tokens'] = response.usage.prompt_tokens
    gpt_response['total_tokens'] = response.usage.total_tokens
    gpt_response['model'] = MODEL_NAME
    # st.header(gpt_response['completion_tokens'])
    # st.header(gpt_response['prompt_tokens'])
    # st.header(gpt_response['total_tokens'])
    # print('*********** GPT RESPONSE *************')
    # print(gpt_response)
    return gpt_response


def generate_query(data):
    query = f'''You are an expert system in identifying named entities and infer values and labels. Based on the below information extract the entities like list of job roles the user is eligible for ,Name, Phone Number, Email, Skills, Experience, Projects. Give output as the dictionary only

    {data}
    '''
    # st.write('This is the query asked to chagpt')
    # st.write(query)
    return query