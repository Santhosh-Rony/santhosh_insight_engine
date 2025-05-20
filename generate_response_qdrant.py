from openai import OpenAI
from decouple import config
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
            base_url=config("LLM_PROXY_ENDPOINT"),
            api_key=config("LLM_PROXY_API_KEY"),
        ) 

# Uncomment this and comment out the proxy block above if you want to use OpenAI's key.
# client = OpenAI(
#     api_key=config("OPENAI_API_KEY"),  # Make sure to add OPENAI_API_KEY in your .env
# )

def generate_response_from_qdrant(query_text, retrieved_texts):
    try:
        
        context = "\n".join(retrieved_texts)
        prompt = f"Context:\n{context}\n\nQuestion: {query_text}\nAnswer:"

        response = client.chat.completions.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],  
            temperature=0.5,  
        )
        
        answer = response.choices[0].message.content.strip()
        
        print(f"Generated answer: {answer}")
        return answer
        

    except Exception as e:
        print(f"Error generating response: {e}")
        return "I'm sorry, I couldn't generate a response at this time."