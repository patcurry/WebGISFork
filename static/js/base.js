// This file has base JS stuff, such as the document.ready command
// and a toggle display command.

// define DOM ready function
const domReady = function(callback) {
  document.readyState === "interactive" ||
  document.readyState === "complete" ? callback() : document.addEventListener("DOMContentLoaded", callback);
};


// define toggle element display function
// this may not be needed anymore
/*
function toggleDisplay(obj) {
  let element = document.getElementById(obj);
  if ( element.style.display != "none" ) {
    element.style.display = "none";
  } else {
    element.style.display = "";
  }
};
*/

Element.prototype.remove = function() {
    this.parentElement.removeChild(this);
}
NodeList.prototype.remove = HTMLCollection.prototype.remove = function() {
    for(var i = this.length - 1; i >= 0; i--) {
        if(this[i] && this[i].parentElement) {
            this[i].parentElement.removeChild(this[i]);
        }
    }
}

