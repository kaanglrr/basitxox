board = ["-","-","-","-","-","-","-","-","-"]
#tahtayı gösterme fonksiyonu
def display_board():
    print("|"+board[0]+"|"+board[1]+"|"+board[2]+"|")
    print("|"+board[3]+"|"+board[4]+"|"+board[5]+"|")
    print("|"+board[6]+"|"+board[7]+"|"+board[8]+"|")
#oyunu başlatıp tahtayı gösterme
def play_game():
    display_board()
    while kazanma():
        oyuncu1()
        display_board()
        if kazanma() == False:
            kazanma()
            break
        oyuncu2()
        display_board()
        if kazanma() == False:
            kazanma()
            break
def oyuncu1():
    a = int(input("hamle yapacağınız yerin numarasını girin")) - 1
    rem = board[a]
    if str(rem) != "-":
        print("buraya hamle yapılmış! tekrar deneyin.")
        oyuncu1()
    else:
        board[a] = "x"
    return
def oyuncu2():
    a = int(input("hamle yapacağınız yerin numarasını girin")) - 1
    rem = board[a]
    if str(rem) != "-":
        print("buraya hamle yapılmış! tekrar deneyin.")
        oyuncu1()
    else:
        board[a] = "o"
    return
def satir():
    satir1 = board[0]==board[1]==board[2] != "-"
    satir2 = board[3]==board[4]==board[5] != "-"
    satir3 = board[6]==board[7]==board[8] != "-"
    if satir1:
        return board[0]
    elif satir2:
        return board[3]
    elif satir3:
        return board[6]
    else:
        return None
def sutun():
    sutun1 = board[0]==board[3]==board[6] != "-"
    sutun2 = board[1]==board[4]==board[7] != "-"
    sutun3 = board[2]==board[5]==board[8] != "-"
    if sutun1:
        return board[0]
    elif sutun2:
        return board[1]
    elif sutun3:
        return board[2]
    else:
        return None
def capraz():
    capraz1 = board[0]==board[4]==board[8] != "-"
    capraz2 = board[2]==board[4]==board[6] != "-"
    if capraz1:
        return board[0]
    elif capraz2:
        return board[2]
    else:
        return None
def kazanma():
    satirkazanani = satir()
    sutunkazanani = sutun()
    caprazkazanan = capraz()
    if sutun() or capraz() or satir() != None:
        if sutunkazanani == "x":
            print("Oyuncu 1 kazandı!")
        elif sutunkazanani == "o":
            print("Oyuncu 2 kazandı!")
        elif satirkazanani == "x":
            print("Oyuncu 1 kazandı!")
        elif satirkazanani == "o":
            print("Oyuncu 2 kazandı!")
        elif caprazkazanan == "x":
            print("Oyuncu 1 kazandı!")
        elif caprazkazanan == "o":
            print("Oyuncu 2 kazandı!")
        return False
    elif board[0] and board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] != "-":
        print("Berabere!")
        return False
    else:
        return True
play_game()
