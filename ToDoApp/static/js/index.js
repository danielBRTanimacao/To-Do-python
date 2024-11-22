const makeEditable = (element) => {
    element.addEventListener("click", () => {
        const input = document.createElement("input");
        input.type = "text";
        input.value = element.textContent;

        element.replaceWith(input);
        input.focus();

        const save = () => {
            element.textContent = input.value;
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

const h1Handle = document.querySelector("h1#titleChange");
const h4Handle = document.querySelector("h4#subtitleChange");

makeEditable(h1Handle);
makeEditable(h4Handle);
