$(document).ready(function(){

$("#errorReNombre").hide();
$("#errorReCorreo").hide();
$("#errorReContraseña").hide();


$("#register-form").submit(function(){
    if($("#reNombreUsuario").val().trim().length==0){
        $("#errorReNombre").html("ingrese nombre de usuario valido");
        $("#errorReNombre").show();
        event.preventDefault();
    }
    
    if($("#reCorreo").val().trim().length==0){
        $("#errorReCorreo").html("ingrese correo valido");
        $("#errorReCorreo").show();
        event.preventDefault();
    }
    
    if($("#reContraseña").val().trim().length==0){
        $("#errorReContraseña").html("ingrese contraseña valida");
        $("#errorReContraseña").show();
        event.preventDefault();
    }

});

$("#reNombreUsuario").focus(function(){
    $("#errorReNombre").hide();
});

$("#reCorreo").focus(function(){
    $("#errorReCorreo").hide();
});

$("#reContraseña").focus(function(){
    $("#errorReContraseña").hide();
});


});

