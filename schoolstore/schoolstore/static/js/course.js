 // Show/hide the form when the button is clicked
     document.getElementById("showFormButton").addEventListener("click", function() {
            var form = document.getElementById("myForm");
            form.style.display = "block";
        });

        document.getElementById("submitButton").addEventListener("click", function() {
            var form = document.getElementById("myForm");
            form.style.display = "block";
        });




document.getElementById("Department").addEventListener("change", function () {
    var Department = this.value;
    var CoursesSelect = document.getElementById("Courses");

    // Clear the existing options
    CoursesSelect.innerHTML = "";

    // Create an array of course options based on the selected department
    var courseOptions = [];

    if (Department === "IT") {
        courseOptions = ["Select a Course", "IT", "Data Analytics", "Cyber Security"];
    } else if (Department === "Commerce") {
        courseOptions = ["Select a Course", "BCom", "MCom"];
    } else if (Department === "Mathematics") {
        courseOptions = ["Select a Course", "BSc Maths","MSc Maths"];
    } else if (Department === "Physics") {
        courseOptions = ["Select a Course","BSc Physics","MSc Physics"];
    } else if (Department === "Chemistry") {
        courseOptions = ["Select a Course", "BSc Chemistry","MSc Chemistry"];
    }

    // Populate the "Courses" dropdown with the options
    courseOptions.forEach(function (course) {
        var option = document.createElement("option");
        option.value = course;
        option.text = course;
        CoursesSelect.appendChild(option);
    });
});
