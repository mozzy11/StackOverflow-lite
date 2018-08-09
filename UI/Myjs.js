
 function validatePostForm() {
    var x = document.forms["PostForm"]["querry"].value;

    if (x == "") {
        alert("Empty Queston .Please Post a question");
        return false;
    }
    
  }


  function ValidAns() {
    var x = document.forms["ans"]["answer"].value;

    if (x == "") {
        alert("Empty Answer .Please Post an Answer");
        return false;
    }
    
  }

  
  function ValdAsses(){
    var x = document.forms["asses"]["comment"].value;

    if (x == "") {
        alert("Empty Comment .Please Post a comment");
        return false;
    }
    
  }