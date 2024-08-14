def predict_move(model, board):
    board_flat = board.flatten().reshape(1, -1)
    predictions = model.predict(board_flat)
    move_index = np.argmax(predictions[0])
    row, col = divmod(move_index, 3)
    return (row, col)

def play_with_ai(model):
    game = TicTacToe()
    while True:
        game.print_board()
        user_move = tuple(map(int, input("Enter your move (row col): ").split()))
        if not game.make_move(*user_move):
            print("Invalid move. Try again.")
            continue
        if game.is_winner(1):
            print("You win!")
            break
        if game.is_draw():
            print("It's a draw!")
            break
        ai_move = predict_move(model, game.board)
        print(f"AI moves: {ai_move}")
        game.make_move(*ai_move)
        if game.is_winner(-1):
            print("AI wins!")
            break
        if game.is_draw():
            print("It's a draw!")
            break
        game.switch_player()

# Play with the AI
play_with_ai(model)
