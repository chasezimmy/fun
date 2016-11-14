

function largestContinuousSum(arr) {
	if (arr.length == 0) return "None";

	var maxSum = arr[0];
	var currentSum = arr[0];

	//console.log(arr.slice(1,arr.length));
	arr.shift();
	arr.forEach(function(entry) {
		currentSum = Math.max(currentSum+entry, entry);
		maxSum = Math.max(currentSum, maxSum);
	});

	console.log(maxSum);
}


arr = [1, 2, -1, -5, 1];
largestContinuousSum(arr);