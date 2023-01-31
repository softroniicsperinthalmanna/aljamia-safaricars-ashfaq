function varify()
{
    var p=document.getElementById("password").value;
    var c=document.getElementById("cpassword").value;
    if(p!=c)
    {
        alert("invalid")
    }
    if(p.length < 8)
    {
        alert("password must be at least 8 characters")
    }
    if(p==c)
    {
        alert("passord is valid")
    }

}