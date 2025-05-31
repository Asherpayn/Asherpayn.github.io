alert("Welcome");
let food = prompt("What is your favourite Food?");

document.getElementsByTagName("h1")[0].onmouseover = function () {
  this.innerText = "MOUSE IS OVER";
  this.style.color = "Blue";
};

document.getElementsByTagName("h1")[0].onmouseout = function () {
  this.innerText = "I love the portal games";
  this.style.color = "aqua";
};

document.getElementsByTagName("button")[0].onclick = function () {
  this.innerText = food;
};
