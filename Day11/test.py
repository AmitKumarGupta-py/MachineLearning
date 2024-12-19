import gradio as gr
import pickle
#import numpy as np 
import pandas as pd 
import os 
os.chdir(r"C:\Users\dai\Desktop\S-AI\MachineLearning\Day11\Wisconsin")

def predict(Clump, UniCell_Size,Uni_CellShape, MargAdh, SEpith,BareN, BChromatin , NoemN , Mitoses):
    tst = pd.DataFrame([[Clump, UniCell_Size,Uni_CellShape, MargAdh, SEpith,BareN, BChromatin , NoemN , Mitoses]],
          columns=['Clump', 'UniCell_Size','Uni_CellShape', 'MargAdh', 'SEpith','BareN', 'BChromatin' , 'NoemN' , 'Mitoses'])    
    filehandler = open("stack_breast_cancer1.pkl", "rb")
    bm_loaded = pickle.load(filehandler)
    print(tst)
    return bm_loaded.predict(tst)[0] 
      

# demo = gr.Interface(
#     fn=predict,
#     inputs=["number"] * 9,
#     outputs=["text"]
# )

with gr.Blocks() as demo:
    with gr.Row():
        Clump = gr.Number(label='Clump')
        UniCell_Size = gr.Number(label='UniCell_Size')
        Uni_CellShape = gr.Number(label='Uni_CellShape')
    with gr.Row():
        MargAdh = gr.Number(label='MargAdh')
        SEpith = gr.Number(label='SEpith')
        BareN = gr.Number(label='BareN')
    with gr.Row():
        BChromatin = gr.Number(label='BChromatin')
        NoemN = gr.Number(label='NoemN')
        Mitoses = gr.Number(label='Mitoses')
    with gr.Row(): 
        Type = gr.Textbox(label='Type') 
    with gr.Row():  
        button = gr.Button(value="Cancer Type?")
        button.click(predict,
            inputs=[Clump, UniCell_Size,Uni_CellShape, MargAdh, SEpith,BareN, BChromatin , NoemN , Mitoses],
            outputs=[Type])


demo.launch()