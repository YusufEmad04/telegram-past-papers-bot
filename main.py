#import json
import requests
import threading

url = "https://api.telegram.org/bot1732866192:AAEp_3tXo994Yy8eUQm2xjUpgU-Pg4XvIi0/"


def thread(update):
    #x = threading.Thread(target=updateHandler, args=(update,))
    #x.start()
    updateHandler(update)


def updateHandler(update: dict):
    print("(______" + str(threading.active_count()) + "______)")
    #requests.post(url=url+"sendMessage" , json={"chat_id" : "1719079956" , "text" : "{}".format("(______" + str(threading.active_count()) + "______)")})
    is_text_message = None
    is_callback_query = None
    callback_query_data = None
    text_message = None

    try:
        if "text" in update["message"]:
            is_text_message = True
    except:
        pass

    try:
        if "data" in update["callback_query"]:
            is_callback_query = True
    except:
        pass

    if is_text_message:
        text_message = update["message"]["text"]

    if is_callback_query:
        callback_query_data = update["callback_query"]["data"]

    print(is_text_message)
    print(text_message)
    print(is_callback_query)
    print(callback_query_data)

    if is_text_message:
        chat_id = update["message"]["chat"]["id"]
        if text_message == "hello":
            d = {"chat_id": chat_id, "text": "hello! \n type /choose_subject command to choose a subject"}
            y = requests.post(url=url + "sendMessage", json=d)
            print(y.content)
        elif text_message == "/choose_subject":
            data = {"chat_id": chat_id, "text": "please choose a subject", "reply_markup": {"inline_keyboard": [
                [{"text": "Biology", "callback_data": "Biology"}, {"text": "Chemistry", "callback_data": "Chemistry"}],
                [{"text": "Math", "callback_data": "Math"}, {"text": "Physics", "callback_data": "Physics"}]]}}
            y = requests.post(url=url + "sendMessage", json=data)
            print(y.content)
        else:
            data = {"chat_id": chat_id, "text": "type /choose_subject command to choose a subject"}
            y = requests.post(url=url + "sendMessage", json=data)
            print(y.content)

    if is_callback_query:
        chat_id = update["callback_query"]["message"]["chat"]["id"]
        if callback_query_data == "Biology" or callback_query_data == "Chemistry" or callback_query_data == "Math" or callback_query_data == "Physics":
            data = callback_query_data
            if data == "Biology" or data == "Physics" or data == "Chemistry":
                json = {
                    "chat_id": chat_id,
                    "text": "{} : \n choose paper".format(data),
                    "reply_markup": {
                        "inline_keyboard": [[{"text": "paper 2", "callback_data": "{}_paper2".format(data)}],
                                            [{"text": "paper 4", "callback_data": "{}_paper4".format(data)}],
                                            [{"text": "paper 6", "callback_data": "{}_paper6".format(data)}]]
                    }
                }
                y = requests.post(url=url + "sendMessage", json=json)
                print(y.content)
        elif len(callback_query_data.split("_")) == 2:
            data = callback_query_data
            json = {"chat_id": chat_id, "text": "{} : \n choose year".format(
                data.split("_")[0] + " " + data.split("_")[1][:5] + " " + data.split("_")[1][-1]),
                    "reply_markup": {"inline_keyboard": [
                        [{"text": "2010", "callback_data": "{}_2010".format(data)}],
                        [{"text": "2011", "callback_data": "{}_2011".format(data)}],
                        [{"text": "2012", "callback_data": "{}_2012".format(data)}],
                        [{"text": "2013", "callback_data": "{}_2013".format(data)}],
                        [{"text": "2014", "callback_data": "{}_2014".format(data)}],
                        [{"text": "2015", "callback_data": "{}_2015".format(data)}],
                        [{"text": "2016", "callback_data": "{}_2016".format(data)}],
                        [{"text": "2017", "callback_data": "{}_2017".format(data)}],
                        [{"text": "2018", "callback_data": "{}_2018".format(data)}],
                        [{"text": "2019", "callback_data": "{}_2019".format(data)}],
                        [{"text": "2020", "callback_data": "{}_2020".format(data)}],

                    ]}}
            y = requests.post(url=url + "sendMessage", json=json)
            print(y.content)

        elif len(callback_query_data.split("_")) == 3:
            data = callback_query_data
            data_splitted = data.split("_")
            json={
                "chat_id":chat_id, "text": "{} : \n choose session".format(data_splitted[0]+" "+data_splitted[1][:5]+" "+data_splitted[1][-1]+" "+data_splitted[2]),
                "reply_markup" : { "inline_keyboard" : [
                    [{"text": "February/March" , "callback_data":"{}_February/March".format(data)}],
                    [{"text": "May/June" , "callback_data":"{}_May/June".format(data)}],
                    [{"text": "October/November" , "callback_data":"{}_October/November".format(data)}]
                ]
                }
            }
            y = requests.post(url=url+"sendMessage",json=json)
            print(y.content)

        elif len(callback_query_data.split("_")) == 4:
            data = callback_query_data
            data_splitted = data.split("_")
            json={
                "chat_id": chat_id, "text":"{} : \n choose variant".format(data_splitted[0]+" "+data_splitted[1][:5]+" "+data_splitted[1][-1]+" "+data_splitted[2]+" "+data_splitted[3]),
                "reply_markup" : { "inline_keyboard" : [
                    [{"text" : "variant 1" , "callback_data" : "{}_variant1".format(data)}],
                    [{"text" : "variant 2" , "callback_data" : "{}_variant2".format(data)}],
                    [{"text" : "variant 3" , "callback_data" : "{}_variant3".format(data)}]
                ]

                }
            }
            y = requests.post(url=url+"sendMessage", json=json)
            print(y.content)

        elif len(callback_query_data.split("_")) == 5:
            data = callback_query_data
            data_splitted = data.split("_")
            json = {
                "chat_id": chat_id, "text":"{} : \n question paper or marking scheme?".format(data_splitted[0]+" "+data_splitted[1][:5]+" "+data_splitted[1][-1]+" "+data_splitted[2]+" "+data_splitted[3]+" "+data_splitted[4][:7]+" "+data_splitted[4][-1]),
                "reply_markup" : { "inline_keyboard" : [
                    [{"text" : "question paper" , "callback_data" : "{}_qp".format(data)}],
                    [{"text" : "marking scheme" , "callback_data":"{}_ms".format(data)}]
                ]
                }
            }
            y = requests.post(url=url+"sendMessage" , json=json)
            print(y.content)

        elif len(callback_query_data.split("_")) == 6:
            data = callback_query_data
            data_splitted = data.split("_")
            file = ""
            year=data_splitted[2][2:]
            session = {
                "October/November" : "w",
                "May/June" : "s",
                "February/March":"m"
            }
            subj={
                "Biology" : "0610_",
                "Chemistry" : "0620"
            }

            file += subj[data_splitted[0]]+"_"+session[data_splitted[3]]+year+"_"+data_splitted[5]+"_"+data_splitted[1][-1]+data_splitted[4][-1]
            print("{}/{}.pdf".format(data_splitted[0] , file))
            try:
                with open("{}/{}.pdf".format(data_splitted[0],file),"rb") as f:
                    files = {"document": ("{}.pdf".format(file), f.read(),"application/pdf")}

                    y = requests.post(url=url + "sendMessage",
                                      json={"chat_id": chat_id, "text": "please wait a moment 😊"})
                    print(y.content)
                    y = requests.post(files=files,url=url+"sendDocument",data={"chat_id":chat_id})
                    print(y.content)
            except FileNotFoundError:
                y = requests.post(url=url+"sendMessage" , json={"chat_id" : chat_id , "text" : "sorry couldn't send file"})
                print(y.content)
