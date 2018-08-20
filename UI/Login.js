

  function validateForm() {
    var x = document.forms["LoginForm"]["user"].value;
    var x2 = document.forms["LoginForm"]["email"].value;
    if (x == "") {
        alert("Name must be filled out");
        return false;
    }
    if (x2 == "") {
      alert("Email must be filled out");
      return false;
  }
  
}

function validateSignupForm() {
  var x = document.forms["SignupForm"]["user"].value;
  var x2 = document.forms["SignupForm"]["email"].value;
  var x3 = document.forms["SignupForm"]["pass1"].value;
  var x4 = document.forms["SignupForm"]["pass2"].value;
  if (x == "") {
      alert("Name must be filled out");
      return false;
  }
  if (x2 == "") {
    alert("Email must be filled out");
    return false;
}
if (x3 == "") {
  alert("Set Pasword");
  return false;
}
if (!x3 == x4) {
  alert("Password Mismatch");
  return false;
}


}