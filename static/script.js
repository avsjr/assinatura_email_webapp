document.addEventListener("DOMContentLoaded", function () {
    let unitSelect = document.getElementById("unitSelect");
    let signatureImage = document.getElementById("signatureImage");

    unitSelect.addEventListener("change", function () {
        const selectedUnit = unitSelect.value;

        if (selectedUnit === "Platina_csc") {
            signatureImage.src = "static/img/02-platina.png";
            email_input.value = "@platinacsc.com.br";
        } else if (selectedUnit === "Platina_log") {
            signatureImage.src = "static/img/02-platina.png";
            email_input.value = "@platinacsc.com.br";
        } else if (selectedUnit === "Masterline") {
            signatureImage.src = "static/img/01-masterline.png";
            email_input.value = "@masterline.ind.br";
        }
    });

});

$(document).ready(function() {
    $("#phoneInput").inputmask({
      mask: ["(99) 9999 9999", "(99) 9 9999 9999"],
      keepStatic: true
    });
  
    $("#phone02Input").inputmask({
      mask: ["(99) 9999 9999", "(99) 9 9999 9999"],
      keepStatic: true
    });
  });
