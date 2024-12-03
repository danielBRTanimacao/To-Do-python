const makeEditable = (element, storageKey) => {
    const cachedValue = localStorage.getItem(storageKey);
    if (cachedValue) {
        element.textContent = cachedValue;
    }

    element.addEventListener("click", () => {
        const input = document.createElement("input");
        input.type = "text";
        input.value = element.textContent;
        if (element.id == "subtitleChange") {
            input.classList.add("sb-input");
        }

        element.replaceWith(input);
        input.focus();

        const save = () => {
            element.textContent = input.value;
            localStorage.setItem(storageKey, input.value);
            input.replaceWith(element);
        };

        input.addEventListener("blur", save);
        input.addEventListener("keydown", (e) => {
            if (e.key === "Enter") {
                save();
            }
        });
    });
};

const h1Handle = document.querySelector("#titleChange");
const h4Handle = document.querySelector("#subtitleChange");

makeEditable(h1Handle, "titleChange");
makeEditable(h4Handle, "subtitleChange");

function selectImage() {
    document.getElementById("imageInput").click();
}

function changeImage(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            const imageUrl = e.target.result;
            document.getElementById("imageDisplay").src = imageUrl;
            localStorage.setItem("cachedImageUrl", imageUrl);
        };

        reader.readAsDataURL(file);
    }
}

window.onload = function () {
    const cachedImageUrl = localStorage.getItem("cachedImageUrl");
    if (cachedImageUrl) {
        document.getElementById("imageDisplay").src = cachedImageUrl;
    }
};

function setAlert() {
    const taskItens = document.querySelectorAll("li.task-item");
    const date = new Date();

    taskItens.forEach((element) => {
        const dueDate = new Date(element.dataset.dueDate);
        const alertElement = element.querySelector("span.alert-task");

        if (dueDate < date) {
            alertElement.classList.remove("d-none");
        } else {
            alertElement.classList.add("d-none");
        }
    });
}

setAlert();

let clicked = false;

function removeIconImage() {
    const defaultImage = "https://fakeimg.pl/85x85/";

    if (!clicked) {
        document.getElementById("imageDisplay").src = defaultImage;
        clicked = true;
    } else {
        document.getElementById("imageDisplay").classList.add("d-none");
    }
}

function removeTitle() {
    document.getElementById("titleChange").innerHTML = "";
}

function removeSubTitle() {
    document.getElementById("subtitleChange").innerHTML = "";
}
