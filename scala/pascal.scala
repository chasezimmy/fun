import scala.collection.mutable.ArrayBuffer

// Recursion
def pascal(row: Int, column: Int): Int =
    if (row == column || column == 0) 1
		else pascal(column - 1, row - 1) + pascal(column, row - 1) 

pascal(1, 2) // 2

// What have I done?
def pascalTerrible(column: Int, row: Int): Int = {
  var P: ArrayBuffer[Int] = ArrayBuffer()
  var c: Int = 0
  var r: Int = 0
  
	def calc(i: Int): Int = {
    if (c == 0 or c == r) 1
    else P(i - r - 1) + P(i - r)
  }
    
  def loop: Int = {
    var i: Int = 0
    while (!(column == c && row == r)) {
      P += calc(i)
      i = i + 1
      if (c > r) {
        r = r + 1
      } else if (c < r) {
        c = c + 1
      } else {
        r = r +1
        c = 0  
      }
    } 
    calc(i)
  }
  loop
}
  
pascalTerrible(1, 2) // 2