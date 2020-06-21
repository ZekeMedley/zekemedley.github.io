function getRelativeMousePos(event, point) {
    var mousex = event.clientX;
    var mousey = event.clientY;
    var deltaX = mousex - point.x;
    var deltaY = mousey - point.y;
    return {x: deltaX / window.innerWidth, y: deltaY /  window.innerHeight}
}

function getPosition(el) {
    return {x: el.offsetLeft, y: el.offsetTop}
}

var topPosition = getPosition(document.getElementById("header").childNodes[1])
var bottomPosition = getPosition(document.getElementById("header").childNodes[3])

function setPosition(el, xpos, ypos) {
    el.style.position = "absolute";
    el.style.left = xpos+'px';
    el.style.top = ypos+'px';
}

function moverFn(delta) {
    return Math.log1p(delta);
}

function moveSquares(event) {
    topDelta = getRelativeMousePos(event, topPosition);
    topX = topPosition.x + 10 * moverFn(topDelta.x);
    topY = topPosition.y + 10 * moverFn(topDelta.y);
    setPosition(document.getElementById("header").childNodes[1], topX, topY);
    
    bottomDelta = getRelativeMousePos(event, bottomPosition);
    bottomX = bottomPosition.x + 5 * moverFn(bottomDelta.x);
    bottomY = bottomPosition.y + 5 * moverFn(bottomDelta.y);
    setPosition(document.getElementById("header").childNodes[3], bottomX, bottomY);
}

document.onmousemove = moveSquares