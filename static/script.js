document.addEventListener("DOMContentLoaded", function () {
    let unitSelect = document.getElementById("unitSelect");
    let signatureImage = document.getElementById("signatureImage");
    let phoneInput = document.getElementById("phoneInput");

    unitSelect.addEventListener("change", function () {
        const selectedUnit = unitSelect.value;

        if (selectedUnit === "Platina") {
            signatureImage.src = "static/img/02-platina.png";
            email_input.value = "@platinacsc.com.br";
        } else if (selectedUnit === "Masterline") {
            signatureImage.src = "static/img/01-masterline.png";
            email_input.value = "@masterline.ind.br";
        }
    });

    phoneInput.addEventListener("input", function () {
        formatPhoneNumber(this);
    });
});

const applyPhoneNumberMask = (input) => {
    let phoneNumber = input.value.replace(/\D/g, ''); // Remove caracteres não numéricos

    if (phoneNumber.length == 11) {
        phoneNumber = `+55 (${phoneNumber.slice(0, 2)}) ${phoneNumber.slice(2, 7)}-${phoneNumber.slice(7, 11)}`;
    } else if (phoneNumber.length == 10) {
        phoneNumber = `+55 (${phoneNumber.slice(0, 2)}) ${phoneNumber.slice(2, 6)}-${phoneNumber.slice(6, 10)}`;
    }

    input.value = phoneNumber;
};

phoneInput.addEventListener("input", function () {
    applyPhoneNumberMask(this);
});





