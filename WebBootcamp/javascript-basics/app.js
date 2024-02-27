let age = 32;
let userName = "Max";
let hobbies = ["Sports", "Cooking", "Reading"];
let job = {
  title: "Developer",
  place: "New York",
  salary: 50000,
};

function calculateAdultYears(userAge) {
  return userAge - 18;
}

console.log(calculateAdultYears(age));

age = 45;
console.log(calculateAdultYears(age));

let person = {
  name: "Max", // property
  greet() {
    // method
    console.log("Hello!");
  },
};

person.greet();
