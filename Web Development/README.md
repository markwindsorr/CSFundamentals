
<h1 align="center">
	:earth_americas: Javascript
</h1>

<h3 align="center">
	A Learning Repository
</h3>


## Callback function

A callback is a function that is to be executed after another function has finished executing -- hence the name 'call back'.

In javascript, functions are objects. Because of this, functions can take functions as arguments, and can be returned by other functions. Functions that do this are called higher-order functions. Any function that is passed as an argument is called a callback function.

We use callbacks in javascript because it is an event driven language. This means that instead of waiting for a response before moving on, javascript will keep executing while listening for other events.

Here is a basic example: 

```
function first(){
	console.log(1);
}

function second(){
	console.log(2);
}

first();
second();

// 1
// 2
```

What if function first contains some sore of code that can't be executed immediately? For example, an API request where we have to send the request then wait for a response? To simulate this action, we're going to use setTimeout which is a javascript function that calls a function after a set amount of time. We'll delay our function for 500 milliseconds to simulate an API request

```
function first(){
	//Simulate a code delay
	setTimeout( function(){
		console.log(1);
	}, 500);
}

function second(){
	console.log(2);
}

first();
second();

// 2
// 1
```

Javascript didn't wait for a response from first() before moing on to execute second().

This is shown because you can't just call one function after another and hope they execute in the right order.
**Callbacks are a way to make sure certain code doesn't execute until other code has already finished execution**

### Create a Callback

```
function doHomework(subject) {
	alert('Starting my ${subject} homework.')
}

doHomework('Math');

// Alerts: Starting my math homework
```
Now lets add our callback -- as our last parameter in the doHomework() function we can pass in callback. The callback function is then defined in the second argument of our call to doHomework().

```
function doHomework(subject, callback) {
  alert(`Starting my ${subject} homework.`);
  callback();
}

doHomework('math', function() {
  alert('Finished my homework');
});

// 'starting my Math homework'
// 'finished my homework'
```

Callback functions don't always have to be defined in our function call. They can be defined elsewhere in our code like this:

```
function doHomework(subject, callback) {
  alert(`Starting my ${subject} homework.`);
  callback();
}
function alertFinished(){
  alert('Finished my homework');
}
doHomework('math', alertFinished);
```

## Callback vs Promise

**Callback**

```
first(2, function(firstResult, error) {
	if (!error) {
		second(firstResult, function(secondResult, error){
			if(!error) {
				third(secondResult, error) {
					if (!error) {
						console.log(thirdResult);
					}
				});
			}
		});
	}
});

function first(value, callback){
	callback(value+1, false);
}

function second(value, callback){
	callback(value+2), false);
}

function third(value, callback){
	callback(value+1, false);
}

```

**Promise**

```
var promise = new Promise(function(resolve, reject) {
	resolve(2);
)};

//don't execute the function after .then until you get a result
promise.then(first).then(second).then(third).then(function(response)){
	console.log(response);
});

function first(value, callback){
	callback(value+1, false);
}

function second(value, callback){
	callback(value+2), false);
}

function third(value, callback){
	callback(value+1, false);
}
```



## Double Equals vs Triple Equals

**Triple Equals ===** we are testing for strict equality. This means both the type and the value we are comparing have to be the same.

**Double Equals ==** we are testing for loose equality. Double equals also performs type coercion.

Type coercion means that two values are compared only after attempting to convert them into a common type.

```
123 == "123" evaluates to true 
123 === "123" evaluates to false 

false == 0 evaluates to true
false === 0 evaluates to false
```

There are six falsy values in JavaScript you should be aware of:

* false -- boolean false
* 0 -- number zero
* "" -- empty string
* null 
* undefined
* NaN -- not a number

Memorizing the six falsy values and the rules associated with them can go a long way towards understanding loose equality

Triple equals is superior to double equals. Whenever possible, you should use triple equals to test equality. By testing the type and value you can be sure that you are always executing a true equality test.

## A Promise

A Promise is an object representing the eventual completion or failure of an asynchronous operation. 

A promise is a returned object to which you attach callbacks, instead of passing callbacks into a function.

Imagine a function, createAudioFileAsync(), which asynchronously generates a sound file given a configuration record and two callback functions, one called if the audio file is successfully created, and the other called if an error occurs.

```
function successCallback(result) {
	console.log("Audio file ready at URL: " + result);
}

function failureCallback(error) {
	console.error("Error generating audio file: " + error);
}

createAudioFileAsync(audioSettings, successCallback, failureCallback);
```

Modern functions that return a promise, yuo can attach your callbacks to instead:

If createAudioFileAsync() were rewritten to return a promise, using it could be as simple as this:

```
createAudioFileAsync(audioSettings).then(successCallback, failureCallback);

// Which is shorthand for:

const promise = createAudioFileAsync(audioSettings); 
promise.then(successCallback, failureCallback);
```

We call this an asynchronous function call.


___

To collect data from multiple children, or to have two child components communicate with each other, you need to declare the shared state in their parent component instead. The parent component can pass the state back down to the children by using props; this keeps the child components in sync with each other and with the parent component.

### Data change with Mutation

```
var player = {score: 1, name: "Mark"};
player.score = 2;
```

### Data change without mutation

```
var player = {score: 1, name: "Mark"};
var newPlayer = Object.assign({}, player, {score: 2});

// Now player is unchanged, but newPlayer is {score: 2, name: 'Jeff'}

// Or if you are using object spread syntax proposal, you can write:
// var newPlayer = {...player, score: 2};
```

The former result is the same but by not mutating or changing the underlying data directly, we gain benefits:

* Complex Features become simple. Avoiding direct data mutation lets us keep previous versions of the games history intact, and reuse them later

* Detecting Changes is easier with immutable objects.

* Determining when to re-render in react. The main benefit of immutability is that it helps you build pure components in React. Immutable data can easily determine if changes have been made which helps to determine when a component requires re-rendering.

In React, function components are a simpler way to write components that only contain a render method and don’t have their own state. Instead of defining a class which extends React.Component, we can write a function that takes props as input and returns what should be rendered. Function components are less tedious to write than classes, and many components can be expressed this way.






