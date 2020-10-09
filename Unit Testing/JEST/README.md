<h1 align="center">
	:earth_americas: JEST
</h1>

<h3 align="center">
	A Learning Repository
</h3>

## Matchers

Jest uses matches to let you test values in different ways. This document will introduce some commonly used matchers. 

**Expect** When you're writing tests, you often need to check that values meet certain conditions. expect gives you access to a number of "matchers" that let you validate different things

### Common Matchers

The simples way to test a value is with exact equality.

```
test('two plus two is four', () => {
	expect(2 + 2).toBe(4);
});
```

In this code, expect(2 + 2) returns an "expectation" object. You typically won't do much with these objects except call matchers on them. 

In this code, .toBe(4) is the matcher. When JEST runs, it tracks all the failing matchers so that it can print out nice error messages for you

<mark>toBe</mark> uses Object.is to test exact equality. If you want to check the value of an object, use toEqual instead:

```
test('object assignment', () => {
	const data = {one: 1};
	data['two'] = 2;
	expect(data).toEqual({one: 1, two: 2});
});
```
<mark>toEqual</mark> recursively checks every field of an object or array.

You can also test for the opposite of a matcher:

```
test('adding positive numbers is not zero', () => {
	for(let a = 1; a < 10; a++){
		for(let b = 1; b < 10; b++){
			expect(a + b).not.toBe(0);
		}
	}
});
```

## Truthiness

Sometimes in tests you need to distinguish between undefined, null and false, but sometimes you do not want to treat these differently. JEST contains helpers that let you be explicit about what you want

* toBeNull matches only null
* toBeUndefined matches only undefined
* toBeDefined is the opposite of toBeUndefined
* toBeTruthy matches anything that an if statement treats as true
* toBeFalsy matches anything that an if statement treats as false

For Example: 

```
test('null', () => {
  const n = null;
  expect(n).toBeNull();
  expect(n).toBeDefined();
  expect(n).not.toBeUndefined();
  expect(n).not.toBeTruthy();
  expect(n).toBeFalsy();
});

test('zero', () => {
  const z = 0;
  expect(z).not.toBeNull();
  expect(z).toBeDefined();
  expect(z).not.toBeUndefined();
  expect(z).not.toBeTruthy();
  expect(z).toBeFalsy();
});
```
You should use the matcher that most precisely corresponds to what you want your code to be doing.


___




describe()
it()
expect()

beforeEach()

jest.spyOn()

<AlertDanger
  onCancelPress={[Function]}
  onConfirmPress={[Function]}
  show={false}
  subtitle="DeleteDevice"
  title="Warning!"
/>

























