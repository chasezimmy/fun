import scala.collection.mutable.ArrayBuffer

def pascal(C: Int, R: Int): Unit = {
  var P: ArrayBuffer[Int] = ArrayBuffer()
  var c: Int = 0
  var r: Int = 0
	def calc(i: Int): Int = {
    if (c == 0) 1
    else if (c == r) 1
    else P(i - r - 1) + P(i - r)
  }
    
  def loop: Unit = {
    for (i <- 0 to 20) {
      P += calc(i)
      if (C == c && R == r) println(calc(i))
      
      if (c > r) {
        r = r + 1
      }
      else if (c == r) {
        r = r +1
        c = 0 
      }
      else if (c < r) {
        c = c + 1
      }
    }
  }
  loop
  
}
  
pascal(1, 2)