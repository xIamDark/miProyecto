$(document).ready(function () {
    $("#errorCorreo").hide();
    $("#errorContraseña").hide();

    $("#login-form").submit(function () {
        if ($("#correo").val().trim().length == 0) {
            $("#errorCorreo").html("ingrese correo valido");
            $("#errorCorreo").show();
            event.preventDefault();
        }

        if ($("#contraseña").val().trim().length == 0) {
            $("#errorContraseña").html("ingrese contraseña valida");
            $("#errorContraseña").show();
            event.preventDefault();
        }

    });
    $("#correo").focus(function () {
        $("#errorCorreo").hide();
    });

    $("#contraseña").focus(function () {
        $("#errorContraseña").hide();
    });


});