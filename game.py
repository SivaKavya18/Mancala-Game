class Mancala_Board:
    def __init__(self, mancala):
        if mancala != None:
            self.mancala = mancala[:]
        else:
            self.mancala = [0 for i in range(10)]
            for i in range(0,4):
                self.mancala[i] = 4
            for i in range(5,9):
                self.mancala[i] = 4

    def player_move(self, i):
        j = i
        repeat_turn = False
        add = self.mancala[j]
        self.mancala[j] = 0
        if i > 4:
            stones = add
            while stones > 0:
                i += 1
                i = i % 10
                if i == 4:
                    continue
                else:
                    self.mancala[i % 10] += 1
                stones -= 1
            if i > 4 and self.mancala[i] == 1 and i != 9 and self.mancala[3-(i-5)] != 0:
                self.mancala[9] += 1 + self.mancala[3-(i-5)]
                self.mancala[i] = 0
                self.mancala[3-(i-5)] = 0
            if i == 9:
                repeat_turn = True
        else:
            stones = add
            while (stones > 0):
                i += 1
                i = i % 10
                if i == 9:
                    continue
                else:
                    self.mancala[i%10] += 1
                stones -= 1
            if i < 4 and self.mancala[i] == 1 and i !=4 and self.mancala[-i + 8]!=0:
                self.mancala[4] += 1 + self.mancala[-i + 8]
                self.mancala[i] = 0
                self.mancala[-i + 8] = 0
            if i == 4:
                repeat_turn = True
        return repeat_turn

    def isEnd(self):
        if sum(self.mancala[0:4])==0 :
            self.mancala[9]+=sum(self.mancala[5:9])
            for i in range(10):
                if  (i != 9 and i != 4):
                    self.mancala[i] = 0

            return True
        elif sum(self.mancala[5:9])==0:
            self.mancala[4] += sum(self.mancala[0:4])
            for i in range(10):
                if  (i != 9 and i != 4):
                    self.mancala[i] = 0
            return True

        return False

    def print_mancala(self):
        for i in range(8,4,-1):
            print('  ', self.mancala[i], '   ', end = '')
        print('  ')
        print(self.mancala[9],'                           ',self.mancala[4])

        for i in range(0,4,1):
            print('  ', self.mancala[i], '   ', end='')
        print('  ')
    def husVal(self):
        if self.isEnd():
            if self.mancala[9]>self.mancala[4]:
                return 100
            elif self.mancala[9]==self.mancala[4]:
                return 0
            else :
                 return -100
        else:
            return self.mancala[9]- self.mancala[4]

def alphabeta(mancala, depth, alpha, beta , MinorMax):
    if depth == 0 or mancala.isEnd():
      return mancala.husVal(),-1
    if MinorMax:
        v = -1000000
        player_move = -1
        for i in range(5,9,1):
            if mancala.mancala[i]==0: continue
            a = Mancala_Board(mancala.mancala[:])
            minormax = a.player_move(i)
            newv,_ =  alphabeta(a, depth-1, alpha, beta, minormax)
            if v < newv:
                player_move = i
                v = newv
            alpha = max(alpha, v)
            if alpha >= beta :
                break
        return v, player_move
    else:
        v = 1000000
        player_move = -1
        for i in range(0, 4, 1):
            if mancala.mancala[i] == 0: continue
            a = Mancala_Board(mancala.mancala[:])
            minormax = a.player_move(i)
            newv,_ = alphabeta(a, depth - 1, alpha, beta, not  minormax)
            if v > newv:
                player_move = i
                v = newv
            beta = min(beta, v)
            if alpha >= beta:
                break
        return v, player_move

def player_aibot():
    j = Mancala_Board(None)
    j.print_mancala()
    while True:
        if j.isEnd():
            break
        while True:
            if j.isEnd():
                break
            h = int(input("YOUR TURN >>> "))
            if h > 3 or j.mancala[h] == 0:
                print("You can't Play at this position. Choose another position")
                continue
            t = j.player_move(h)
            j.print_mancala()
            if not t:
                break
        while True:
            if j.isEnd():
                break
            print("AI-BOT TURN >>> ", end = "")
            _,k = alphabeta(j, 10, -100000, 100000, True)
            print(k)
            t = j.player_move(k)
            j.print_mancala()
            if not t:
                break
    if j.mancala[4] < j.mancala[9]:
        print("AI-BOT WINS")
    else:
        print("YOU WIN")
    print('GAME ENDED')
    j.print_mancala()

def Feedback():
    print("GIVE YOUR FEEDBACK:")
    a=input()
    print("Thankyou for the feedback")

print("\n:::: MANCALA BOARD GAME ::::")
print("!!! Welcome to Mancala Gameplay !!!")
while True:
    print("\nChoose your Gameplay Type")
    print("(1) Player vs AI-Bot")
    print("(2) Feedback")
    type = int(input(">>> "))
    if type == 1:
        player_aibot()
        break
    elif type == 2:
        Feedback()
        break
    else:
        print("Wrong Gameplay Type. Enter Again")
        continue
