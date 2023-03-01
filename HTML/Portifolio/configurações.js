var click = document.querySelector("#mais");
var projetos = document.querySelector(".mais");
click.addEventListener('click', function(){
  projetos.style.display = "inline";
  click.style.display = "none";
})
var imagArmazenamento = document.querySelector(".armazenamento");
var imagWhats = document.querySelector(".whats");
var imagCardapio = document.querySelector(".cardapio");
var imagJogo = document.querySelector(".jogo");
var imagMicrophone = document.querySelector(".Microphone");
var explicacaoArmazenamento = document.querySelector("#textoArmazenamento");
var roboWhats = document.querySelector("#textoWhats");
var cardapioDigital = document.querySelector("#textoCardapio");
var descriçãoDoJogo = document.querySelector("#textoJogo");
var assistenteVirtual = document.querySelector("#textoAssistente");
var fechar = document.querySelector("#fechar");

imagArmazenamento.addEventListener('click', function(){
  explicacaoArmazenamento.style.display = "inline";
  fechar.style.display = "inline";
  imagArmazenamento.style.display = "none";
  imagWhats.style.display = "none";
  imagCardapio.style.display = "none";
  imagJogo.style.display = "none";
  imagMicrophone.style.display = "none";
  click.style.opacity = "0";
})

imagWhats.addEventListener('click', function(){
  roboWhats.style.display = "inline";
  fechar.style.display = "inline";
  imagArmazenamento.style.display = "none";
  imagWhats.style.display = "none";
  imagCardapio.style.display = "none";
  imagJogo.style.display = "none";
  imagMicrophone.style.display = "none";
  click.style.opacity = "0";
})

imagCardapio.addEventListener('click', function(){
  cardapioDigital.style.display = "inline";
  fechar.style.display = "inline";
  imagArmazenamento.style.display = "none";
  imagWhats.style.display = "none";
  imagCardapio.style.display = "none";
  imagJogo.style.display = "none";
  imagMicrophone.style.display = "none";
  click.style.opacity = "0";
})

imagJogo.addEventListener('click', function(){
  descriçãoDoJogo.style.display = "inline";
  fechar.style.display = "inline";
  imagArmazenamento.style.display = "none";
  imagWhats.style.display = "none";
  imagCardapio.style.display = "none";
  imagJogo.style.display = "none";
  imagMicrophone.style.display = "none";
  click.style.opacity = "0";
})

imagMicrophone.addEventListener('click', function(){
  assistenteVirtual.style.display = "inline";
  fechar.style.display = "inline";
  imagArmazenamento.style.display = "none";
  imagWhats.style.display = "none";
  imagCardapio.style.display = "none";
  imagJogo.style.display = "none";
  imagMicrophone.style.display = "none";
  click.style.opacity = "0";
})

fechar.addEventListener('click', function(){
  explicacaoArmazenamento.style.display = "none";
  fechar.style.display = "none";
  roboWhats.style.display = "none";
  cardapioDigital.style.display = "none";
  descriçãoDoJogo.style.display = "none";
  assistenteVirtual.style.display = "none";
  imagArmazenamento.style.display = "inline";
  imagWhats.style.display = "inline";
  imagWhats.style.opacity = "1";
  imagCardapio.style.display = "inline";
  imagJogo.style.display = "inline";
  imagMicrophone.style.display = "inline";
  click.style.opacity = "1";
})
