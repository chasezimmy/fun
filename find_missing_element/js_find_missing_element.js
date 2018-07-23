// Find Missing Element
// http://www.ardendertat.com/2011/09/27/programming-interview-questions-4-find-missing-element/

function findMissingElement(arr1, arr2) {
	if (arr1.length == 0 || arr2.length == 0) return "None";
	res = 0;
	merge = arr1.concat(arr2);
	merge.forEach(function(entry) {
		res^=entry;
	});
	return res;
}

a1 = [4, 1, 0, 2, 9, 6, 8, 7, 5, 3];
a2 = [6, 4, 7, 2, 1, 0, 8, 3, 9];

console.log(findMissingElement(a1, a2));