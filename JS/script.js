if (
  /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent) &&
  !window.location.pathname.endsWith("mobilesupport.html") &&
  !window.location.pathname.endsWith("mobileversion.html")
) {
  window.location = "mobilesupport.html";
}
