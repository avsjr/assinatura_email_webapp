document.addEventListener("DOMContentLoaded", function () {
    let unitSelect = document.getElementById("unitSelect");
    let signatureImage = document.getElementById("signatureImage");

    unitSelect.addEventListener("change", function () {
        const selectedUnit = unitSelect.value;

        if (selectedUnit === "Platina") { // Atualize a imagem para a unidade Platina
            signatureImage.src = "static/img/02-platina.png";

        } else if (selectedUnit === "Masterline") { // Atualize a imagem para a unidade Masterline           
            signatureImage.src = "static/img/01-masterline.png";      
        }
    });
});
