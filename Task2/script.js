function saveData()
{
    let gender = document.querySelector('input[name="gender"]:checked').value;

    localStorage.setItem("fname", document.getElementById("fname").value);
    localStorage.setItem("lname", document.getElementById("lname").value);
    localStorage.setItem("email", document.getElementById("email").value);
    localStorage.setItem("phone", document.getElementById("phone").value);
    localStorage.setItem("gender", gender);
    localStorage.setItem("country", document.getElementById("country").value);

    window.location.href="table.html";
}