#Greeting with player
from art import tprint
from tabulate import TableFormat, tabulate

tprint("StaNDRu")
print('Hello, my friend! Developer glad to see you.This is StaNDRu, game about Russia in 16th century.')
#Discribing Rules of game
print("Ты будешь принимать различные решения, которые будут по разному влиять на гос-во")
print("Тебе даны ресурсы в виде таблицы:")
restable = [["Пища",8000],["Железо", 8000],["Дерево", 8000],["Люди",8000],["Целковые",8000]]
rets = tabulate(restable)
print(tabulate(restable))
print("Каждое решение будет иметь своё последствие.")
answer = input("Давай начнём?")
#Start of game
if answer == "Давай":
    print(rets)
    deseat= input("Царь, в стране голодают люди. Выделить пищу из запасов Царского двора?\n Да - потратьте 500 пищи/Нет - умрёт 500 человек\n")
    #Good way 
    if deseat == "Да":
        restable[0] = ["Пища",7500]
        print("Вы приняли верное решение. Народ вам благодарен. Пища -500, Целковые + 500")
        restable[4] = [ "Целковые", 8500]
        print(rets)
        Wardes = input("Царь, прибыли послы из Англии. Они желают заключить с нами договор. Сейчас мы можем предоставить им\n привилегии, а в будующем это сыграет хорошую службу. Да ( -50 пищи, - 50 железа)/Нет(Ничего не изменится)")
        if Wardes == "Да":
            restable[0] = ["Пища", 7500-50]
            restable[1] = ["Железо", 8000-50]
            print("Спасибо, царь мы вам благодарны!")
            print(rets)
    #Bad way
    if deseat == "Нет":
        restable[3] = ["Люди", 7500]
        print("К сожалению, множесство людей погибло! -500 человек.\n В стране бунты")
        restable[4] = ["Целковые",7900]
        print("На их подавление ззатраченны деньги -100р")
        print(rets)
       
else: 
    print("Хорошо, ладно.")
        
