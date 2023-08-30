const addItemForm = document.querySelector("#add-items-form");
const popup = document.querySelector("#popup");

addItemForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const Title = addItemForm.querySelector('input[name="title"]').value;
    const Description = addItemForm.querySelector('input[name="description"]').value;

    const user_id = localStorage.getItem("user_id"); // Get the user ID from local storage

    const itemData = {
        title: Title,
        description: Description,
    };

    try {
        const response = await fetch(`http://127.0.0.1:8000/users/${user_id}/items/`, { method: "POST",headers: {
                'Content-type': 'application/json',},body: JSON.stringify(itemData),});

        const data = await response.json();

        if (response.status === 200) {
            
            // Show popup on successful item addition
            popup.style.display = "block";
            setTimeout(() => { popup.style.display = "none";}, 2000); // Hide popup after 2 seconds

            // Clear input fields for next item
            addItemForm.querySelector('input[name="title"]').value = "";
            addItemForm.querySelector('input[name="description"]').value = "";
        } 
        else {
            console.log("Item addition failed:", data.message);
        }
    } 
    catch (error) {
        console.error("Error:", error);
    }
});
