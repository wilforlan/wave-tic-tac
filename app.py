from flask import Flask,request,abort,jsonify,Response
from game.play import TTTBoard
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.errorhandler(Exception)
def handle_error(e):
    code = 400
    if isinstance(e, HTTPException):
        code = e.code
    return str(e), code

@app.route('/', methods=['GET'])
def game():
    board_query = request.args.get('board')
    board = TTTBoard(board_query)
    return board.makeMove(), 200


if __name__ == '__main__':
    app.run(debug=True)