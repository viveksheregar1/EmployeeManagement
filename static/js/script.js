function changereadonly(){
    document.getElementById('firstname').readOnly=false;
    document.getElementById('lastname').readOnly=false;
    document.getElementById('email').readOnly=false;
    document.getElementById('contact').readOnly=false;
    document.getElementById('address').readOnly=false;
    document.getElementById('dept').readOnly=false;
    document.getElementById('salary').readOnly=false;
    document.getElementById('update').style.visibility='visible';
    document.getElementById('edit').style.visibility='hidden';
    document.getElementById('delete').style.visibility='hidden';
}