from langchain_community.llms.ctransformers import CTransformers
from langchain_openai import AzureChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from contanst import llm_path_list, embed_llm_path_list, LLModelSpecs
from langchain_huggingface import HuggingFaceEmbeddings
from utils import blog
from time import time
from utils import blog
from document_reader import DocumentReader
from question_answering import get_response

def print_llm_list(llm_list: list[LLModelSpecs]):
    print("List of available models:")
    for count in range(len(llm_list)):
        print(f"[{count}] {llm_list[count].model_file}")
        

def get_llm(): 

    #print llm list
    print_llm_list(llm_list= llm_path_list)
    
    # choose LLM
    llm_opn = int(input("Enter index of chosen model: "))
    
    dir = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models"
    
    if (llm_opn < 0 or llm_opn >= len(llm_path_list)):
        blog("Invalid input")
        return
    else:    
        blog(f"Chosen Model: {llm_path_list[llm_opn].model_file}")
        file_name = llm_path_list[llm_opn].model_file    
    
     
    start_time = time()
    llm =  CTransformers( model= dir, model_file = file_name, callbacks=[StreamingStdOutCallbackHandler()], config = {"context_length": 16000, "max_new_tokens": 3000})
    blog(f"LLM Initialisation time ----->{time() - start_time}")
    return llm
 
 

def get_embed_llm():
    print_llm_list(llm_list= embed_llm_path_list)
    
    llm_opn = int(input("Enter index of chosen model: "))
    
    if (llm_opn < 0 or llm_opn >= len(embed_llm_path_list)):
        blog("Invalid input")
        return
    else:    
        blog(f"Chosen Model: {embed_llm_path_list[llm_opn].model_file}")
        file_name = embed_llm_path_list[llm_opn].model_dir   
    
    start_time = time()
    embed_llm =  HuggingFaceEmbeddings(
            model_name = file_name,
            show_progress = True,
            model_kwargs = {"trust_remote_code": True})
    blog(f"Embed LLM Initialisation time ----->{time() - start_time}")
    return embed_llm    
        
    
def get_gpt_llm(): 
    
    OPENAI_API_BASE="https://ailabazopenaise.openai.azure.com"
    GPT_DEPLOYMENT_NAME="ailabgpt35turbo"
    OPENAI_API_KEY="07a2db3305d14f619202c549ca81b0d2"

    model = AzureChatOpenAI(
    azure_endpoint=OPENAI_API_BASE,
    openai_api_version="2023-09-15-preview",
    deployment_name =GPT_DEPLOYMENT_NAME,
    openai_api_key=OPENAI_API_KEY,
    openai_api_type="azure",
    temperature= 0 
    )    
    
    blog(f"Created Model ----> {model}")
    return model


query_list = [
                "What are the different types of leave mentioned in the document?",
                "Who is the sanctioning authority for granting leave to employees?",
                "What is the objective of providing leave to employees?",
                "How is leave earning calculated for employees?",
                "What is the Leave Year defined as in the document?",
                "Can employees avail leave without having leave credit?",
                "What are the conditions for employees to be entitled to leave?",
                "Can employees carry forward unused leave to the next year?",
                "How many public holidays are declared by businesses each year?",
                "What happens if employees do not choose optional holidays?",
                "What is the purpose of Exit Leave?",
                "Who can approve deviations from the leave rules?",
                "Are employees encouraged to work from home?",
                "What is the consequence of absence from work without sanctioned leave?",
                "Are employees entitled to special leave for parental benefits?",
                "What is the policy for employees joining or leaving in the middle of a Leave Year?",
                "Can employees encash their leave?",
                "Can employees choose their preferred holidays from the list of optional holidays?",
                "Who determines the list of optional holidays for employees to choose from?",
                "Are there any restrictions on the maximum leave balance that employees can accumulate?",
                ]


import pandas as pd
from contanst import available_docs
import pandas as pd



def add_data_time_comp(
    llm, embed_llm, llm_init_time, embed_init_itme, doc_name,
    vector_store, vector_creation_time,min_time, max_time,avg_time):

    file_path = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\accuracy_timecomp.xlsx"
    existing_file = file_path

    new_data = {
        "LLM":[llm],
        "Embed LLM":[embed_llm],
        "LLM init time": [llm_init_time],
        "Embed LLM init time": [embed_init_itme],
        "Document": [doc_name],
        "Vector store": [vector_store],
        "Vector store creation time":[vector_creation_time],
        "LLM response time(min)": [min_time],
        "LLM response time(max)": [max_time],
        "LLM response time(avg)" : [avg_time]
        
    }

    df_new = pd.DataFrame(new_data)

    ## Reading existing data
    df_existing = pd.read_excel(file_path)

    df_combined = pd.concat([df_existing,df_new],ignore_index=True)

    # Save the combined data to Excel
    df_combined.to_excel(existing_file, index = False) 
        

first_init =  True
def test():
    count = 1
    
    for llm in llm_path_list:
        
        
        blog(f"Iteration NUMBER ----> #{count}")
        start= time()
        dir = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\local_downloaded_models"
        # chosen_llm = CTransformers( model= dir,
        #                            model_file = llm.model_file,
        #                            callbacks=[StreamingStdOutCallbackHandler()],
        #                            config = {"context_length": 16000, "max_new_tokens": 3000,"temperature": 0})
        
        chosen_llm = get_gpt_llm()
        llm_init_time = (time() - start)
        blog(f"#Iteration ------ {count} LLM: {chosen_llm} ------> LLM init time ----> {llm_init_time}")
           
        first_init = True
        
        for embed_llm in embed_llm_path_list:
            response_time_list = []
            question_list = []
            answer_list = []
            
            if not first_init:
                start= time()
                # chosen_llm = CTransformers( model= dir, model_file = llm.model_file, callbacks=[StreamingStdOutCallbackHandler()], config = {"context_length": 16000, "max_new_tokens": 3000})
                chosen_llm = get_gpt_llm()
                llm_init_time = time() - start
                blog(f"#{count} LLM init time ----> {llm_init_time}")
                        
            start= time()                        
            chosen_embed_llm = HuggingFaceEmbeddings(
            model_name = embed_llm.model_dir,
            show_progress = True,
            model_kwargs = {"trust_remote_code": True})
            embed_llm_init_time = (time() - start)
            blog(f"#Iteration --------- {count}Embed LLM: {chosen_embed_llm} ------> LLM init time ----> {embed_llm_init_time}")
            
             
            doc_loading = DocumentReader()
            start = time()
            vector_store = doc_loading.load_document(embeddings=chosen_embed_llm)
            vector_store_creation_time = str(time() - start)
            blog(f"#Iteration ------- {count}Vector Store: {vector_store} ------> Vector store creation time ----> {vector_store_creation_time}")
            
            qa_retriever = vector_store.as_retriever()
            
            question_number =  1       
            for question in query_list:
                blog(f"Iteration: {count}--- Question number: {question_number}--- Question: {question}")
                start_time = time()
                response = get_response(llm=chosen_llm,retriever=qa_retriever,query=question)
                end_time = time()
                response_time_list.append((end_time-start_time))
                blog(f"Iteration: {count}--- Question number: {question_number} --------  Generated Response ------> {response.content}")
                question_list.append(question)
                answer_list.append(response.content)
                question_number +=1
                                
           
            min_time = min(response_time_list)
            max_time = max(response_time_list)
            avg_time = sum(response_time_list)/len(response_time_list)
            
           
           ### Adding to time complexity sheet 
            add_data_time_comp(
                # llm= llm.model_file,
                llm= "gpt-3.5-turbo",
                embed_llm= embed_llm.model_file,
                llm_init_time= llm_init_time,
                embed_init_itme= embed_llm_init_time,
                doc_name= available_docs[0].file_name,
                vector_store= "Chroma",
                vector_creation_time= vector_store_creation_time,
                min_time= min_time,
                max_time= max_time,
                avg_time= avg_time
            )
            
           ## Adding data to individual excel sheets
            llm_response = pd.DataFrame({
                "Question": question_list,
                "Answers": answer_list
            })
            file_name = f"{count}+{llm.model_file}+{embed_llm.model_file}.xlsx" 
            file_path = rf"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\benchmark_qa_3_temp_zero\{file_name}"
            llm_response.to_excel(excel_writer = file_path)    
            
            blog("After excel call----->")
            
            
            
            # add average response time
            first_init = False
            count += 1
            
            # clearing     
            question_list = []
            answer_list = []
            response_time_list = []
        
        
     
        
    


def reset_sheet():
    time_complexity_excel = pd.DataFrame({
    "LLM":[],
    "Embed LLM":[],
    "LLM init time": [],
    "Embed LLM init time": [],
    "Document": [],
    "Vector store": [],
    "Vector store creation time":[],
    "LLM response time(min)": [],
    "LLM response time(max)": [],
    "LLM response time(avg)" : []
})
    file_path = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\accuracy_timecomp.xlsx"

    time_complexity_excel.to_excel(file_path,sheet_name="all_time_complexities")
    
        
if __name__ == "__main__":
    # start = time.time()
    # time.sleep(3)
    # blog(type(str(time.time()- start)))
    reset_sheet()
    test()

    
    
    
                