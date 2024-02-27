let courseName = "Web Development - The Complete Guide";
let coursePrice = 39;
let courseGoals = [
  "Learn Web Development",
  "Become a web developer",
  "Have fun!",
];

alert(courseName);
alert(coursePrice);
alert(courseGoals);

let onlineCourse = { name: courseName, price: coursePrice, goals: courseGoals };

alert(onlineCourse.name);
alert(onlineCourse.price);
alert(onlineCourse.goals);

alert(onlineCourse.goals[1]);

function getListItem(array, arrayIndex) {
  let arrayElement = array[arrayIndex];
  return arrayElement;
}

let firstGoal = getListItem(onlineCourse.goals, 0);
alert(firstGoal);
