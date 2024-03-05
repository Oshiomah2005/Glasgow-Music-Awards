function myFunction() {
    var x = document.getElementById("navList");
    var y = document.getElementById("navBar");
    if (x.className === "topNav") {
      x.className = " responsive";
      y.className = " greyNav"
    } else {
      x.className = "topNav";
      y.className = "navBar"
    }
} 