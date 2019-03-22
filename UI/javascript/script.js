var attempt = 3;
function login(email, password){

    if(email==="admin@gmail.com" && password ==="admin123"){
        alert('Login successfull')
        window.location.href = "./admin.html"; // Redirecting to admin page.
    }
    else if (login_form.email.value == 'user@gmail.com' && login_form.password.value == 'user123'){
        alert('Login successfull')
        window.location.href = "./user.html";    //redirect to user
    }
    else{
           const errormessage = document.getElementById("error");
           errormessage.innerText = "Invalid login"
       }
       
  }
  
  const loginForm = document.getElementById("login_form");
  loginForm.addEventListener("submit", (event)=>{
      event.preventDefault()
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value; 
      login(email, password)
    })