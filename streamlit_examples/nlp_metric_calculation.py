import pandas as pd
from functools import reduce
import openpyxl
import evaluate

removeWords = ["\nAssistant:", "\nBot:", "\nHuman:", '\nSystem']


def get_formatted_answers(answers_per_sheet:list):
    final_answer_list = []
    for answers in answers_per_sheet:
           answers = str(answers)
           for sub in removeWords:
               answers = answers.replace(sub, "")
           final_answer_list.append(answers)
    return final_answer_list
    
    
def calc_rouge_score(path, reference):
    
    df = pd.read_excel(path, sheet_name= None)
    sheets = list(df.keys())
    results = {}
    for sheet_name in sheets:
        anwsers =  df[sheet_name]["Answers"]
        predictions = get_formatted_answers(anwsers)
        rouge = evaluate.load('rouge')
        #    results = rouge.compute(predictions= predictions, references= reference)
        # print(predictions)
        results[sheet_name] = rouge.compute(predictions= predictions, references= reference)
       ## now calculate the predictions
    print(results)   
       
    
          
          
       
        

def get_reference_list():
    path = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\benchmark_qa_3_temp_zero\1+gpt35turbo+snowflake-arctic-embed-m.xlsx"

    wb_obj = openpyxl.load_workbook(path)
    sheets = wb_obj.sheetnames
    df = pd.read_excel(path, sheet_name= sheets)
    keys = df.keys()

    final_answer_list = []
    first_list = df["snowflakeArctic"]["Answers"]
    second_list = df["bgebase"]["Answers"]
    third_list = df["gteBase"]["Answers"]


    for i in range(20):
        # print(i)
        test = []
        test.append(first_list[i])    
        test.append(second_list[i])    
        test.append(third_list[i])
        final_answer_list.append(test)

    references = final_answer_list
    return references       
    
    


if __name__ == "__main__":
    reference  = get_reference_list()
    
    # prediction_path = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\benchmark_qa_3_temp_zero\all_llama-2-7b-chat.Q6_K.gguf_responses.xlsx"
    # prediction_path = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\benchmark_qa_2\1+Mistral-7B-Instruct-v0.3.Q4_K_M.gguf+snowflake-arctic-embed-m.xlsx"
    # prediction_path = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\benchmark_qa_2\2+Mistral-7B-Instruct-v0.3.Q4_K_M.gguf+bge-base-en-v1.5.xlsx"
    # prediction_path = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\benchmark_qa_2\3+Mistral-7B-Instruct-v0.3.Q4_K_M.gguf+gte-base-en-v1.5.xlsx"
    # prediction_path = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\benchmark_qa_2\4+llama-2-7b-chat.Q4_K_M.gguf+snowflake-arctic-embed-m.xlsx"
    # prediction_path = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\benchmark_qa_2\5+llama-2-7b-chat.Q4_K_M.gguf+bge-base-en-v1.5.xlsx"
    prediction_path = r"D:\OneDrive - Adani\Desktop\LEARNING_FOLDER\_Kolkata_2024\1_LLM\3_Text_query_bot\_docs\benchmark_qa_2\6+llama-2-7b-chat.Q4_K_M.gguf+gte-base-en-v1.5.xlsx"
    calc_rouge_score(prediction_path,reference)
    