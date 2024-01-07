import gradio as gr

def greet(*args):
    return [i for i in args] #"Hello " * intensity + name + "!"

demo = gr.Interface(
    fn=greet,
    inputs=[
    gr.Dropdown(
        [60, 20, 70, 50, 190, 45, 90, 120, 30, 85, 80, 160, 75, 180, 40], label="Класс здания"
    )  
    , gr.Dropdown(
        ['RL', 'RM', 'C (all)', 'FV', 'RH'], label="Классификация зонирования"
    )   
        , gr.Textbox(label="Размер участка")
        , gr.Textbox(label="Улица")
    , gr.Dropdown(
        ['Reg', 'IR1', 'IR2', 'IR3'], label="Форма объекта недвижимости", 
    )
    , gr.Dropdown(
        ['Lvl', 'Bnk', 'Low', 'HLS'], label="Ровность участка"
    )
    , gr.Dropdown(
        ['AllPub', 'NoSeWa'], label="Утилиты"
    )
    
    , gr.Dropdown(
            ["cat", "dog", "bird"], label="Animal", info="Will add more animals later!"
        )],
    outputs=["text"],
)
demo.language = "en"
demo.launch()
# to see your result you should go to browser and write http://127.0.0.1:7860

# linearModel = None
# with open("LinearRegression.pickle", "rb") as file:
#     linearModel = pickle.load(file)