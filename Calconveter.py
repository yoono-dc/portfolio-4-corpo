# importing all widgets and modules from the tkinter library  
from tkinter import *  
  
# defining the reset function  
def reset():  
    # using the delete() method to delete entries in entry field  
    input_field.delete(0, END)  
    output_field.delete(0, END)  
    # setting the value of the option menu to the  
    # first index of the list using the set() method  
    input_value.set(SELECTIONS[0])  
    output_value.set(SELECTIONS[0])  
  
    # setting the focus to input field using the focus_set() method  
    input_field.focus_set()  
  
# defining the convert function  
def convert():  
    # getting the string from entry field and converting it into float  
    inputVal = float(input_field.get())  
    # getting the values from selection menus  
    input_unit = input_value.get()  
    output_unit = output_value.get()  
  
    # list of the required combination of the conversion factors  
    conversion_factors = [input_unit in length_units and output_unit in length_units,  
    input_unit in weight_units and output_unit in weight_units,  
    input_unit in temperature_units and output_unit in temperature_units,  
    input_unit in area_units and output_unit in area_units,  
    input_unit in volume_units and output_unit in volume_units]  
  
    if any(conversion_factors): # If both the units are of same type, perform the conversion  
        if input_unit == "摂氏" and output_unit == "華氏":  
            output_field.delete(0, END)  
            output_field.insert(0, (inputVal * 1.8) + 32)  
        elif input_unit == "華氏" and output_unit == "摂氏":  
            output_field.delete(0, END)  
            output_field.insert(0, (inputVal - 32) * (5/9))  
        else:  
            output_field.delete(0, END)  
            output_field.insert(0, round(inputVal * unitDict[input_unit] / unitDict[output_unit], 5))  
  
    else:  
        # displaying error if units are of different types  
        output_field.delete(0, END)  
        output_field.insert(0, "ユニットが違います")  
  
if __name__ == "__main__":  
    # dictionary of conversion factors  
    unitDict = {  
        "ミリ" : 0.001,  
        "センチ" : 0.01,  
        "メートル" : 1.0,  
        "キロメートル" : 1000.0,  
        "フィート" : 0.3048,  
        "マイル" : 1609.344,  
        "ヤード" : 0.9144,  
        "インチ" : 0.0254,  
        "平方メートル" : 1.0,  
        "平方キロメートル" : 1000000.0,  
        "平方センチメートル" : 0.0001,  
        "平方ミリメートル" : 0.000001,  
        "アール" : 100.0,  
        "ヘクタール" : 10000.0,  
        "エーカー" : 4046.856,  
        "平方マイル" : 2590000.0,  
        "平方フィート" : 0.0929,  
        "立方メートル" : 1000.0,  
        "立方センチメートル" : 0.001,  
        "リットル" :  1.0,  
        "ミリリットル" : 0.001,
        "小さじ" : 0.005, 
        "大さじ" : 0.015,
        "液量オンス" : 0.29574,
        "カップ(日本)" : 0.200,
        "カップ(米国)" : 0.240,
        "ガロン" : 3.785,  
        "グラム" : 1.0,
        "グレーン" : 0.15432,
        "ストーン" : 6350.2,  
        "キログラム" : 1000.0,  
        "ミリグラム" : 0.001,  
        "トン" : 1000000.0,  
        "ポンド" : 453.592,  
        "オンス" : 28.3495  
    }  
  
    # charts for units conversion  
    length_units = [  
        "ミリメートル", "センチメートル", "メートル", "キロメートル", "フィート", "マイル", "ヤード", "インチ"  
        ]  
    temperature_units = [  
        "摂氏", "華氏"  
    ]  
    area_units = [  
        "平方メートル", "平方キロメートル", "平方センチメートル",  "平方ミリメートル",   
        "アール", "ヘクタール", "エーカー", "平方マイル", "平方フィート"  
        ]  
    volume_units = [  
        "立方メートル", "立方センチメートル", "リットル", "ミリリットル", 
        "小さじ", "大さじ", "液量オンス", "カップ(日本)", "カップ(米国)", "ガロン"     
    ]  
    weight_units = [  
        "グラム", "キログラム", "ミリグラム", "グレーン",  "ストーン", "トン", "ポンド", "オンス"  
    ]  
  
    # creating the list of options for selection menu  
    SELECTIONS = [  
        "ユニット",  
        "ミリメートル",  
        "センチメートル",  
        "メートル",  
        "キロメートル",  
        "フィート",  
        "マイル",  
        "ヤード",  
        "インチ",  
        "摂氏",  
        "華氏"  
        "平方メートル",  
        "平方キロメートル",  
        "平方センチメートル",  
        "平方ミリメートル",  
        "アール", 
        "ヘクタール", 
        "エーカー", 
        "平方マイル", 
        "平方フィート",  
        "立方メートル",  
        "立方センチメートル",  
        "リットル",  
        "ミリリットル", 
        "小さじ", 
        "大さじ", 
        "液量オンス", 
        "カップ(日本)", 
        "カップ(米国)", 
        "ガロン",
        "グラム",
        "キログラム",
        "ミリグラム",
        "トン",
        "ストーン",
        "ポンド",
        "オンス",
        "グレーン"
    ]  
  
    guiWindow = Tk()   
    guiWindow.title("Calconverter")  
    guiWindow.geometry("500x500+500+250")   
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg = "#3A6EA5")  
  
    # フレーム 
    header_frame = Frame(guiWindow, bg = "#3A6EA5")  
    body_frame = Frame(guiWindow, bg = "#3A6EA5")  
  
    # setting the positions of the frames  
    header_frame.pack(expand = True, fill = "both")  
    body_frame.pack(expand = True, fill = "both")  
  
    # adding the label to the header frame   
    header_label = Label(  
        header_frame,  
        text = "コンバージョン",  
        font = ("arial black", 16),  
        bg = "#3A6EA5",  
        fg = "#e8f6f3"  
    )  
  
    # setting the position of the label  
    header_label.pack(expand = True, fill = "both")  
  
    # creating the objects of the StringVar() class  
    input_value = StringVar()  
    output_value = StringVar()  
    # using the set() method to set the primary  
    # value of the objects to index value 0  
    # of the SELECTIONS list  
    input_value.set(SELECTIONS[0])  
    output_value.set(SELECTIONS[0])  
  
    # creating the labels for the body of the main window  
    input_label = Label(  
        body_frame,  
        text = "インプット",  
        bg = "#3A6EA5",  
        fg = "#d0ece7"  
    )  
    output_label = Label(  
        body_frame,  
        text = "アウトプット",  
        bg = "#3A6EA5",  
        fg = "#d0ece7"  
    )  
  
    # using the grid() method to set the position of the above labels   
    input_label.grid(row = 1, column = 1, padx = 50, pady = 20, sticky = W)  
    output_label.grid(row = 2, column = 1, padx = 50, pady = 20, sticky = W)  
  
    # creating the entry fields for the body of the main window  
    # input field to enter data  
    input_field = Entry(  
        body_frame,  
        bg = "#e8f8f5"  
    )  
    # output field to display result  
    output_field = Entry(  
        body_frame,  
        bg = "#e8f8f5"  
    )  
  
    # using the grid() method to set the position of the above entry fields   
    input_field.grid(row = 1, column = 2)  
    output_field.grid(row = 2, column = 2)  
  
    # adding the option menus to the main window  
    input_menu = OptionMenu(  
        body_frame,  
        input_value,  
        *SELECTIONS  
    )  
    output_menu = OptionMenu(  
        body_frame,  
        output_value,  
        *SELECTIONS  
    )  
  
    # using the grid() method to set the position of the above option menus   
    input_menu.grid(row = 1, column = 3, padx = 20)  
    output_menu.grid(row = 2, column = 3, padx = 20)  
  
    # creating the buttons for the main window  
    # CONVERT button  
    convert_button = Button(  
        body_frame,  
        text = "CONVERT",  
        bg = "#0b5345",  
        fg = "#ffffff",  
        command = convert  
    )  
    # RESET button  
    reset_button = Button(  
        body_frame,  
        text = "RESET",  
        bg = "#f7dc6f",  
        fg = "#000000",  
        command = reset  
    )  
  
    # using the grid() method to set the position of the above buttons  
    convert_button.grid(row = 3, column = 2)  
    reset_button.grid(row = 3, column = 3)  
  
    # running the application  
    guiWindow.mainloop()  