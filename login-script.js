// selects the HTML element with the ID "login-form","popup" and assigns it to the loginForm,popup constant

const loginForm = document.querySelector("#login-form");
const popup = document.querySelector("#popup");

// When the form is submitted, the provided async function is executed. 
//The event parameter represents the event object associated with the form submission.

loginForm.addEventListener("submit", async function (event) {
    event.preventDefault();


    ///These lines retrieve the values entered by the user in the email and password input fields of the form.
    const email = loginForm.querySelector('input[name="email"]').value;
    const password = loginForm.querySelector('input[name="password"]').value;


    // It uses these values to prepare data that will be sent to the server.
    const userData = {
        email: email,
        password: password,
    };

    try {
        //This line makes an asynchronous HTTP POST request to the specified URL using the fetch API. 
        //It sends the userData object in the request body as JSON. The await keyword indicates that 
        //the code will wait for the response to be received before continuing.

        const response = await fetch("http://127.0.0.1:8000/users/", { method: "POST",headers: 
        {'Content-type': 'application/json'}, body: JSON.stringify(userData),});

        const data = await response.json();

        // response status is 200 (OK), indicating a successful response.
        if (response.status === 200) {

            // Set the user ID in local storage for later use
            localStorage.setItem("user_id", data.id);

            // Login successful, redirect to add-items page(another window)
            window.location.href = "add-items.html";


            // Clear input fields for next registration
            loginForm.querySelector('input[name="email"]').value = "";
            loginForm.querySelector('input[name="password"]').value = "";
        } 
        else {

            //They first set it to "block" to make the popup visible, and then
            //use setTimeout to hide the popup after 2 seconds by setting its display style back to "none".
            
            popup.style.display = "block";
            setTimeout(() => { popup.style.display = "none";}, 2000); // Hide popup after 2 seconds

            console.log("Login failed:", data.message);
        }
    } 
    catch (error) {
        console.error("Error:", error);
    }
});
