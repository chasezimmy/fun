def balance(chars: List[Char]): Boolean = {
  def f(chars: List[Char], open: Int): Boolean = {
    if (chars.isEmpty) {
      open == 0
    } else {
      var head = chars.head
      var points = 
      	if (head == '(') open + 1
        else if (head == ')') open - 1
        else open
      if (points >= 0) f(chars.tail, points)
      else false
    }
  }
  f(chars, 0) 
}

balance("(())".toList) // true
balance(":-)".toList) // false