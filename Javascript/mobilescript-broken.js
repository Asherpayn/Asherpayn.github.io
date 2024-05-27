// Get the user's operating system
var OSName = "Unknown OS";
if (navigator.appVersion.indexOf("Win")!= -1) OSName = "Windows";
if (navigator.appVersion.indexOf("Mac")!= -1) OSName = "MacOS";
if (navigator.appVersion.indexOf("X11")!= -1) OSName = "Linux";

// Redirect to index.html if the user is on a PC or Mac
if (OSName == "Windows" || OSName == "MacOS" || OSName == "Linux") {
  window.location.href = "index.html";
}