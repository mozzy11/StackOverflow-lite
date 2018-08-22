
 function validatePostForm() {
    var x = document.forms["PostForm"]["querry"].value;

    if (x == "") {
        alert("Empty Queston .Please Post a question");
        return false;
    } else {
        window.location.replace ("answerPage.html");
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
function  delet(){
    var checkbox = document.getElementById("chbx");
   
       if(checkbox.checked){
        var retVal = confirm("Do you want to Delete this Question ?");
               if( retVal == true ){
                alert("Question Deleted");
               
                  return true;
               }
               else{
                  return false;

}
}
}
function showcomments() {
    var x = document.getElementById("comments");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function addcomment() {
    var x = document.getElementById("addcomment");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}