# Инициализация игрового поля 3x3
def initialize_board():
    return [["-" for _ in range(3)] for _ in range(3)]

# Функция для отображения игрового поля
def print_board(board):
    # Вывод заголовков столбцов
    print("  0 1 2")
    # Вывод строк с номерами
    for i, row in enumerate(board):
        print(f"{i} {' '.join(row)}")

# Функция для проверки, завершена ли игра
def check_winner(board):
    # Проверка строк и столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "-":
            return board[0][i]
    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return board[0][2]
    # Проверка на ничью
    if all(cell != "-" for row in board for cell in row):
        return "Ничья"
    return None

# Функция для проверки корректности ввода и выполнения хода
def make_move(board, player):
    while True:
        try:
            row, col = map(int, input(f"Игрок {player}, введите номер строки и столбца (0, 1, 2): ").split())
            if 0 <= row < 3 and 0 <= col < 3:  # Проверка диапазона
                if board[row][col] == "-":
                    board[row][col] = player
                    break
                else:
                    print("Эта клетка уже занята, попробуйте другую.")
            else:
                print("Некорректный ввод. Числа должны быть от 0 до 2.")
        except (ValueError, IndexError):
            print("Некорректный ввод. Пожалуйста, введите два числа от 0 до 2.")

# Основная функция игры
def play_game():
    board = initialize_board()
    current_player = "X"
    while True:
        print_board(board)
        make_move(board, current_player)
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "Ничья":
                print("Игра окончена: Ничья!")
            else:
                print(f"Игра окончена: Игрок {winner} выиграл!")
            break
        current_player = "0" if current_player == "X" else "X"  # Меняем игрока

# Запуск игры
play_game()