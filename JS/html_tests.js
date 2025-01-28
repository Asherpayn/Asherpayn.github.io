alert('Welcome');
let username = prompt("What is your name?");



document.getElementsByTagName('h1')[0].onmouseover = function() {
    this.innerText = 'MOUSE IS OVER';
    this.style.color = "Blue";
}

document.getElementsByTagName('h1')[0].onmouseout = function() {
    this.innerText = 'I love the portal games';
    this.style.color = "aqua";
}

ducument.getElementsByTagName('button')[0].onclick = function() {
    this.innerText = username
}