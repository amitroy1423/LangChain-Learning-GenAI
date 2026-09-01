from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

st.header("Research Tool")

# user_input = st.text_input("Enter your prompt")
#User selects the research paper, explanation style, and length from dropdowns
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

#design a template/prompt template that incorporates the user selections
# template
template = load_prompt("template.json")  # Load the template from the JSON file
# there are two ways to load the template, one is to use the load_prompt function and the other is to use the PromptTemplate class directly. The load_prompt function is a convenient way to load a template from a JSON file, while the PromptTemplate class allows you to create a template from scratch.
#To generate the json file, creating a different script called prompt_generator.py that creates the template and saves it to a json file. The prompt_ui.py script then loads the template from the json file and uses it to generate the prompt based on user inputs.


# #fill the placeholder/template with user inputs
# prompt = template.invoke({
#     'paper_input': paper_input,
#     'style_input': style_input,
#     'length_input': length_input
# })

# if st.button("Summarize"):
#     result = model.invoke(prompt)
#     st.write(result.text)


# no need to use 2 times invoke, we can use the pipe operator to chain the prompt and model together and then invoke the chain with the user inputs. This is more efficient and cleaner than invoking the prompt and model separately.Invoking the chain and passing the user inputs as a dictionary to the invoke method of the chain will automatically fill the placeholders in the template with the user inputs and generate the final prompt that is passed to the model for processing.
if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.text)