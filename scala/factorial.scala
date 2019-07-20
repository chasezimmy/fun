def factorial(n: Int, sum: Int = 1): Int = {
    if (n == 0) sum
    else factorial(n - 1, sum * n)
}

println(factorial(4))