
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



function openCity(evt, Name) {

    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(Name).style.display = "block";
    evt.currentTarget.className += " active";
}



