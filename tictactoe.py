import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
     # satır-sutun kontrolu 
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board [i][0] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]

# kosegen kontrolu
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0] 
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
# berabere mi devam mi
    if any(' ' in row for row in board):
        return None
    return 'berabere'

def minimax(board, depth, is_maximizing):
    result = check_winner(board)
    if result == 'X': return 10 - depth # bot kazaninca
    if result == 'O': return depth - 10 # oyuncu kazaninca
    if result == 'berabere': return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# ana dongu
def play():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("tic-tac-toe: bilgisayara karsi!!")
    print("koordinatlari 0, 1, 2 seklinde girin.")

    while True:
        print_board(board)
        # hamle (oyuncu) - O
        row, col = map(int, input("satir ve sutun sec (ornegin: 0 1): ").split())
        if board[row][col] != ' ':
            print("gecersiz hamle, tekrar dene!")
            continue
        board[row][col] = 'O'

        if check_winner(board): break
        
        # hamle (bilgisayar) - X
        print("\nbilgisayar hamlesini yapiyor...")
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = 'X'

        if check_winner(board): break

    print_board(board)
    sonuc = check_winner(board)
    if sonuc == 'berabere':
        print("oyun berabere bitti!")
    else:
        print(f"kazanan: {sonuc}")

if __name__ == "__main__":
    play()