let board = null;
let game = new Chess();

function onDragStart(source, piece, position, orientation) {
    if (Gamepad.game_over() || piece.search(/^b/) !== -1) {
        return false;
    }
}

var config = {
    draggable: true,
    position: "start",
    onDragStart: onDragStart,
    onDrop: onDrop,
    onSnapEnd: onSnapEnd,
    pieceTheme: "https://chessboardjs.com/img/chesspieces/wikipedia/{piece}.png"
};

board = Chessboard("board", config);
